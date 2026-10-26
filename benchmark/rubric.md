# Scoring rubric

For human designers (and the optional blind AI judge). Score each response 1–5 per criterion without knowing which one used the skill. Hide the file names, or have someone else shuffle them into A/B.

**Scale:** 1 = missing or wrong · 2 = weak · 3 = acceptable · 4 = good, a designer would use it with small edits · 5 = excellent, ready to use.

## Feedback Decoder

| Criterion | What a 5 looks like |
|---|---|
| **specificity** | Changes are concrete and measurable (element + from → to values), not "make it bolder". |
| **grounding** | Changes refer to elements actually visible in the design; no invented elements or values. |
| **interpretation** | Plausible readings of vague phrases, ranked, honest about uncertainty; asks when it should. |
| **conflicts_scope** | Spots contradictions between requests, with the brief or accessibility; flags out-of-scope requests and round limits. |
| **client_reply** | Reply is in the client's language, warm and professional, could be sent with minimal edits; handles scope politely. |
| **usability** | Scannable, right length, the designer knows what to do in under a minute. |

## Desk Crit

| Criterion | What a 5 looks like |
|---|---|
| **prioritization** | Focuses on the 1–3 issues that matter most for this work; no laundry list. |
| **accuracy** | Observations are correct and point to specific places in the work. |
| **teaching** | Names the principle behind each issue and why it matters, calibrated to the stated level. |
| **exercise** | One concrete, time-boxed exercise targeting the main weakness, with a clear "done" check. |
| **tone** | Kind and honest: specific praise, no grade inflation, no harshness; in the student's language. |
| **actionability** | The student knows exactly what to do next. |

## How to run a human scoring session

1. `python3 benchmark/run_benchmark.py run --suite feedback --all` (and `--suite crit`).
2. `python3 benchmark/run_benchmark.py report --out <run dir>` and strip the "with/without" headers, or copy outputs into a form as A/B in random order.
3. Ask 3+ designers to score independently. Average per criterion; report the spread, not just the mean.
