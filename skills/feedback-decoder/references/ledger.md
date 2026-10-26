# Revision ledger

File: `./.feedback-decoder/<project-slug>.md` in the user's working directory. One file per project. The slug describes the work (`coffee-site`, `fintech-app`), never a client or person name.

## Privacy rules

- No names, emails, phone numbers, company names (unless the user explicitly asks), or money amounts.
- Refer to "the client". Quote feedback only as short fragments needed to track requests.
- If the folder is a git repo, make sure `.feedback-decoder/` is in `.gitignore`.

## Template

```markdown
# Ledger: <project-slug>

Agreed rounds: 3
Brief scope: <one line, e.g. "homepage + menu page, desktop + mobile">
Out of scope (agreed): <one line or "—">

## Rounds
| Round | Date | Items | In scope | New requests | Status |
|---|---|---|---|---|---|
| 1 | 2026-05-02 | 5 | 5 | 0 | done |
| 2 | 2026-05-09 | 4 | 3 | 1 (#2.4 online ordering) | in progress |

## New requests log
- #2.4 online ordering: outside brief → scope message sent? yes/no

## Decisions
- R1: keep warm palette (client liked it)
- R2: client chose variant A for CTA
```

## Update rules

- A **round** = one batch of client feedback answered with one delivery. Several messages before you deliver count as one round. Ask the designer if unsure.
- Append; don't rewrite history. Update the current round's status when the designer confirms delivery.
- Item IDs are `<round>.<n>` and match the decode table rows.
- Record decisions the client made (chosen variants, things to keep) so later rounds don't reopen them.
- If rounds used ≥ agreed: say so at the top of the answer and include the round-limit message.
