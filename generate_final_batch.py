#!/usr/bin/env python3
"""
Generate final set of music notation articles
"""

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
                <div class="breadcrumb"><a href="../index.html">Home</a> / <a href="index.html">Music Notation</a> / <span>{breadcrumb}</span></div>
                <h1>{h1}</h1>
                <div class="article-meta"><span>📚 Music Notation</span><span>⏱️ {read_time} min read</span><span>📅 February 2026</span></div>
                {content}
                <div class="related-articles">
                    <h3>Continue Learning</h3>
                    <ul>{related_links}</ul>
                </div>
            </article>
            <aside class="sidebar">{sidebar}</aside>
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

articles = {
    "what-does-3-4-time-mean": {
        "title": "What Does 3/4 Time Mean? Exploring Waltz Rhythm and Beyond",
        "description": "Learn all about the 3/4 time signature. Discover why it's called 'waltz time', how to count it, and its unique feel compared to 4/4 meter.",
        "keywords": "3/4 time signature, waltz time explained, counting 3/4 music, music theory 3/4 meter",
        "h1": "What Does 3/4 Time Mean? The Dance of Three",
        "breadcrumb": "3/4 Time",
        "read_time": "7",
        "content": '''
<section>
    <h2>The Elegant Waltz Rhythm</h2>
    <p>If <a href="understanding-4-4-time-signature.html">4/4 time</a> is a steady march, then <strong>3/4 time</strong> is a graceful dance. Often called "waltz time," this meter has a unique triple feel that feels circular and flowing rather than square and stable.</p>
    <p>But beyond just waltzes, 3/4 time appears in everything from folk songs to modern pop ballads. Let's look at what makes it tick.</p>
</section>

<section>
    <h2>Breaking Down the Numbers</h2>
    <p>Just like our other time signatures, the numbers tell a specific story:</p>
    <ul>
        <li><strong>Top 3</strong>: There are three beats in every measure.</li>
        <li><strong>Bottom 4</strong>: The quarter note gets the beat.</li>
    </ul>
    <p>So, instead of counting 1-2-3-4, we count: <strong>1 - 2 - 3, 1 - 2 - 3.</strong> It's a repeating cycle of three quarter-note beats.</p>
</section>

<section>
    <h2>The Feel: Strong-Weak-Weak</h2>
    <p>The magic of 3/4 time is in the emphasis. Typically, only <strong>Beat 1</strong> is strong. Beats 2 and 3 are weak. This creates a "OOM-pah-pah, OOM-pah-pah" sound that is the heart of the waltz.</p>
</section>
''',
        "sidebar": '''
<div class="sidebar-card">
    <h4>QUICK REFERENCE</h4>
    <p><strong>3/4 Time:</strong> 3 quarter notes per measure</p>
    <p><strong>The Pulse:</strong> ONE - two - three</p>
</div>
''',
        "related_links": '''
<li><a href="understanding-4-4-time-signature.html">Understanding 4/4 Time</a></li>
<li><a href="6-8-time-signature-explained.html">6/8 Time Signature</a></li>
'''
    },
    
    "6-8-time-signature-explained": {
        "title": "6/8 Time Signature Explained: Compound Meter Made Simple",
        "description": "Demystify 6/8 time signature. Learn the difference between 6/8 and 3/4, how to count compound meter, and feel the galloping rhythm of six.",
        "keywords": "6/8 vs 3/4, compound meter explained, 6/8 time signature counting, music theory rhythm",
        "h1": "6/8 Time Signature: The Galloping Compound Meter",
        "breadcrumb": "6/8 Time",
        "read_time": "8",
        "content": '''
<section>
    <h2>Is It Just Two Measures of Three?</h2>
    <p>At first glance, <strong>6/8 time</strong> looks like it might just be two bars of 3/4 smashed together. But musicians feel it very differently. While 3/4 feels like "ONE-two-three," 6/8 usually feels like "ONE-two-three, FOUR-five-six."</p>
    <p>This is what we call a <strong>compound meter</strong>. The beats are grouped in threes, giving it a swaying, galloping, or "triplet" feel that 4/4 and 3/4 just don't have.</p>
</section>

<section>
    <h2>The 6/8 Logic</h2>
    <ul>
        <li><strong>Top 6</strong>: Six beats per measure.</li>
        <li><strong>Bottom 8</strong>: The eighth note gets the beat.</li>
    </ul>
    <p>In practice, we usually feel this as two big pulses per measure, with each pulse containing three faster eighth notes. Think: <strong>ONE</strong>-and-a-<strong>TWO</strong>-and-a.</p>
</section>
''',
        "sidebar": '''
<div class="sidebar-card">
    <h4>QUICK COMPARISON</h4>
    <p><strong>3/4:</strong> 3 groups of 2</p>
    <p><strong>6/8:</strong> 2 groups of 3</p>
</div>
''',
        "related_links": '''
<li><a href="what-does-3-4-time-mean.html">What Does 3/4 Time Mean?</a></li>
<li><a href="understanding-4-4-time-signature.html">4/4 Time Signature</a></li>
'''
    },
    
    "how-to-read-key-signatures": {
        "title": "How to Read Key Signatures: The Ultimate Guide for Beginners",
        "description": "Unlock any piece of music by learning how to read key signatures. Understand the order of sharps and flats and use simple tricks to identify the key instantly.",
        "keywords": "reading key signatures, sharps and flats in key, order of sharps and flats, music theory key recognition",
        "h1": "How to Read Key Signatures: Your Musical Roadmap",
        "breadcrumb": "Key Signatures",
        "read_time": "9",
        "content": '''
<section>
    <h2>Stopped Guessing, Started Reading</h2>
    <p>Have you ever looked at a group of sharps or flats at the start of a song and felt stuck? Those are <strong>key signatures</strong>, and they are actually your best friend. Instead of writing a sharp symbol every single time a note appears, the key signature sets the rules for the entire song up front.</p>
    <p>Once you learn a few simple tricks, you'll be able to look at any key signature and instantly know exactly which notes to play.</p>
</section>

<section>
    <h2>The Order of Sharps and Flats</h2>
    <p>Sharps and flats are always added in a specific, predictable order. If a key has one sharp, it's always F#. If it has two, they are always F# and C#.</p>
    <ul>
        <li><strong>Order of Sharps:</strong> F - C - G - D - A - E - B (Fat Cats Go Down Alleys Eating Birds)</li>
        <li><strong>Order of Flats:</strong> B - E - A - D - G - C - F (BEAD-Go-Call-Fred)</li>
    </ul>
</section>
''',
        "sidebar": '''
<div class="sidebar-card">
    <h4>PRO TRICK: SHARPS</h4>
    <p>Go up one half-step from the last sharp to find the key!</p>
</div>
<div class="sidebar-card">
    <h4>PRO TRICK: FLATS</h4>
    <p>The second-to-last flat is the name of the key!</p>
</div>
''',
        "related_links": '''
<li><a href="c-major-key-signature.html">C Major Key Signature</a></li>
<li><a href="g-major-key-signature.html">G Major Key Signature</a></li>
'''
    },
    
    "a-minor-key-signature": {
        "title": "A Minor Key Signature: The Relative Minor of C Major",
        "description": "Explore the A minor key signature. Learn why it has no sharps or flats, how it relates to C major, and its unique melancholic sound.",
        "keywords": "a minor key signature, relative minor of c major, key signature with no sharps, natural minor scale",
        "h1": "A Minor Key Signature: Shadow of the Major",
        "breadcrumb": "A Minor",
        "read_time": "7",
        "content": '''
<section>
    <h2>Same Notes, Different Soul</h2>
    <p>Just like <a href="c-major-key-signature.html">C major</a>, the key of <strong>A minor</strong> has no sharps and no flats in its key signature. They share the same collection of notes, but they couldn't sound more different.</p>
    <p>While C major sounds bright, happy, and resolved, A minor sounds introspective, dark, and often a bit sad. This relationship is called being <strong>relative keys</strong>.</p>
</section>

<section>
    <h2>The Relative Minor Connection</h2>
    <p>Every major key has a "relative minor" that lives three half-steps below it. For C major, that's A minor. Because they share the same key signature, you can move between them seamlessly in a song to change the mood from joyful to melancholic.</p>
</section>
''',
        "sidebar": '''
<div class="sidebar-card">
    <h4>QUICK FACTS</h4>
    <p><strong>Sharps/Flats:</strong> 0</p>
    <p><strong>Home Note:</strong> A</p>
</div>
''',
        "related_links": '''
<li><a href="c-major-key-signature.html">C Major Key Signature</a></li>
<li><a href="how-to-read-key-signatures.html">How to Read Key Signatures</a></li>
'''
    }
}

for filename, data in articles.items():
    html = template.format(
        filename=filename,
        title=data['title'],
        description=data['description'],
        keywords=data['keywords'],
        h1=data['h1'],
        breadcrumb=data['breadcrumb'],
        read_time=data['read_time'],
        content=data['content'],
        sidebar=data['sidebar'],
        related_links=data['related_links']
    )
    
    filepath = f'/Users/bizcheers/jan-20-haolingsheng/haolingsheng/gepu/{filename}.html'
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✓ Created {filename}.html")
