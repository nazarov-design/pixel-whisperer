# Results v1.0

5 cases per skill, Claude Sonnet, same prompt with and without the skill. Both conditions run isolated from user skills, plugins and MCP (see `tools/run_claude.sh`). A blind Claude Opus judge scored A/B in random order with [rubric.md](rubric.md). This is an AI judge on a small sample, so treat it as a sanity check rather than proof. Human scoring is welcome.

## feedback-decoder (f04, f06, f10, f11, f17)

| Criterion | Without | With |
|---|---|---|
| specificity | 3.2 | 5.0 |
| grounding | 3.6 | 4.4 |
| interpretation | 2.0 | 5.0 |
| conflicts & scope | 3.0 | 5.0 |
| client reply | 2.0 | 4.8 |
| usability | 4.0 | 3.8 |
| **overall** | **2.97** | **4.67** |

Without the skill, Claude often redesigned the screen itself and skipped the client reply. In f10 it produced new files instead of a decode.

## desk-crit (s04–s08)

| Criterion | Without | With |
|---|---|---|
| prioritization | 2.0 | 4.8 |
| accuracy | 4.0 | 3.8 |
| teaching | 2.6 | 4.6 |
| exercise | 1.0 | 4.8 |
| tone | 3.8 | 4.6 |
| actionability | 4.0 | 4.6 |
| **overall** | **2.90** | **4.53** |

Without the skill, crits were accurate but came as 7–17-point lists with no exercise.

## Weak spots found and fixed (v1.0.1 rules)

- Numbers sometimes contradicted each other, and one measurement was wrong. A self-check step was added.
- The level a student stated was overridden. It is now respected.
- Answers ran long. There is now a length budget.
- Some answers ended with tool chatter. That is now forbidden.

Recheck after the fixes (without → with): f04 2.67 → 4.83, f06 3.5 → 4.5, s06 3.0 → 4.67, s07 3.17 → 4.5. Accuracy is still the weakest criterion for the skills.

Full side-by-side outputs: `runs/*/REPORT.md`. To reproduce: `python3 benchmark/run_benchmark.py run --suite feedback --all`.
