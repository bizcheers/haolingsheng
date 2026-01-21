#!/usr/bin/env python3
"""
HTML Page Generator for Hao Ling Sheng Music Education Website
Generates static HTML pages from CSV data files
"""

import csv
import os
from pathlib import Path
from typing import Dict, List

# Template for sheet music detail pages
SHEET_MUSIC_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{meta_description}">
    <meta name="keywords" content="{keywords}">
    <title>{title} | Free Sheet Music - Hao Ling Sheng</title>
    <link rel="stylesheet" href="../../styles.css">
    <link rel="stylesheet" href="../sheet-detail.css">
</head>
<body>
    <header>
        <div class="container">
            <div class="logo">
                <h1>🎵 Hao Ling Sheng</h1>
                <p class="tagline">Your Free Music Education Resource</p>
            </div>
            <nav>
                <ul>
                    <li><a href="../../index.html">Home</a></li>
                    <li><a href="../index.html">Sheet Music</a></li>
                    <li><a href="../../music-theory/index.html">Music Theory</a></li>
                    <li><a href="../../instruments/index.html">Instruments</a></li>
                    <li><a href="../../about.html">About</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main>
        <div class="breadcrumb">
            <div class="container">
                <a href="../../index.html">Home</a> / 
                <a href="../index.html">Sheet Music</a> / 
                <a href="index.html">{instrument}</a> / 
                <span>{piece_name}</span>
            </div>
        </div>

        <article class="sheet-detail">
            <div class="container">
                <div class="content-wrapper">
                    <div class="main-content">
                        <h1>{full_title}</h1>
                        
                        <div class="composer-info">
                            <p><strong>Composer:</strong> {composer}</p>
                            {composer_years}
                            {opus_info}
                        </div>

                        <div class="sheet-meta">
                            <span class="badge">🎹 {instrument}</span>
                            <span class="badge">🎼 {genre}</span>
                            <span class="badge">📊 {difficulty}</span>
                            <span class="badge">⏱️ {duration}</span>
                        </div>

                        <div class="sheet-preview">
                            <div class="preview-placeholder">
                                <p>🎼 Sheet Music Preview</p>
                                <p class="preview-note">{preview_note}</p>
                            </div>
                        </div>

                        <div class="download-section">
                            <h2>📥 Download Options</h2>
                            <div class="download-buttons">
                                <a href="#" class="download-btn">
                                    <span class="icon">📄</span>
                                    <span class="text">
                                        <strong>PDF - Full Score</strong>
                                        <small>{pages} pages</small>
                                    </span>
                                </a>
                            </div>
                        </div>

                        <div class="ad-placeholder">
                            <p>Advertisement</p>
                        </div>

                        <div class="about-piece">
                            <h2>About This Piece</h2>
                            {content}
                        </div>

                        <div class="practice-tips">
                            <h2>💡 Practice Tips</h2>
                            {practice_tips}
                        </div>

                        <div class="ad-placeholder">
                            <p>Advertisement</p>
                        </div>
                    </div>

                    <aside class="sidebar">
                        <div class="sidebar-widget">
                            <h3>Quick Info</h3>
                            <ul class="info-list">
                                <li><strong>Instrument:</strong> {instrument}</li>
                                <li><strong>Genre:</strong> {genre}</li>
                                <li><strong>Level:</strong> {difficulty}</li>
                                <li><strong>Pages:</strong> {pages}</li>
                                <li><strong>Duration:</strong> {duration}</li>
                            </ul>
                        </div>

                        <div class="ad-placeholder sidebar-ad">
                            <p>Ad</p>
                        </div>

                        <div class="sidebar-widget">
                            <h3>Browse by Category</h3>
                            <ul class="category-list">
                                <li><a href="../piano/index.html">Piano Music</a></li>
                                <li><a href="../guitar/index.html">Guitar Tabs</a></li>
                                <li><a href="../violin/index.html">Violin Music</a></li>
                                <li><a href="../flute/index.html">Flute Music</a></li>
                            </ul>
                        </div>
                    </aside>
                </div>
            </div>
        </article>
    </main>

    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>Sheet Music</h4>
                    <ul>
                        <li><a href="../piano/index.html">Piano</a></li>
                        <li><a href="../guitar/index.html">Guitar</a></li>
                        <li><a href="../violin/index.html">Violin</a></li>
                        <li><a href="../flute/index.html">Flute</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Music Theory</h4>
                    <ul>
                        <li><a href="../../music-theory/scales.html">Scales</a></li>
                        <li><a href="../../music-theory/chords.html">Chords</a></li>
                        <li><a href="../../music-theory/rhythm.html">Rhythm</a></li>
                        <li><a href="../../music-theory/harmony.html">Harmony</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Resources</h4>
                    <ul>
                        <li><a href="../../instruments/index.html">Instrument Guides</a></li>
                        <li><a href="../../blog/index.html">Music Blog</a></li>
                        <li><a href="../../glossary.html">Music Glossary</a></li>
                        <li><a href="../../faq.html">FAQ</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>About</h4>
                    <ul>
                        <li><a href="../../about.html">About Us</a></li>
                        <li><a href="../../privacy.html">Privacy Policy</a></li>
                        <li><a href="../../terms.html">Terms of Use</a></li>
                        <li><a href="../../contact.html">Contact</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Hao Ling Sheng. All sheet music is in the public domain. Educational use only.</p>
            </div>
        </div>
    </footer>
