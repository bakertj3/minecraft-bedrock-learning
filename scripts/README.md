# Scripts

This directory contains utility scripts for Minecraft Bedrock pack development.

## Available Scripts

### validate.py
Validates pack structure and catches common errors before testing.

**Usage:**
```bash
python3 scripts/validate.py
```

**What it checks:**
- manifest.json is valid JSON
- Required manifest fields are present
- UUIDs are valid format
- UUIDs are unique within each pack
- pack_icon.png exists
- pack_icon.png is 256x256 (requires Pillow: `pip install Pillow`)
- sound_definitions.json is valid JSON (if present)

**Example output:**
```
Minecraft Bedrock Pack Validator
Repository: /path/to/minecraft-bedrock-learning

============================================================
Validating pack: HelloWorldPack
============================================================
✓ No issues found!

============================================================
Validating pack: SillySoundsPack
============================================================
ℹ️  1 Info:
  INFO: sounds.json found in root - this file is deprecated, use sounds/sound_definitions.json instead

============================================================
✓ All packs validated successfully!
```

### package.sh
Packages a pack directory as .mcpack file for easy transfer to PC.

**Usage:**
```bash
./scripts/package.sh HelloWorldPack
./scripts/package.sh SillySoundsPack
```

**What it does:**
- Creates a .mcpack (zip) file
- Excludes .DS_Store, .git, and temporary files
- Names output as PackName.mcpack
- Ready to transfer and import into Minecraft

**Example output:**
```
Packaging HelloWorldPack...
  adding: HelloWorldPack/manifest.json
  adding: HelloWorldPack/pack_icon.png
  adding: HelloWorldPack/textures/
  ...
✓ Package created: HelloWorldPack.mcpack
Transfer this file to your PC and double-click to import into Minecraft
```

## Recommended Workflow

1. Make changes to your pack
2. Run validation: `python3 scripts/validate.py`
3. Fix any errors
4. Package: `./scripts/package.sh YourPack`
5. Transfer .mcpack to PC
6. Import and test in Minecraft

## Requirements

- Python 3.6+ for validate.py
- `zip` command for package.sh (pre-installed on Mac/Linux)
- Optional: `pip install Pillow` for icon dimension validation

## Future Scripts

Consider adding:
- `create-pack.sh` - Create new pack from template
- `validate-textures.py` - Check texture dimensions
- `check-uuids.py` - Verify UUID uniqueness across all packs
- `generate-docs.py` - Auto-generate pack documentation
