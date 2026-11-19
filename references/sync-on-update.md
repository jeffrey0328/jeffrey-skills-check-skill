# Sync when another skill updates

This skill is **常驻**. When it is attached and **any other skill** under the current agent app’s default skills path is created or updated this turn, run this sync before ending the turn.

**读法:** § Resident for the always-on duty; § Companion sync for what to align; § New skill for a folder just added to the fleet.

## Resident (always-on)

1. Run the update-time check on the changed skill (`agent-check.md` full depth + `skill-authoring.md` § Agent-specific spec file): current-app spec conformance, agent-only fixes to its `agent/<agent>` branch.
2. Run § Companion sync for the companions that drifted.
3. End the turn with a one-line Chinese note of what was synced.

Pure typo/format fixes with no Route / `description` / workflow change: skip companion rewrites; say so in one line.

## Companion sync

When you change a skill’s workflow, constraints, triggers, examples, or layout (typical skill authoring turn):

| Companion | Sync when |
|-----------|-----------|
| `README.md` / `README-EN.md` | Purpose, triggers, install, or capabilities changed (keep both files in sync, same facts) |
| `kind.txt` | Only when the user asks to switch 演进 / 底本 |
| `references/cross-reference.md` | Files or cited `##` / `§` headings were added, renamed, moved, or deleted |

Authoring detail: `skill-authoring.md` § Synchronize companion files.

## New skill added to the fleet

1. Check it against `skill-authoring.md` (shape, companions, id, 叫法, language, invoke mode) — fix gaps in this turn.
2. Register the pointer in the skills fleet repo when the fleet tracks it (`.gitmodules` + gitlink), per that fleet’s own rules.
3. Report the new skill and its invoke mode in the turn’s Chinese summary.

## Must

- While this skill is attached, run the update-time check + companion sync for every other skill created or updated this turn. *(see § Resident)*
- Sync the human companions in the table when that skill’s substance changes.

## Must not

- End the turn with a changed skill whose companions drifted, without syncing or saying why not. *(← Must: resident sync)*