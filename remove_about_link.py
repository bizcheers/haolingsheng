import os
import re
from pathlib import Path

def remove_about_link(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # The pattern for the About link in the header
        # Note: sometimes there are spaces or newlines before it
        about_pattern = r'\s*<li><a href="[^"]*about\.html"[^>]*>About</a></li>'
        
        new_content = re.sub(about_pattern, '', content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
            
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    base_dir = Path('/Users/bizcheers/jan-20-haolingsheng/haolingsheng')
    
    # Process both html and py files
    files = list(base_dir.rglob('*.html')) + list(base_dir.rglob('*.py'))
    
    updated_count = 0
    for filepath in files:
        if remove_about_link(filepath):
            updated_count += 1
            
    print(f"✅ Removed About link from {updated_count} files")

if __name__ == '__main__':
    main()
