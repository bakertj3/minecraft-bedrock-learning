# Resource Pack Creation Checklist

## Every New Pack Needs

### 1. manifest.json

- [ ] Generate 2 new UUIDs (`uuidgen` in Terminal)
- [ ] Set pack name and description
- [ ] Set version [1, 0, 0]
- [ ] Set min_engine_version [1, 20, 0]
- [ ] Header UUID (first one)
- [ ] Module UUID (second one)
- [ ] Module type: "resources"

### 2. pack_icon.png

- [ ] 256x256 pixels
- [ ] PNG format
- [ ] Saved in pack root folder

### 3. Textures (if modifying)

- [ ] Create folder structure: `textures/blocks/` or `textures/items/`
- [ ] Get vanilla texture from bedrock-samples repo
- [ ] Modify in Photopea (keep 16x16 dimensions!)
- [ ] Save with exact vanilla filename (e.g., `dirt.png`)

### 4. Packaging

```bash
cd ~/MinecraftBedrock
zip -r PackName.mcpack PackFolderName/
```

### 5. Git Workflow

```bash
git add .
git commit -m "Description of changes"
git push
```

### 6. Transfer to PC

- Email .mcpack file, OR
- Push to GitHub and pull on PC, OR
- Use cloud storage

### 7. Testing on PC

- Double-click .mcpack → Import
- Settings → Global Resources → Activate
- Create/load world
- Verify changes

## Common Texture Paths

- Blocks: `textures/blocks/filename.png`
- Items: `textures/items/filename.png`
- All textures: 16x16 pixels (or multiples: 32x32, 64x64)

## Vanilla Texture Reference

Location: `~/Downloads/bedrock-samples/resource_pack/textures/`

## Troubleshooting

- Pack not showing? Check manifest.json syntax
- Texture not changing? Verify exact filename matches vanilla
- Import fails? Check .mcpack is valid zip with correct structure
