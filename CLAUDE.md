# CLAUDE.md — AI Assistant Guide for minecraft-bedrock-learning

This file provides context and conventions for AI assistants working in this repository.

## Project Overview

This is a **Minecraft Bedrock Edition resource pack learning project**. The goal is for a parent to learn Bedrock add-on development in order to help facilitate a child's creative ideas in Minecraft.

There is no traditional source code, build system, or test suite. The project consists entirely of:
- JSON configuration files (manifests, sound definitions)
- PNG texture assets
- OGG audio assets

**Development platform:** Mac (authoring) → Windows PC (testing in Minecraft)

---

## Repository Structure

```
minecraft-bedrock-learning/
├── CLAUDE.md                       ← This file
├── README.md                       ← Project overview
├── QUICKSTART.md                   ← Mac/PC workflow and Git reference
├── PACK_CREATION_CHECKLIST.md      ← Step-by-step guide for new packs
├── .gitignore                      ← Excludes .DS_Store, .mcpack, .mcaddon, etc.
├── HelloWorldPack/                 ← Pack 1: texture modifications
│   ├── manifest.json
│   ├── pack_icon.png
│   └── textures/
│       ├── blocks/
│       │   └── dirt.png            ← Custom cyan-speckled dirt (16x16)
│       └── items/
│           └── apple_golden.png    ← Custom golden apple texture (16x16)
└── SillySoundsPack/                ← Pack 2: sound modifications
    ├── manifest.json
    ├── pack_icon.png
    ├── sounds.json                 ← Maps block sound events to categories
    └── sounds/
        ├── sound_definitions.json  ← Maps sound event names to audio files
        ├── dig/
        │   └── funny_pop.ogg       ← Custom dig sound (replaces grass/gravel break)
        └── mob/
            └── cow/
                └── cow_farts.ogg   ← Custom cow sound (added to cow ambient pool)
```

---

## Current Packs

### HelloWorldPack
- **Type:** Resource pack (texture modification)
- **Status:** Complete
- **What it does:** Replaces the vanilla dirt block texture and golden apple item texture with custom versions.
- **Version:** `[1, 1, 0]`

### SillySoundsPack
- **Type:** Resource pack (sound modification)
- **Status:** Active / evolving
- **What it does:**
  - Replaces the dirt/grass block break sound with a "funny pop"
  - Replaces the gravel block break sound with a "funny pop"
  - Adds a cow fart sound to the cow ambient sound pool (alongside vanilla cow sounds)
- **Version:** `[1, 0, 0]`

---

## File Format Conventions

### manifest.json

Every pack requires a `manifest.json` in its root folder. Use `format_version: 2`.

```json
{
  "format_version": 2,
  "header": {
    "name": "Pack Name",
    "description": "Short description",
    "uuid": "<UUID-v4>",
    "version": [1, 0, 0],
    "min_engine_version": [1, 20, 0]
  },
  "modules": [
    {
      "type": "resources",
      "uuid": "<different-UUID-v4>",
      "version": [1, 0, 0]
    }
  ]
}
```

**Rules:**
- The header UUID and module UUID must be different and unique across all packs.
- Generate new UUIDs with `uuidgen` in Terminal.
- `min_engine_version` is always `[1, 20, 0]`.
- `type` is always `"resources"` for resource packs (behavior packs use `"data"`).
- Bump the version array (e.g. `[1, 0, 0]` → `[1, 1, 0]`) when making significant changes.

### sounds.json (block sound mapping)

Located at the pack root. Maps vanilla block sound categories to custom sound events.

```json
{
    "block_sounds": {
        "<block_category>": {
            "events": {
                "<event_name>": {
                    "pitch": [0.80, 1.0],
                    "sound": "<sound_event_id>",
                    "volume": 0.70
                }
            }
        }
    }
}
```

- `<block_category>` matches vanilla categories (e.g. `"grass"`, `"stone"`, `"wood"`).
- `<event_name>` is typically `"break"`, `"place"`, `"hit"`, or `"step"`.
- `<sound_event_id>` references an entry in `sound_definitions.json`.

### sounds/sound_definitions.json

Defines sound events and maps them to audio files. Bedrock's format_version for this file is `"1.20.20"` (a string, not a number).

```json
{
    "format_version": "1.20.20",
    "sound_definitions": {
        "<sound_event_id>": {
            "__use_legacy_max_distance": "true",
            "category": "block",
            "sounds": [
                "sounds/dig/filename_without_extension"
            ]
        }
    }
}
```

