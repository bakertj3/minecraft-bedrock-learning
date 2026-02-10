#!/usr/bin/env python3
"""
Minecraft Bedrock Pack Validator

This script validates Bedrock resource/behavior packs to catch common issues
before packaging and testing in Minecraft.
"""

import json
import os
import sys
from pathlib import Path
from uuid import UUID

def validate_json_file(file_path):
    """Validate that a file contains valid JSON."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        return True, None
    except json.JSONDecodeError as e:
        return False, f"JSON syntax error: {e}"
    except Exception as e:
        return False, f"Error reading file: {e}"

def validate_uuid(uuid_string):
    """Validate UUID format."""
    try:
        UUID(uuid_string)
        return True
    except (ValueError, AttributeError):
        return False

def validate_manifest(manifest_path):
    """Validate manifest.json structure and content."""
    issues = []
    
    # Check if manifest exists
    if not manifest_path.exists():
        return [f"ERROR: manifest.json not found at {manifest_path}"]
    
    # Validate JSON syntax
    is_valid, error = validate_json_file(manifest_path)
    if not is_valid:
        return [f"ERROR: Invalid JSON in manifest.json - {error}"]
    
    # Load and validate content
    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)
    
    # Check required fields
    if 'format_version' not in manifest:
        issues.append("WARNING: Missing format_version")
    
    if 'header' not in manifest:
        issues.append("ERROR: Missing header section")
        return issues
    
    header = manifest['header']
    
    # Validate header fields
    required_header_fields = ['name', 'description', 'uuid', 'version', 'min_engine_version']
    for field in required_header_fields:
        if field not in header:
            issues.append(f"ERROR: Missing required header field: {field}")
    
    # Validate UUIDs
    if 'uuid' in header:
        if not validate_uuid(header['uuid']):
            issues.append(f"ERROR: Invalid header UUID: {header['uuid']}")
    
    # Validate modules
    if 'modules' not in manifest:
        issues.append("ERROR: Missing modules section")
    else:
        for i, module in enumerate(manifest['modules']):
            if 'uuid' not in module:
                issues.append(f"ERROR: Module {i} missing UUID")
            elif not validate_uuid(module['uuid']):
                issues.append(f"ERROR: Invalid UUID in module {i}: {module['uuid']}")
            
            if 'type' not in module:
                issues.append(f"ERROR: Module {i} missing type")
            
            if 'version' not in module:
                issues.append(f"ERROR: Module {i} missing version")
    
    # Check for UUID uniqueness
    uuids = []
    if 'uuid' in header:
        uuids.append(header['uuid'])
    if 'modules' in manifest:
        for module in manifest['modules']:
            if 'uuid' in module:
                uuids.append(module['uuid'])
    
    if len(uuids) != len(set(uuids)):
        issues.append("ERROR: Duplicate UUIDs found in manifest")
    
    return issues

def validate_pack_icon(pack_path):
    """Validate pack_icon.png exists and has correct dimensions."""
    issues = []
    icon_path = pack_path / 'pack_icon.png'
    
    if not icon_path.exists():
        issues.append("WARNING: pack_icon.png not found")
        return issues
    
    # Try to check dimensions (requires PIL/Pillow)
    try:
        from PIL import Image
        img = Image.open(icon_path)
        if img.size != (256, 256):
            issues.append(f"WARNING: pack_icon.png should be 256x256, found {img.size[0]}x{img.size[1]}")
    except ImportError:
        issues.append("INFO: Install Pillow (pip install Pillow) to validate icon dimensions")
    except Exception as e:
        issues.append(f"WARNING: Could not validate icon dimensions: {e}")
    
    return issues

def validate_pack(pack_path):
    """Validate an entire pack directory."""
    print(f"\n{'='*60}")
    print(f"Validating pack: {pack_path.name}")
    print('='*60)
    
    all_issues = []
    
    # Validate manifest
    manifest_path = pack_path / 'manifest.json'
    manifest_issues = validate_manifest(manifest_path)
    all_issues.extend(manifest_issues)
    
    # Validate pack icon
    icon_issues = validate_pack_icon(pack_path)
    all_issues.extend(icon_issues)
    
    # Validate sound_definitions.json if present
    sound_defs_path = pack_path / 'sounds' / 'sound_definitions.json'
    if sound_defs_path.exists():
        is_valid, error = validate_json_file(sound_defs_path)
        if not is_valid:
            all_issues.append(f"ERROR: Invalid JSON in sound_definitions.json - {error}")
    
    # Validate sounds.json if present (check for deprecation)
    sounds_json_path = pack_path / 'sounds.json'
    if sounds_json_path.exists():
        all_issues.append("INFO: sounds.json found in root - this file is deprecated, use sounds/sound_definitions.json instead")
        is_valid, error = validate_json_file(sounds_json_path)
        if not is_valid:
            all_issues.append(f"ERROR: Invalid JSON in sounds.json - {error}")
    
    # Print results
    if not all_issues:
        print("✓ No issues found!")
        return True
    else:
        errors = [i for i in all_issues if i.startswith('ERROR')]
        warnings = [i for i in all_issues if i.startswith('WARNING')]
        infos = [i for i in all_issues if i.startswith('INFO')]
        
        if errors:
            print(f"\n❌ {len(errors)} Error(s):")
            for issue in errors:
                print(f"  {issue}")
        
        if warnings:
            print(f"\n⚠️  {len(warnings)} Warning(s):")
            for issue in warnings:
                print(f"  {issue}")
        
        if infos:
            print(f"\nℹ️  {len(infos)} Info:")
            for issue in infos:
                print(f"  {issue}")
        
        return len(errors) == 0

def main():
    """Main validation function."""
    # Get repository root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    print(f"Minecraft Bedrock Pack Validator")
    print(f"Repository: {repo_root}")
    
    # Find all pack directories (contain manifest.json)
    packs = []
    for item in repo_root.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            if (item / 'manifest.json').exists():
                packs.append(item)
    
    if not packs:
        print("\nNo packs found (directories with manifest.json)")
        return 0
    
    # Validate each pack
    all_passed = True
    for pack_path in sorted(packs):
        passed = validate_pack(pack_path)
        if not passed:
            all_passed = False
    
    # Summary
    print(f"\n{'='*60}")
    if all_passed:
        print("✓ All packs validated successfully!")
        return 0
    else:
        print("❌ Some packs have errors - please fix before packaging")
        return 1

if __name__ == '__main__':
    sys.exit(main())
