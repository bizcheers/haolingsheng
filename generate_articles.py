#!/usr/bin/env python3
"""
Batch create music notation articles
"""

articles = {
    "f-major-key-signature": {
        "title": "F Major Key Signature: The Key with One Flat",
        "description": "Learn F major key signature with B♭. Understand why F major has one flat and how to play the F major scale on piano and other instruments.",
        "keywords": "f major key signature, one flat key, f major scale, b flat in f major",
        "h1": "F Major Key Signature: One Flat Makes All the Difference",
        "content": """
<section>
    <h2>Welcome to Your First Flat</h2>
    <p>After mastering <a href="c-major-key-signature.html">C major</a> with its zero sharps and flats, F major is often the next stop on your musical journey. Why? Because it introduces you to the world of flats—but just one flat, so it's not overwhelming.</p>
    <p>F major has exactly <strong>one flat: B♭ (B-flat)</strong>. Every time you see a B in F major music, you play it as B♭ instead of B natural. That's the only difference from C major. Not too scary, right?</p>
</section>

<section>
    <h2>The F Major Scale</h2>
    <p>The F major scale goes: <strong>F - G - A - B♭ - C - D - E - F</strong>. Notice how it's almost all natural notes except for that one B♭ sitting in the middle.</p>
    <p>On a piano, start at F (the white key just before the group of three black keys) and play: F, G, A, then hit the black key for B♭, then continue with C, D, E, and back to F. You've just played F major!</p>
    <p>The pattern of whole and half steps is the same as every major scale: W-W-H-W-W-W-H. But in F major, that pattern requires lowering the B to B♭ to make it work.</p>
</section>

<section>
    <h2>Why B♭ and Not Some Other Note?</h2>
    <p>Good question! It all comes down to maintaining that major scale pattern. If you tried to build a major scale starting on F using only natural notes, the intervals wouldn't line up correctly. You'd get F-G-A-B-C-D-E-F, which sounds wrong because the B natural creates an incorrect interval.</p>
    <p>By flatting the B, you fix the pattern. Suddenly everything sounds right—bright, major, and properly balanced. This is why <a href="how-to-read-key-signatures.html">key signatures</a> exist: to tell you which notes need to be modified to make the scale work.</p>
</section>

<section>
    <h2>Reading F Major Sheet Music</h2>
    <p>When you look at sheet music in F major, you'll see one flat symbol (♭) sitting on the B line in the key signature. This appears right after the clef at the beginning of each staff.</p>
    <p>That flat symbol means: "Every B in this piece is played as B♭ unless otherwise noted." You don't need to see a flat symbol before every single B—the key signature handles it for you. This is way more efficient than writing ♭ symbols all over the place.</p>
</section>

<section>
    <h2>Common F Major Chords</h2>
    <p>The basic chords in F major are:</p>
    <ul>
        <li><strong>F major (I)</strong>: F-A-C — Your home chord</li>
        <li><strong>B♭ major (IV)</strong>: B♭-D-F — Notice the B♭ from the key signature</li>
        <li><strong>C major (V)</strong>: C-E-G — Creates tension that resolves to F</li>
    </ul>
    <p>Many popular songs use F major because it sits comfortably in the middle range for both singers and instruments. It's not too high, not too low—just right.</p>
</section>

<section>
    <h2>F Major vs. C Major</h2>
    <p>The main difference is that one flat. But this small change affects the entire feel and range of the key:</p>
    <ul>
        <li><strong>C major</strong>: All white keys on piano, bright and simple</li>
        <li><strong>F major</strong>: One black key (B♭), slightly warmer tone</li>
    </ul>
    <p>F major is particularly popular in band music because it works well for brass and woodwind instruments. Many school bands play in F major or B♭ major because these keys suit the instruments' natural ranges.</p>
</section>

<section>
    <h2>The Relative Minor: D Minor</h2>
    <p>F major shares its key signature with D minor. Both have one flat (B♭), but D minor starts on D and has a darker, more serious character. Same notes, different emotional vibe.</p>
</section>

<section>
    <h2>Practice Tips</h2>
    <ul>
        <li><strong>Drill the scale</strong>: Play F major up and down until the B♭ feels automatic</li>
        <li><strong>Watch for B naturals</strong>: Sometimes composers use B natural as an accidental in F major for special effect</li>
        <li><strong>Practice chord progressions</strong>: Try F-B♭-C-F or F-Dm-B♭-C</li>
        <li><strong>Learn simple songs</strong>: Many folk songs and hymns are written in F major</li>
    </ul>
</section>

<section>
    <h2>Moving Forward</h2>
    <p>Once you're comfortable with F major's one flat, you can explore keys with more flats like B♭ major (two flats) or E♭ major (three flats). Or you might venture into sharp keys like <a href="g-major-key-signature.html">G major</a> (one sharp).</p>
    <p>F major is your gateway to understanding how flats work in key signatures. Master this one flat, and adding more flats later becomes much easier.</p>
</section>
""",
        "sidebar": """
<div class="sidebar-card">
    <h4>QUICK FACTS</h4>
    <p><strong>Sharps:</strong> 0</p>
    <p><strong>Flats:</strong> 1 (B♭)</p>
    <p><strong>Scale notes:</strong> F-G-A-B♭-C-D-E</p>
    <p><strong>Relative minor:</strong> D minor</p>
</div>
<div class="sidebar-card">
    <h4>REMEMBER THIS</h4>
    <p>In F major, every B is played as B♭. That's the only flat in the key!</p>
</div>
<div class="sidebar-card">
    <h4>PRO TIP</h4>
    <p>F major is extremely common in band music. If you play a wind instrument, you'll see this key a lot!</p>
</div>
"""
    }
}

