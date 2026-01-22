#!/usr/bin/env python3
import os
from pathlib import Path
from datetime import datetime

# Configuration
BASE_URL = "https://www.haolingsheng.com/"
CONTENT_DIRS = ['geci', 'gepu', 'music-production', 'music-business']
ROOT_FILES = ['index.html', 'about.html', 'contact.html', 'privacy.html', 'terms.html']
EXCLUDE_FILES = ['debug_layout.html', 'google', '404.html']

def get_priority(path):
    """Determines priority based on file type."""
    if path.name == 'index.html':
        # Root homepage
        if path.parent.resolve() == Path('.').resolve(): 
            return "1.0"
        # Category indexes
        return "0.8"
    # Standard articles
    return "0.6"

def generate():
    """Scans directories and generates sitemap.xml."""
    urls = []
    
    # scan current directory for root files
    for f in ROOT_FILES:
        p = Path(f)
        if p.exists():
            mod_time = datetime.fromtimestamp(p.stat().st_mtime).strftime('%Y-%m-%d')
            # For root index.html, we usually want the bare domain, but sitemap requires full URL
            # We will use index.html in the path for consistency, or standard convention
            loc = f 
            priority = "1.0" if f == 'index.html' else "0.5"
            urls.append({'loc': loc, 'lastmod': mod_time, 'priority': priority})

    # scan content directories
    for d in CONTENT_DIRS:
        path = Path(d)
        if not path.exists(): continue
        
        for p in path.rglob('*.html'):
            if any(ex in p.name for ex in EXCLUDE_FILES):
                continue
            
            rel_path = p.as_posix()
            mod_time = datetime.fromtimestamp(p.stat().st_mtime).strftime('%Y-%m-%d')
            priority = get_priority(p)
            
            urls.append({'loc': rel_path, 'lastmod': mod_time, 'priority': priority})
            
    # XML Construction
    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    count = 0
    for item in urls:
        xml.append('  <url>')
        xml.append(f'    <loc>{BASE_URL}{item["loc"]}</loc>')
        xml.append(f'    <lastmod>{item["lastmod"]}</lastmod>')
        xml.append(f'    <changefreq>weekly</changefreq>')
        xml.append(f'    <priority>{item["priority"]}</priority>')
        xml.append('  </url>')
        count += 1
    
    xml.append('</urlset>')
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml))
        
    print(f"✅ Automatically updated sitemap.xml with {count} URLs.")

if __name__ == "__main__":
    generate()
