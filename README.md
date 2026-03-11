# Minecraft Bedrock Learning Projects

Parent learning Bedrock add-on development to help facilitate child's creative ideas.

## Projects

### HelloWorldPack
First learning project focused on texture modification.
- **Type:** Resource Pack
- **Features:** Modified dirt block and golden apple textures
- **Concepts Learned:** Basic pack structure, texture overrides

### SillySoundsPack
Second learning project focused on sound customization.
- **Type:** Resource Pack
- **Features:** Custom sounds for grass/gravel blocks and cow mobs
- **Concepts Learned:** Sound definitions, audio file integration

## Quick Start

### Prerequisites
- Minecraft Bedrock Edition (Windows 10/11, Xbox, Mobile)
- VS Code with Blockception extensions (recommended)
- Git for version control

### Getting Started
1. Clone this repository
2. Review [QUICKSTART.md](QUICKSTART.md) for development workflow
3. Use [PACK_CREATION_CHECKLIST.md](PACK_CREATION_CHECKLIST.md) for new packs
4. Check [RESOURCES.md](RESOURCES.md) for helpful links

### Validating and Packaging
```bash
# Validate all packs
python3 scripts/validate.py

# Package for Minecraft
./scripts/package.sh HelloWorldPack
```

See [scripts/README.md](scripts/README.md) for more details.

## Development Setup
- **Platform:** Develop on Mac, test on Windows PC
- **Tools:** VS Code, Blockception extensions, GIMP
- **Version Control:** Git + GitHub

## Repository Structure
```
.
├── HelloWorldPack/          # Texture modification pack
├── SillySoundsPack/         # Sound customization pack
├── scripts/                 # Utility scripts
│   ├── validate.py         # Pack validation
│   └── package.sh          # Pack packaging
├── CODE_IMPROVEMENTS.md     # Code review and suggestions
├── UUID_REGISTRY.md         # Track pack UUIDs
├── RESOURCES.md             # Learning resources
└── .editorconfig            # Editor configuration

```

## Standard Pack Structure
Each pack follows the Bedrock standard:
- `manifest.json` - Pack metadata and UUIDs
- `pack_icon.png` - 256x256 icon shown in Minecraft
- `textures/` - Texture overrides (blocks, items, entities)
- `sounds/` - Sound files and definitions

## Documentation
- **[CODE_IMPROVEMENTS.md](CODE_IMPROVEMENTS.md)** - Comprehensive code review and improvement suggestions
- **[QUICKSTART.md](QUICKSTART.md)** - Development workflow reference
- **[PACK_CREATION_CHECKLIST.md](PACK_CREATION_CHECKLIST.md)** - New pack creation guide
- **[RESOURCES.md](RESOURCES.md)** - Curated learning resources
- **[UUID_REGISTRY.md](UUID_REGISTRY.md)** - UUID tracking

## Contributing
This is a personal learning project, but suggestions and improvements are welcome!

## License
MIT License - See [LICENSE](LICENSE) for details.

Minecraft and Minecraft Bedrock Edition are trademarks of Mojang AB and Microsoft Corporation.
Packs in this repository contain derivative works based on Minecraft assets for educational purposes.