</body>
</html>
"""


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug"""
    return text.lower().replace(' ', '-').replace("'", '').replace('"', '')


def generate_sheet_music_pages(csv_file: str, output_dir: str):
    """Generate HTML pages from CSV data"""
    
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        pages_generated = 0
        
        for row in reader:
            # Generate filename from piece name
            filename = slugify(row['piece_name']) + '.html'
            filepath = os.path.join(output_dir, filename)
            
            # Prepare template variables
            template_vars = {
                'title': row['piece_name'],
                'meta_description': row.get('meta_description', f"Free sheet music for {row['piece_name']}. Download printable PDF score."),
                'keywords': row.get('keywords', f"{row['piece_name']}, {row['instrument']}, sheet music"),
                'full_title': row['full_title'],
                'piece_name': row['piece_name'],
                'composer': row['composer'],
                'composer_years': f"<p><strong>Years:</strong> {row['composer_years']}</p>" if row.get('composer_years') else '',
                'opus_info': f"<p><strong>Opus:</strong> {row['opus']}</p>" if row.get('opus') else '',
                'instrument': row['instrument'],
                'genre': row['genre'],
                'difficulty': row['difficulty'],
                'duration': row['duration'],
                'pages': row['pages'],
                'preview_note': row.get('preview_note', ''),
                'content': row['content'],
                'practice_tips': row.get('practice_tips', '<ul><li>Practice slowly at first</li><li>Focus on difficult passages</li></ul>')
            }
            
            # Generate HTML
            html_content = SHEET_MUSIC_TEMPLATE.format(**template_vars)
            
            # Write to file
            with open(filepath, 'w', encoding='utf-8') as output_file:
                output_file.write(html_content)
            
            pages_generated += 1
            print(f"✓ Generated: {filename}")
    
    print(f"\n🎉 Successfully generated {pages_generated} pages in {output_dir}")


def main():
    """Main function"""
    print("🎵 Hao Ling Sheng HTML Page Generator\n")
    
    # Example usage
    # generate_sheet_music_pages('data/piano-music.csv', 'sheet-music/piano/')
    
    print("Usage:")
    print("  python generate.py")
    print("\nEdit the main() function to specify your CSV file and output directory.")
    print("\nExample:")
    print("  generate_sheet_music_pages('data/piano-music.csv', 'sheet-music/piano/')")


if __name__ == '__main__':
    main()
