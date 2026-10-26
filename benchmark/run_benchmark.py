#!/usr/bin/env python3
"""Compare Claude with and without a pixel-whisperer skill, side by side.

  run     --suite feedback|crit [--ids f04,f06 | --all] [--model sonnet] [--jobs 4] [--out DIR]
  judge   --out DIR [--model opus]      blind A/B scoring with rubric.md (optional)
  report  --out DIR                     writes DIR/REPORT.md with outputs side by side

Both conditions run headless Claude Code with user settings, user skills, user
plugins and MCP servers excluded (see tools/run_claude.sh). "with" adds only this
repo's plugin. Each case gets a fresh working folder, so no journal or ledger leaks
between runs.
"""
import argparse
import concurrent.futures as cf
import datetime
import json
import os
import random
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
RUNNER = os.path.join(REPO, "tools", "run_claude.sh")
SUITES = {
    "feedback": (os.path.join(HERE, "feedback-cases", "cases.json"), os.path.join(HERE, "designs")),
    "crit": (os.path.join(HERE, "student-works", "works.json"), os.path.join(HERE, "student-works")),
}


def load_cases(suite):
    path, img_dir = SUITES[suite]
    with open(path, encoding="utf-8") as fh:
        cases = json.load(fh)
    for c in cases:
        c["image_path"] = os.path.join(img_dir, c.get("design") or c["image"])
    return cases


def prompt_for(suite, c):
    if suite == "feedback":
        return (f"Client feedback on this design (design.png in this folder).\n\n"
                f"Brief: {c['brief']}\n\nClient message:\n> {c['message']}\n")
    return f"{c['prompt']}\n\n(The work is design.png in this folder.)\n"


def run_one(suite, c, mode, out, model):
    work = os.path.join(out, c["id"], mode)
    os.makedirs(work, exist_ok=True)
    shutil.copy(c["image_path"], os.path.join(work, "design.png"))
    pfile = os.path.join(out, c["id"], "prompt.txt")
    with open(pfile, "w", encoding="utf-8") as fh:
        fh.write(prompt_for(suite, c))
    result = os.path.join(out, c["id"], f"{mode}.md")
    subprocess.run([RUNNER, work, pfile, mode, result, model], check=False)
    return c["id"], mode


def cmd_run(a):
    cases = load_cases(a.suite)
    if not a.all:
        wanted = set(a.ids.split(","))
        cases = [c for c in cases if c["id"] in wanted]
    if not cases:
        sys.exit("No cases selected. Use --ids or --all.")
    out = os.path.abspath(a.out or os.path.join(HERE, "runs", datetime.date.today().isoformat() + "-" + a.suite))
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "meta.json"), "w") as fh:
        json.dump({"suite": a.suite, "model": a.model, "ids": [c["id"] for c in cases]}, fh)
    jobs = [(c, m) for c in cases for m in ("with", "without")]
    with cf.ThreadPoolExecutor(a.jobs) as pool:
        for cid, mode in pool.map(lambda j: run_one(a.suite, j[0], j[1], out, a.model), jobs):
            print(f"done {cid} {mode}")
    print(f"Outputs in {out}")


def read(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        return "(missing)"


def cmd_judge(a):
    a.out = os.path.abspath(a.out)
    meta = json.load(open(os.path.join(a.out, "meta.json")))
    rubric = read(os.path.join(HERE, "rubric.md"))
    section = "Feedback Decoder" if meta["suite"] == "feedback" else "Desk Crit"
    scores = {}
    for cid in meta["ids"]:
        d = os.path.join(a.out, cid)
        order = ["with", "without"]
        random.shuffle(order)  # blind: the judge never learns which is which
        jp = os.path.join(d, "judge_prompt.txt")
        with open(jp, "w", encoding="utf-8") as fh:
            fh.write(
                f"You are a senior product designer scoring two AI responses blind. "
                f"Look at design.png in this folder first. Use the '{section}' rubric below. "
                f"Score each response 1-5 per criterion. Judge substance, not length. "
                f"Reply with JSON only: {{\"A\": {{criterion: score}}, \"B\": {{...}}, \"note\": \"one sentence\"}}.\n\n"
                f"RUBRIC:\n{rubric}\n\nTASK GIVEN TO BOTH:\n{read(os.path.join(d, 'prompt.txt'))}\n\n"
                f"RESPONSE A:\n{read(os.path.join(d, order[0] + '.md'))}\n\n"
                f"RESPONSE B:\n{read(os.path.join(d, order[1] + '.md'))}\n")
        jdir = os.path.join(d, "judge")
        os.makedirs(jdir, exist_ok=True)
        shutil.copy(os.path.join(d, "with", "design.png"), os.path.join(jdir, "design.png"))
        raw = os.path.join(d, "judge.json.txt")
        subprocess.run([RUNNER, jdir, jp, "without", raw, a.model], check=False)
        m = re.search(r"\{.*\}", read(raw), re.S)
        try:
            parsed = json.loads(m.group(0))
            scores[cid] = {order[0]: parsed["A"], order[1]: parsed["B"], "note": parsed.get("note", "")}
            print(f"judged {cid}")
        except (AttributeError, json.JSONDecodeError, KeyError):
            print(f"could not parse judge output for {cid}; see {raw}")
    with open(os.path.join(a.out, "scores.json"), "w") as fh:
        json.dump(scores, fh, indent=2, ensure_ascii=False)


def cmd_report(a):
    meta = json.load(open(os.path.join(a.out, "meta.json")))
    scores = {}
    if os.path.exists(os.path.join(a.out, "scores.json")):
        scores = json.load(open(os.path.join(a.out, "scores.json")))
    lines = [f"# Benchmark report: {meta['suite']} (model: {meta['model']})", ""]
    if scores:
        lines += ["| Case | Without skill | With skill | Judge note |", "|---|---|---|---|"]
        for cid in meta["ids"]:
            s = scores.get(cid)
            if not s:
                continue
            avg = lambda d: sum(d.values()) / len(d)
            lines.append(f"| {cid} | {avg(s['without']):.1f} | {avg(s['with']):.1f} | {s['note']} |")
        lines.append("")
    for cid in meta["ids"]:
        d = os.path.join(a.out, cid)
        lines += [f"## {cid}", "", "**Prompt**", "", "```", read(os.path.join(d, "prompt.txt")).strip(), "```", ""]
        lines += ["<table><tr><th>Without skill</th><th>With skill</th></tr><tr><td valign=\"top\">", "",
                  read(os.path.join(d, "without.md")), "", "</td><td valign=\"top\">", "",
                  read(os.path.join(d, "with.md")), "", "</td></tr></table>", ""]
    with open(os.path.join(a.out, "REPORT.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(os.path.join(a.out, "REPORT.md"))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("run")
    s.add_argument("--suite", choices=SUITES, required=True)
    s.add_argument("--ids", default="")
    s.add_argument("--all", action="store_true")
    s.add_argument("--model", default="sonnet")
    s.add_argument("--jobs", type=int, default=4)
    s.add_argument("--out")
    s.set_defaults(fn=cmd_run)
    s = sub.add_parser("judge")
    s.add_argument("--out", required=True)
    s.add_argument("--model", default="opus")
    s.set_defaults(fn=cmd_judge)
    s = sub.add_parser("report")
    s.add_argument("--out", required=True)
    s.set_defaults(fn=cmd_report)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
