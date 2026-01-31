# Bedrock Development Quick Reference

## Development Workflow (Mac → PC)

### On Mac (Development)

1. Make changes in VS Code
2. Test JSON syntax (extensions will show errors)
3. Commit changes to git
4. Push to GitHub

### On PC (Testing)

1. Pull from GitHub
2. Package as .mcpack: Right-click folder → "Send to" → "Compressed folder" → Rename to .mcpack
3. Double-click .mcpack to import into Bedrock
4. Test in Minecraft
5. Note bugs/changes

## Essential File Locations

### Mac Development

- Project root: `~/MinecraftBedrock/`
- Current project: `~/MinecraftBedrock/HelloWorldPack/`

### PC Testing (when you set it up)

- Bedrock data folder: `C:\Users\USERNAME\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\`
- Resource packs: `com.mojang/resource_packs/`
- Behavior packs: `com.mojang/behavior_packs/`

## Common Commands

### Git Workflow

```bash
# Commit changes
git add .
git commit -m "Description of changes"
git push

# Get changes from PC
git pull
```

### Package for Testing (Mac)

```bash
cd ~/MinecraftBedrock
zip -r HelloWorldPack.mcpack HelloWorldPack/
# Transfer .mcpack file to PC
```

## VS Code Shortcuts

- ⌘+P - Quick file open
- ⌘+Shift+P - Command palette
- ⌘+B - Toggle sidebar
- ⌘+` - Toggle terminal

## Bedrock Pack Basics

### Minimum Required Files

1. `manifest.json` - Pack metadata (UUID, version, description)
2. `pack_icon.png` - 256x256 PNG shown in Minecraft UI

### Resource Pack Structure

```tree
MyPack/
├── manifest.json
├── pack_icon.png
└── textures/
    ├── blocks/
    │   └── dirt.png (16x16 or multiple of 16)
    └── items/
        └── diamond.png
```

## Parking Lot (Future Learning)

- Behavior packs (Sprint 2)
- Custom entities (Sprint 5)
- Python automation (Sprint 4)
  