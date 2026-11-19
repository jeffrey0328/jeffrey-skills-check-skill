# Plugin norms & checks

Plugins are created and maintained per the **current agent app’s plugin spec** (manifest layout, bundled skill/agent/hook/MCP structure, version fields, install mechanism) plus `preferences.md`. Read that spec first; the app’s own plugin-authoring skill (when it has one) is the how-to — this file is the check standard.

**读法:** § Structure for authoring/shape; § Version & pins for release checks; § Install records for machine state; § Check list for the gate.

## Structure

- A plugin bundles its content in the layout the current app’s spec defines: manifests, bundled skills, agents, hooks, commands, MCP config — each where that spec puts them.
- Bundled skills follow `skill-authoring.md` like any other skill, with the plugin’s packaging rules on top (e.g. a bundled skill pinned as a submodule is edited in its source repo, never hand-edited inside the plugin tree).
- MCP config travels as sanitized examples only; no API keys, tokens, or machine-local paths in committed plugin content.
- Wording: no specific agent app name or project name in shared plugin content — `skill-authoring.md` § Agent-app names.

## Version & pins

- All version manifests of a plugin stay equal to each other and to the product’s release version when the plugin ships with a product.
- Submodule pins point at commits that exist on their declared remotes; after a pin bump the working tree is updated to the pin (`git submodule update --init --recursive`).
- A content change (bundled skill body, manifest, MCP config) ships as a new plugin version through the product’s established release path — updating a bundled skill alone does not count as shipping.
- After a release, the plugin instance installed in the working agent is refreshed and its version verified against the release.

## Install records

- Install output and per-machine state (caches, runtime data, records embedding absolute install paths) are never committed.
- What travels is the sanitized lock inventory: one entry per plugin with id, display name, version, scope, market id/source, visibility, enabled — no paths, no timestamps.
- The lock is regenerated whenever a plugin is installed, removed, or toggled; enabled-plugin settings and the lock agree.

## Check list (full)

| Check | Pass |
|-------|------|
| Manifest layout | Matches the current app’s plugin spec; all required manifests present and mutually consistent |
| Versions | All version fields equal; equal to the product release version when shipped together |
| Pins | Every submodule pin exists on its remote; working tree matches the pin |
| Bundled skills | Pass `skill-authoring.md`; edited in source repos, not in the plugin tree |
| Secrets / machine values | None in committed content; MCP only as sanitized examples |
| Lock & settings | Lock inventory matches installed records and enabled settings; regenerated after the last install/remove/toggle |
| Installed instance | The working agent’s installed copy matches the released version |

Quick check (before use): enabled state, version fields present, no broken pin, installed instance loadable.

## Must

- Read the current app’s plugin spec before authoring or checking a plugin.
- Ship content changes as a new version through the established release path, and refresh the working agent’s installed instance.
- Keep the sanitized lock in sync with installs, removals, and toggles.

## Must not

- Hand-edit a bundled submodule skill inside the plugin tree. *(← Must: bundled skills edited in source repos)*
- Commit install output, runtime state, or records with absolute paths. *(← Must: only the sanitized lock travels)*