**Rules:**
- `format_version` is a string (`"1.20.20"`), unlike `manifest.json` where it is a number.
- File paths in `"sounds"` array are relative to the pack root, without the `.ogg` extension.
- `category` is typically `"block"` for block sounds or `"neutral"` for mob sounds.
- `"__use_legacy_max_distance": "true"` should be included for compatibility.
- To add a sound to an existing vanilla pool (rather than replacing it), list the vanilla sound IDs alongside the custom one in `"sounds"`.

---

## Naming Conventions

| Item | Convention | Example |
|---|---|---|
| Pack folder | PascalCase | `HelloWorldPack` |
| JSON config files | snake_case | `manifest.json`, `sounds.json`, `sound_definitions.json` |
| Texture files | snake_case, match vanilla exactly | `dirt.png`, `apple_golden.png` |
| Sound files | snake_case, descriptive | `funny_pop.ogg`, `cow_farts.ogg` |
| Subdirectories | lowercase | `textures/`, `blocks/`, `sounds/`, `dig/`, `mob/` |

---

## Development Workflow

### Creating a new pack

1. Create a new folder in the repo root using PascalCase (e.g. `MyNewPack/`).
2. Generate 2 unique UUIDs: `uuidgen && uuidgen` in Terminal.
3. Create `manifest.json` using the template above.
4. Create a `pack_icon.png` (256×256 PNG) in the pack root.
5. Add content (textures, sounds, behaviors, etc.).
6. See `PACK_CREATION_CHECKLIST.md` for the full checklist.

### Modifying textures

- Match vanilla file paths and filenames exactly (e.g. `textures/blocks/dirt.png`).
- Keep textures at 16×16 pixels (or exact multiples: 32×32, 64×64).
- Reference vanilla textures from the `bedrock-samples` repo at `~/Downloads/bedrock-samples/resource_pack/textures/`.

### Modifying sounds

- Audio files must be `.ogg` format, placed under `sounds/` in the pack.
- Add a `sound_definitions.json` inside the `sounds/` folder.
- Optionally add a `sounds.json` in the pack root for block sound event mapping.

### Packaging for testing

```bash
cd ~/MinecraftBedrock
zip -r PackName.mcpack PackFolderName/
```

Then transfer the `.mcpack` file to the Windows PC and double-click to import into Bedrock.

**Note:** `.mcpack` files are excluded from Git via `.gitignore`. Never commit them.

### Git workflow

```bash
git add .
git commit -m "Short description of changes"
git push
```

Commit messages use plain imperative style (e.g. `add SillySoundsPack icon`, `fix sound_definitions.json`).

---

## Troubleshooting Reference

| Problem | Likely cause | Fix |
|---|---|---|
| Pack not showing in Minecraft | JSON syntax error in `manifest.json` | Validate JSON; check for trailing commas, missing brackets |
| Texture not changing | Filename doesn't exactly match vanilla | Compare against bedrock-samples reference |
| Sound not playing | Wrong path in `sound_definitions.json` or missing `.ogg` | Check path is relative to pack root, no extension in path string |
| Import fails | `.mcpack` is malformed or wrong folder structure | Re-zip; ensure pack folder is at root of zip, not nested |
| Block sound not replaced | Wrong block category name in `sounds.json` | Reference vanilla `sounds.json` from bedrock-samples |

---

## AI Assistant Guidelines

- **No build step.** There is nothing to compile, run, or test automatically.
- **Validate JSON by inspection.** No linter or schema validator is configured; check for syntax issues manually.
- **UUID uniqueness is critical.** Never reuse a UUID from an existing pack. Generate fresh ones.
- **Respect vanilla filenames.** Texture and sound overrides only work if the filename matches the vanilla asset exactly.
- **Minimal changes.** This is a learning project. Prefer small, focused edits that are easy to understand.
- **Document changes.** When modifying JSON, keep the structure readable; avoid minifying.
- **`.mcpack` files are build artifacts.** Never create or commit them.
- **This is Bedrock, not Java.** Bedrock and Java Edition have entirely different modding systems; do not apply Java Edition conventions here.
- **Check existing packs for patterns.** Before adding a new sound or texture, look at `SillySoundsPack` and `HelloWorldPack` for reference implementations.
