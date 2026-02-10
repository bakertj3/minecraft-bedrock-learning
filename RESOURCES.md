# Useful Resources for Minecraft Bedrock Development

## Official Documentation

### Microsoft/Mojang Resources
- [Official Bedrock Documentation](https://learn.microsoft.com/en-us/minecraft/creator/)
- [Bedrock Samples Repository](https://github.com/Mojang/bedrock-samples)
- [Bedrock Wiki](https://wiki.bedrock.dev/) - Community-maintained documentation
- [Official Creator Portal](https://www.minecraft.net/en-us/creator)

### JSON Schemas
- [Manifest Schema](https://github.com/Mojang/bedrock-samples/blob/main/schemas/manifest_schema.json)
- [Sound Definitions Schema](https://github.com/Mojang/bedrock-samples/tree/main/schemas)

## Development Tools

### Editors and IDEs
- [Visual Studio Code](https://code.visualstudio.com/)
- [Blockception Extensions](https://marketplace.visualstudio.com/publishers/BlockceptionLtd) for VS Code
  - Minecraft Bedrock Development
  - JSON Schema validation
  - Autocomplete support

### Image Editing
- [GIMP](https://www.gimp.org/) - Free, open-source image editor
- [Photopea](https://www.photopea.com/) - Free online Photoshop alternative
- [Aseprite](https://www.aseprite.org/) - Pixel art editor (paid, but excellent for Minecraft textures)

### Sound Editing
- [Audacity](https://www.audacityteam.org/) - Free audio editor
- [Online Audio Converter](https://online-audio-converter.com/) - Convert to .ogg format

## Learning Resources

### Tutorials
- [Bedrock OSS](https://github.com/Bedrock-OSS) - Community tools and documentation
- [Microsoft Learn - Minecraft Education](https://learn.microsoft.com/en-us/minecraft/education/)
- [Minecraft Commands](https://www.digminecraft.com/game_commands/index.php)

### Video Tutorials
- Search YouTube for "Minecraft Bedrock addon tutorial"
- Look for channels focused on Bedrock edition specifically (not Java)

### Community
- [Minecraft Feedback](https://feedback.minecraft.net/) - Official feedback site
- [r/MinecraftCommands](https://www.reddit.com/r/MinecraftCommands/) - Reddit community
- [Bedrock Add-Ons Discord](https://discord.gg/bedrock) - Community Discord servers

## Technical References

### File Formats
- **Textures**: PNG format, typically 16x16 pixels or multiples (32x32, 64x64, etc.)
- **Sounds**: OGG Vorbis format (.ogg files)
- **Models**: JSON format following Bedrock model schema
- **Animations**: JSON format

### Common File Paths
- **Block Textures**: `textures/blocks/`
- **Item Textures**: `textures/items/`
- **Entity Textures**: `textures/entity/`
- **Sound Files**: `sounds/`
- **Models**: `models/entity/`

### UUID Generation
- Mac/Linux: `uuidgen` command in Terminal
- Windows PowerShell: `[guid]::NewGuid().ToString()`
- Online: [UUID Generator](https://www.uuidgenerator.net/)

## Version Compatibility

### Minimum Engine Version
- Current packs use: `[1, 20, 0]` (Minecraft 1.20.0)
- Check [version history](https://minecraft.fandom.com/wiki/Bedrock_Edition_version_history) for features

### Format Versions
- Manifest: `format_version: 2`
- Sound Definitions: `format_version: "1.20.20"`

## Tips and Tricks

### Testing
1. Always test on actual Minecraft Bedrock Edition
2. Check the Content Log in Settings > Creator
3. Enable "Content Log" in Settings for debugging
4. Test with fresh worlds to avoid cached data issues

### Common Pitfalls
- Filenames are case-sensitive on some platforms
- UUIDs must be unique across all packs
- Texture files must match exact vanilla names to override
- JSON must be valid (use a validator)

### Performance
- Keep texture resolution reasonable (16x16 or 32x32 typically)
- Compress .ogg files to reduce pack size
- Don't include unused files in packs

## Advanced Topics (Future Learning)

### Behavior Packs
- Entity behaviors
- Custom items
- Custom blocks
- Loot tables

### Scripting
- GameTest Framework
- Script API (JavaScript/TypeScript)
- Automation and custom logic

### World Templates
- Combining resource and behavior packs
- Creating distributable worlds
- Marketplace content guidelines

---

**Last Updated**: 2026-02-10
