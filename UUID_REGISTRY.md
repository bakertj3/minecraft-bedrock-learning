# UUID Registry

This file tracks all UUIDs used across packs to prevent conflicts.

> **Important**: Each pack must have unique UUIDs. Never reuse UUIDs across different packs.

## HelloWorldPack
- **Header UUID**: `a8fc50c7-b568-4871-b0d4-62bbf4ef1244`
- **Module UUID**: `051c1846-37c8-4b91-8120-f542eabe45b2`
- **Version**: 1.1.0
- **Created**: Initial learning project
- **Purpose**: Texture modification learning (dirt block, golden apple)

## SillySoundsPack
- **Header UUID**: `6caca1e1-5af6-4879-82c5-cfb7735f6905`
- **Module UUID**: `7f4319ab-5d0d-4dbf-b087-1d4e382628fd`
- **Version**: 1.0.0
- **Created**: Second learning project
- **Purpose**: Sound customization learning (grass, gravel, cow sounds)

## How to Generate New UUIDs

### On Mac/Linux:
```bash
uuidgen
```

### On Windows (PowerShell):
```powershell
[guid]::NewGuid().ToString()
```

### Online:
- https://www.uuidgenerator.net/

## UUID Format
UUIDs follow the format: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
- Must be lowercase for Minecraft Bedrock
- Must be unique for each pack and module
