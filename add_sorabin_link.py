#!/usr/bin/env python3
"""
Script to add SoraBin link to all HTML files in the project
"""
import os
import re
from pathlib import Path

def update_footer_in_file(filepath):
    """Update the footer Connect section in a single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False
    
    # Check if already has the link
    if 'sorabin.com' in content:
        # print(f"✓ {filepath.name} already has SoraBin link")
        return False

    # Pattern to match the Connect section footer
    # We look for the <h4>Connect</h4> and then the following <ul>...</ul>
    pattern = r'(<h4>Connect</h4>\s*<ul>)(.*?)(</ul>)'
    
    # SoraBin link to add
    new_link = '                        <li><a href="https://sorabin.com/" rel="dofollow noopener" target="_blank">SoraBin</a></li>'
    
    def add_link(match):
        header_ul = match.group(1)
        items = match.group(2)
        end_ul = match.group(3)
        
        # Check if the list already has some items to maintain indentation
        if items.strip():
            # Append to the end of the list
            if items.endswith('\n'):
                return f"{header_ul}{items}{new_link}\n{end_ul}"
            else:
                return f"{header_ul}{items}\n{new_link}\n{end_ul}"
        else:
            return f"{header_ul}\n{new_link}\n{end_ul}"

    # Search for the pattern
    if not re.search(pattern, content, re.DOTALL):
        # Fallback to a simpler search if the specific pattern above fails
        # print(f"⚠ {filepath.name} - pattern not found")
        return False
    
    # Replace
    new_content = re.sub(pattern, add_link, content, flags=re.DOTALL)
    
    # Write back
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ Updated {filepath}")
        return True
    except Exception as e:
        print(f"Error writing to {filepath}: {e}")
        return False

def main():
    # Find all HTML files in the project
    base_dir = Path('/Users/bizcheers/jan-20-haolingsheng/haolingsheng')
    
    html_files = []
    # Walk through all directories
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                html_files.append(Path(root) / file)
    
    updated_count = 0
    for filepath in html_files:
        if update_footer_in_file(filepath):
            updated_count += 1
    
    print(f"\n✅ Updated {updated_count} files")

if __name__ == '__main__':
    main()
