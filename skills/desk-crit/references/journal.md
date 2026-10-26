# Progress journal

File: `./.desk-crit/student.md` in the student's working directory. Work versions: `./.desk-crit/works/<slug>-vN.png` (downscaled with `annotate.py prep`). If the folder is a git repo, `.desk-crit/` must be in `.gitignore`.

Privacy: learning data only. No names, schools, employers, grades, ages or personal details.

## Template

```markdown
# Desk crit journal

Level (overall): beginner
Goal: <one line from the student, e.g. "first junior UI job">
Language: ru

## Skill levels (1–5)
| Area | Level | Evidence (latest) |
|---|---|---|
| hierarchy | 2 | 2026-05-02 poster: date buried |
| contrast | 2 | |
| alignment | 1 | 3 sessions: mixed centred/left |
| rhythm | 2 | |
| typography | 2 | 4 display fonts on poster v1 |
| color | 3 | |
| composition | 2 | |

## Recurring issues
- alignment: mixed axes. Seen 2026-04-18, 2026-04-25, 2026-05-02 (3×)

## Fixed
- typography: too many fonts. Fixed in poster v2 (2026-05-09)

## Works
- jazz-poster: v1 2026-05-02, v2 2026-05-09 → works/jazz-poster-v2.png

## Exercises
| ID | Exercise | Given | Status | Outcome |
|---|---|---|---|---|
| E14 | Invisible lines (alignment) | 2026-05-02 | done | 3 alignment lines instead of 7 |
| E03 | Squint & rank (hierarchy) | 2026-05-09 | open | |

## Next focus
alignment → then hierarchy

## Sessions
### 2026-05-09 · jazz-poster v2
Improved: font count 4→2, clear date. Open: alignment. Exercise: E03.

## History
<consolidated summary of older sessions>
```

## Level rubric (per area)

1. **Unaware**: the problem is everywhere and not noticed.
2. **Aware**: notices when pointed out; fixes are inconsistent.
3. **Competent**: mostly correct in simple layouts; slips under complexity.
4. **Fluent**: consistent; makes deliberate choices; small slips only.
5. **Expert**: uses the principle expressively; can explain trade-offs.

Change a level by at most 1 per session, and only with visible evidence in the work. Lower it only if a regression repeats.

## Recurrence and escalation

- Same area + same kind of mistake = same issue. Track dates.
- 2nd occurrence: mention it. 3rd+: escalate in the crit and make it the exercise target.
- Move an issue to **Fixed** when a new work shows it solved (not just the exercise).

## Exercises

- Status: `open`, `done`, `skipped`. Ask about open exercises at the start of a session.
- `done` needs a one-line outcome from what the student showed or said.
- Don't reassign a `done` exercise; give a harder variant or a different one from the same area.

## Consolidation (when the file exceeds ~150 lines)

1. Keep the last 5 sessions in full.
2. Merge older sessions into **History** as 3–6 lines: date range, main themes, levels at that time.
3. Keep all exercise rows, but collapse `done` rows older than 2 months into one line per area ("alignment: E14, E15 done").
4. Never delete Recurring issues or Fixed entries; shorten their text if needed.
