#!/usr/bin/env python3
import os
import re
from datetime import datetime
from pathlib import Path

# Configuration
CONTENT_DIRS = ['geci', 'gepu', 'music-production', 'music-business']
INDEX_FILE = 'index.html'
MAX_ARTICLES = 6

def extract_meta(filepath):
    """Extracts title, category, and read time from an article HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract Title from article header (using lookbehind for category-tag to be more certain)
    # The structure is: <span class="category-tag">...</span>\n                <h1>...</h1>
    title_match = re.search(r'class="category-tag">.*?</span>\s*<h1>(.*?)</h1>', content, re.DOTALL)
    if not title_match:
        # Fallback to the last h1 in the file which is usually the article title in this template
        h1s = re.findall(r'<h1>(.*?)</h1>', content)
        title = h1s[-1].strip() if h1s else filepath.name
    else:
        title = title_match.group(1).strip()
    
    # Extract Category from <span class="category-tag">
    cat_match = re.search(r'<span class="category-tag">(.*?)</span>', content)
    category = cat_match.group(1).strip() if cat_match else "General"
    
    # Extract Read Time from <span class="read-time">
    time_match = re.search(r'<span class="read-time">(.*?)</span>', content)
    read_time = time_match.group(1).strip() if time_match else "5 min read"

    # Determine Icon based on category or directory
    icon = "🎵"
    if "Theory" in category: icon = "🎼"
    if "Scales" in category: icon = "⭕"
    if "Harmony" in category: icon = "🎹"
    if "Rhythm" in category: icon = "🥁"
    if "Business" in category: icon = "💰"
    if "Melody" in category: icon = "✍️"
    if "Composition" in category: icon = "🖋️"
    if "Science" in category: icon = "⚛️"

    # The filepath is already relative to the root if we use glob on CONTENT_DIRS
    link = filepath.as_posix()
    
    return {
        'title': title,
        'category': category,
        'read_time': read_time,
        'icon': icon,
        'link': link,
        'mtime': os.path.getmtime(filepath)
    }

def generate_section_html(articles):
    """Generates the HTML for the Recent Articles section."""
    html = ['            <div class="sheet-music-list">']
    for art in articles:
        html.append(f"""                <div class="sheet-item">
                    <div class="sheet-thumb">{art['icon']}</div>
                    <div class="sheet-info">
                        <h4><a href="{art['link']}">{art['title']}</a></h4>
                        <p>{art['category']} • {art['read_time']}</p>
                    </div>
                </div>""")
    html.append('            </div>')
    return "\n".join(html)

def update_index():
    """Scans for articles and updates index.html."""
    all_articles = []
    
    for d in CONTENT_DIRS:
        path = Path(d)
        if not path.exists(): continue
        
        for f in path.glob('*.html'):
            if f.name == 'index.html': continue
            try:
                all_articles.append(extract_meta(f))
            except Exception as e:
                print(f"Skipping {f}: {e}")

    # Sort by modification time descending
    all_articles.sort(key=lambda x: x['mtime'], reverse=True)
    recent = all_articles[:MAX_ARTICLES]
    
    new_html = generate_section_html(recent)
    
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace using markers
    pattern = re.compile(r'<!-- RECENT_ARTICLES_START -->.*?<!-- RECENT_ARTICLES_END -->', re.DOTALL)
    replacement = f'<!-- RECENT_ARTICLES_START -->\n{new_html}\n            <!-- RECENT_ARTICLES_END -->'
    
    if not pattern.search(content):
        print("Error: Could not find Recent Articles markers in index.html")
        return

    updated_content = pattern.sub(replacement, content)
    
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"Successfully updated index.html with {len(recent)} articles.")

if __name__ == "__main__":
    update_index()
