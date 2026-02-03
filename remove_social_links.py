#!/usr/bin/env python3
"""
Script to remove social media links from footer, keeping only Time Zone Converter
"""
import os
import re
from pathlib import Path

def update_footer_in_file(filepath):
    """Remove social media links from footer Connect section"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match the Connect section with all links
    pattern = r'(<div class="footer-section">\s*<h4>Connect</h4>\s*<ul>\s*<li><a href="#"[^>]*>Facebook</a></li>\s*<li><a href="#"[^>]*>Twitter</a></li>\s*<li><a href="#"[^>]*>Instagram</a></li>\s*<li><a href="#"[^>]*>YouTube</a></li>\s*<li><a href="https://timeuo\.com/"[^>]*>Time Zone Converter</a></li>\s*</ul>)'
    
    # Replacement with only Time Zone Converter
    replacement = r'''<div class="footer-section">
                    <h4>Connect</h4>
                    <ul>
                        <li><a href="https://timeuo.com/" rel="dofollow noopener" target="_blank">Time Zone Converter</a></li>
                    </ul>'''
    
    # Check if pattern matches
    if not re.search(pattern, content, re.DOTALL):
        print(f"⚠ {filepath.name} - pattern not found")
        return False
    
    # Replace
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ Updated {filepath.name}")
    return True

def main():
    # Find all HTML files in the project
    base_dir = Path('/Users/bizcheers/jan-20-haolingsheng/haolingsheng')
    
    html_files = []
    for directory in ['gepu', 'geci', 'music-production', 'music-business']:
        dir_path = base_dir / directory
        if dir_path.exists():
            html_files.extend(dir_path.glob('*.html'))
    
    # Also check root HTML files
    html_files.extend(base_dir.glob('*.html'))
    
    updated_count = 0
    for filepath in html_files:
        if update_footer_in_file(filepath):
            updated_count += 1
    
    print(f"\n✅ Updated {updated_count} files")

if __name__ == '__main__':
    main()
