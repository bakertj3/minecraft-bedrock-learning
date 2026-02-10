#!/bin/bash
# Package a Minecraft Bedrock pack as .mcpack file
# Usage: ./package.sh PackName

set -e

if [ -z "$1" ]; then
    echo "Usage: ./package.sh <PackName>"
    echo "Example: ./package.sh HelloWorldPack"
    exit 1
fi

PACK_NAME="$1"
PACK_DIR="$PACK_NAME"

# Check if pack directory exists
if [ ! -d "$PACK_DIR" ]; then
    echo "Error: Directory '$PACK_DIR' not found"
    exit 1
fi

# Check if manifest.json exists
if [ ! -f "$PACK_DIR/manifest.json" ]; then
    echo "Error: manifest.json not found in '$PACK_DIR'"
    exit 1
fi

# Create output filename
OUTPUT_FILE="${PACK_NAME}.mcpack"

echo "Packaging $PACK_NAME..."

# Remove old package if it exists
if [ -f "$OUTPUT_FILE" ]; then
    echo "Removing old package..."
    rm "$OUTPUT_FILE"
fi

# Create .mcpack (zip file with .mcpack extension)
# Exclude .DS_Store, .git, and other unwanted files
zip -r "$OUTPUT_FILE" "$PACK_DIR/" \
    -x "*.DS_Store" \
    -x "*/.git/*" \
    -x "*/.*" \
    -x "*~" \
    -x "*.tmp"

echo "✓ Package created: $OUTPUT_FILE"
echo "Transfer this file to your PC and double-click to import into Minecraft"