# Generate HTML for each article
template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <link rel="canonical" href="https://www.haolingsheng.com/gepu/{filename}.html">
    <link rel="stylesheet" href="../styles.css">
    <link rel="stylesheet" href="article.css">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@type":"Article","headline":"{title}","description":"{description}","author":{{"@type":"Organization","name":"Hao Ling Sheng"}},"publisher":{{"@type":"Organization","name":"Hao Ling Sheng","logo":{{"@type":"ImageObject","url":"https://www.haolingsheng.com/logo.svg"}}}},"datePublished":"2026-02-03","dateModified":"2026-02-03"}}
    </script>
</head>
<body>
    <header>
        <div class="container">
            <div class="logo">
                <img src="../logo.svg" alt="Hao Ling Sheng Logo" class="logo-image">
                <a href="../index.html" class="logo-text"><h1>Hao Ling Sheng</h1><p class="tagline">Professional Music Education</p></a>
            </div>
            <nav><ul><li><a href="../gepu/">Music Notation</a></li><li><a href="../geci/">Music Theory</a></li><li><a href="../music-production/">Production</a></li><li><a href="../music-business/">Music Business</a></li><li><a href="../about.html">About</a></li></ul></nav>
        </div>
    </header>
    <main class="article-page">
        <div class="container">
            <article class="article-content">
                <div class="breadcrumb"><a href="../index.html">Home</a> / <a href="index.html">Music Notation</a> / <span>Key Signatures</span></div>
                <h1>{h1}</h1>
                <div class="article-meta"><span>📚 Music Notation</span><span>⏱️ 7 min read</span><span>📅 February 2026</span></div>
                {content}
                <div class="related-articles">
                    <h3>Continue Learning</h3>
                    <ul>
                        <li><a href="how-to-read-key-signatures.html">How to Read Key Signatures</a></li>
                        <li><a href="c-major-key-signature.html">C Major Key Signature</a></li>
                        <li><a href="g-major-key-signature.html">G Major Key Signature</a></li>
                        <li><a href="../geci/circle-of-fifths-guide.html">Circle of Fifths</a></li>
                    </ul>
                </div>
            </article>
            <aside class="sidebar">
                {sidebar}
            </aside>
        </div>
    </main>
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-section"><h4>Resources</h4><ul><li><a href="../gepu/">Music Notation</a></li><li><a href="../geci/">Music Theory</a></li><li><a href="../music-production/">Production</a></li><li><a href="../music-business/">Music Business</a></li></ul></div>
                <div class="footer-section"><h4>Company</h4><ul><li><a href="../about.html">About Us</a></li><li><a href="../contact.html">Contact</a></li><li><a href="../privacy.html">Privacy Policy</a></li><li><a href="../terms.html">Terms of Service</a></li></ul></div>
                <div class="footer-section"><h4>Connect</h4><ul><li><a href="https://timeuo.com/" rel="dofollow noopener" target="_blank">Time Zone Converter</a></li></ul></div>
            </div>
            <div class="footer-bottom"><p>&copy; 2026 Hao Ling Sheng. All educational content is provided for learning purposes.</p></div>
        </div>
    </footer>
</body>
</html>'''

for filename, data in articles.items():
    html = template.format(
        filename=filename,
        title=data['title'],
        description=data['description'],
        keywords=data['keywords'],
        h1=data['h1'],
        content=data['content'],
        sidebar=data['sidebar']
    )
    
    with open(f'/Users/bizcheers/jan-20-haolingsheng/haolingsheng/gepu/{filename}.html', 'w') as f:
        f.write(html)
    
    print(f"✓ Created {filename}.html")

print("\n✅ Article generation complete!")
