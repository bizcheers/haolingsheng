#!/usr/bin/env python3
"""
Update navigation across all HTML files:
1. Make logo clickable (wrap h1 in <a> tag)
2. Remove 'Home' link from navigation
"""

import os
import re
from pathlib import Path

# Base directory
base_dir = Path("/Users/bizcheers/jan-20/haolingsheng")

# All HTML files to update
html_files = [
    "index.html",
    "about.html",
    "contact.html",
    "privacy.html",
    "terms.html",
    "geci/index.html",
    "geci/major-scale-explained.html",
    "geci/chord-progressions-explained.html",
    "geci/what-is-interval.html",
    "gepu/index.html",
    "gepu/what-is-time-signature.html",
    "music-production/index.html",
    "music-production/suno-ai-prompts-guide.html",
    "music-production/what-is-daw.html",
    "music-production/eq-basics.html",
    "music-business/index.html",
    "music-business/distrokid-complete-guide.html",
    "music-business/youtube-music-verification.html",
    "music-business/how-to-make-money-from-music.html",
    "sheet-music/piano/beethoven-moonlight-sonata.html",
]

def get_home_url(file_path):
    """Calculate relative path to index.html based on file location"""
    depth = file_path.count('/')
    if depth == 0:
        return "index.html"
    elif depth == 1:
        return "../index.html"
    elif depth == 2:
        return "../../index.html"
    else:
        return "../" * depth + "index.html"

def update_html_file(file_path):
    """Update a single HTML file"""
    full_path = base_dir / file_path
    
    if not full_path.exists():
        print(f"⚠️  File not found: {file_path}")
        return False
    
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    home_url = get_home_url(file_path)
    
    # Pattern 1: Make logo clickable - wrap the logo-text div in an <a> tag
    # Find the logo section and wrap logo-text in <a>
    logo_pattern = r'(<div class="logo-text">)\s*(<h1>Hao Ling Sheng</h1>)\s*(<p class="tagline">Professional Music Education</p>)\s*(</div>)'
    logo_replacement = f'<a href="{home_url}" class="logo-text">\\n                    \\2\\n                    \\3\\n                </a>'
    
    content = re.sub(logo_pattern, logo_replacement, content)
    
    # Pattern 2: Remove Home link from navigation
    # Match the Home link in various formats
    home_link_patterns = [
        r'\s*<li><a href="[^"]*index\.html">Home</a></li>\s*\n',
        r'\s*<li><a href="[^"]*/">Home</a></li>\s*\n',
        r'\s*<li><a href="#">Home</a></li>\s*\n',
    ]
    
    for pattern in home_link_patterns:
        content = re.sub(pattern, '', content)
    
    # Write back if changed
    if content != original_content:
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated: {file_path}")
        return True
    else:
        print(f"⏭️  No changes: {file_path}")
        return False

def main():
    print("🔄 Updating navigation across all HTML files...\n")
    
    updated_count = 0
    for file_path in html_files:
        if update_html_file(file_path):
            updated_count += 1
    
    print(f"\n✨ Complete! Updated {updated_count}/{len(html_files)} files")

if __name__ == "__main__":
    main()
