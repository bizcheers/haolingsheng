#!/usr/bin/env python3
"""
Batch add Schema.org Article markup to HTML files missing it.
Extracts title and meta description from each file and generates proper JSON-LD.
"""

import os
import re
from pathlib import Path
from datetime import datetime

# Base URL
BASE_URL = "https://www.haolingsheng.com"

# Schema template
SCHEMA_TEMPLATE = '''
    <!-- Schema.org Structured Data -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{headline}",
      "description": "{description}",
      "author": {{
        "@type": "Organization",
        "name": "Hao Ling Sheng"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Hao Ling Sheng",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://www.haolingsheng.com/logo.svg"
        }}
      }},
      "datePublished": "{date_published}",
      "dateModified": "{date_modified}",
      "mainEntityOfPage": {{
        "@type": "WebPage",
        "@id": "{url}"
      }}
    }}
    </script>
'''

def extract_metadata(html_content):
    """Extract title and meta description from HTML."""
    title_match = re.search(r'<title>(.*?)</title>', html_content, re.DOTALL)
    desc_match = re.search(r'<meta name="description"\s+content="([^"]*)"', html_content, re.IGNORECASE)
    
    title = title_match.group(1).strip() if title_match else ""
    # Remove " | Hao Ling Sheng" from title for headline
    headline = re.sub(r'\s*\|\s*Hao Ling Sheng\s*$', '', title)
    description = desc_match.group(1).strip() if desc_match else ""
    
    return headline, description

def has_schema(html_content):
    """Check if file already has Schema.org markup."""
    return 'schema.org' in html_content

def get_file_url(file_path, base_dir):
    """Convert file path to website URL."""
    rel_path = os.path.relpath(file_path, base_dir)
    url = f"{BASE_URL}/{rel_path}"
    return url

def add_schema_to_file(file_path, base_dir, dry_run=False):
    """Add Schema markup to a single HTML file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already has schema
    if has_schema(content):
        return False, "Already has schema"
    
    # Extract metadata
    headline, description = extract_metadata(content)
    
    if not headline or not description:
        return False, f"Missing metadata (headline={bool(headline)}, desc={bool(description)})"
    
    # Generate URL
    url = get_file_url(file_path, base_dir)
    
    # Get dates (use current date for both)
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Generate schema
    schema = SCHEMA_TEMPLATE.format(
        headline=headline.replace('"', '\\"'),
        description=description.replace('"', '\\"'),
        date_published=today,
        date_modified=today,
        url=url
    )
    
    # Find insertion point (before </head>)
    head_close_match = re.search(r'(\s*)</head>', content)
    if not head_close_match:
        return False, "No </head> tag found"
    
    # Insert schema before </head>
    new_content = content[:head_close_match.start()] + schema + content[head_close_match.start():]
    
    if not dry_run:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
    
    return True, "Schema added successfully"

def process_directory(directory, dry_run=False):
    """Process all HTML files in directory."""
    base_dir = os.path.dirname(os.path.abspath(directory))
    results = {
        'success': [],
        'skipped': [],
        'failed': []
    }
    
    # Find all HTML files (exclude index and page-* files)
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html') and file not in ['index.html'] and not file.startswith('page-'):
                html_files.append(os.path.join(root, file))
    
    print(f"\nFound {len(html_files)} HTML files to process in {directory}")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}\n")
    
    for file_path in sorted(html_files):
        rel_path = os.path.relpath(file_path, base_dir)
        success, message = add_schema_to_file(file_path, base_dir, dry_run)
        
        if success:
            results['success'].append(rel_path)
            print(f"✓ {rel_path}")
        elif "Already has schema" in message:
            results['skipped'].append(rel_path)
            print(f"⊘ {rel_path} - {message}")
        else:
            results['failed'].append((rel_path, message))
            print(f"✗ {rel_path} - {message}")
    
    return results

def main():
    import sys
    
    # Get base directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Directories to process
    directories = [
        os.path.join(base_dir, 'music-production'),
        os.path.join(base_dir, 'music-business'),
        os.path.join(base_dir, 'geci')
    ]
    
    # Check if dry run
    dry_run = '--dry-run' in sys.argv
    
    all_results = {
        'success': [],
        'skipped': [],
        'failed': []
    }
    
    for directory in directories:
        if os.path.exists(directory):
            results = process_directory(directory, dry_run)
            all_results['success'].extend(results['success'])
            all_results['skipped'].extend(results['skipped'])
            all_results['failed'].extend(results['failed'])
    
    # Print summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"✓ Successfully processed: {len(all_results['success'])}")
    print(f"⊘ Skipped (already has schema): {len(all_results['skipped'])}")
    print(f"✗ Failed: {len(all_results['failed'])}")
    
    if all_results['failed']:
        print("\nFailed files:")
        for file, reason in all_results['failed']:
            print(f"  - {file}: {reason}")
    
    if dry_run:
        print("\n⚠️  This was a DRY RUN. No files were modified.")
        print("Run without --dry-run to apply changes.")

if __name__ == '__main__':
    main()
