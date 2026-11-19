# Memory norms & checks

Auto-memory (user scope and project scope) is written and read per the current agent app’s memory mechanism plus `preferences.md`. Memory is context for what was true when written — never a substitute for reading current state.

**读法:** § Write for creating/updating entries; § Read for using entries; § Check list for the gate.

## Write

- Save only what persists across conversations: user role/preferences, feedback (corrections and confirmed non-obvious approaches, with the reason), project decisions/owners/deadlines not derivable from code or git (absolute dates), references to external resources.
- One topic per file; the scope’s `MEMORY.md` index links every topic file with a one-line hook. Keep the index and files in sync both ways.
- Conversation-only state belongs in plans or tasks, not memory.
- No secrets, tokens, or machine-local values in memory that syncs as committed content; project-scoped memory stays on disk (its folder name encodes machine paths).
- Save immediately when Jeffrey explicitly asks to remember; find and remove the entry when he asks to forget.

## Read

- Read the index and the linked topic files when relevant; always when Jeffrey asks to check/recall/remember.
- Before acting on a memory that names a file, function, or flag: verify it still exists (Read / Grep). A repo-state snapshot in memory is frozen in time — for recent/current state prefer `git log` or the code.
- When memory conflicts with what you observe now, trust the observation and update the entry.
- If Jeffrey says to ignore memory: do not apply, cite, or compare against it.

## Check list (full)

| Check | Pass |
|-------|------|
| Index integrity | Every `MEMORY.md` link resolves to an existing topic file; every topic file is indexed |
| Type fit | Each entry matches its type (user / feedback / project / reference); conversation-only state is not stored |
| Freshness | Entries naming files/functions/flags verified against current state; stale entries updated or marked |
| Secrets / machine values | None in synced memory content |
| Scope | User-scope facts in user memory; project facts in project memory; no cross-scope duplication |

Quick check (before use): the entry’s factual claims verified against current state; index link resolves.

## Must

- Verify a memory’s factual claims against current files before recommending or acting on them.
- Keep each scope’s index and topic files in sync.
- Trust current observation over a conflicting memory, and update the entry.

## Must not

- Store conversation-only state in memory. *(← Must: memory holds cross-conversation facts; plans/tasks hold the rest)*
- Act on a memory-named path or symbol without verifying it exists now. *(← Must: verify before acting)*