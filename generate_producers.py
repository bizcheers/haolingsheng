import os

# Base template for producer pages
TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Music Producer Profile | Hao Ling Sheng</title>
    <meta name="description" content="{description}">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="{url}">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="{name} - Music Producer Profile | Hao Ling Sheng">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{url}">
    <meta property="og:site_name" content="Hao Ling Sheng">

    <!-- Twitter -->
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{name} - Music Producer Profile | Hao Ling Sheng">
    <meta name="twitter:description" content="{description}">

    <!-- Styles -->
    <link rel="stylesheet" href="../styles.css?v=5">
    <link rel="stylesheet" href="producers.css?v=1">

    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Person",
      "name": "{name}",
      "description": "{description}",
      "url": "{url}",
      "jobTitle": "Music Producer",
      "knowsAbout": ["Music Production", "Songwriting", "Record Producing", "Arranging"]
    }}
    </script>
</head>
<body class="producer-body">
    <header>
        <div class="container">
            <div class="logo">
                <img src="../logo.svg" alt="Hao Ling Sheng Logo" class="logo-image">
                <a href="../index.html" class="logo-text">
                    <h1>Hao Ling Sheng</h1>
                    <p class="tagline">Professional Music Education</p>
                </a>
            </div>
            <nav>
                <ul>
                    <li><a href="../gepu/">Music Notation</a></li>
                    <li><a href="../geci/">Music Theory</a></li>
                    <li><a href="../music-production/">Production</a></li>
                    <li><a href="../music-business/">Music Business</a></li>
                    <li><a href="index.html" class="active">Producers</a></li>
                    <li><a href="../about.html">About</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <div class="producer-hero">
        <div class="container">
            <div class="producer-subtitle">{subtitle}</div>
            <h1>{name}</h1>
            <p class="producer-intro">{intro}</p>
        </div>
    </div>

    <div class="container content-grid">
        <section class="feature-section signature-sound-box">
            <h3><div class="icon-box">🎛️</div> Signature Sound</h3>
            <p>{sound}</p>
        </section>

        <section class="feature-section">
            <h3><div class="icon-box">💿</div> Notable Productions</h3>
            <p style="margin-bottom: 20px; color: var(--text-secondary);">Defining hits that shaped the industry:</p>
            <ul class="discography-grid">
                {hits}
            </ul>
        </section>

        <section class="feature-section">
            <h3><div class="icon-box">🚀</div> Impact on Industry</h3>
            <p>{impact}</p>
        </section>

        <div class="section-header" style="margin-top: 60px;">
            <h2>Explore More Legends</h2>
        </div>
        
        <div class="producer-index-grid">
            <a href="max-martin.html" class="producer-index-card">
                <div class="card-content">
                    <div class="card-role">Pop Mastermind</div>
                    <h2>Max Martin</h2>
                </div>
            </a>
            <a href="rick-rubin.html" class="producer-index-card">
                <div class="card-content">
                    <div class="card-role">The Reducer</div>
                    <h2>Rick Rubin</h2>
                </div>
            </a>
            <a href="quincy-jones.html" class="producer-index-card">
                <div class="card-content">
                    <div class="card-role">The Titan</div>
                    <h2>Quincy Jones</h2>
                </div>
            </a>
            <a href="timbaland.html" class="producer-index-card">
                <div class="card-content">
                    <div class="card-role">Rhythm King</div>
                    <h2>Timbaland</h2>
                </div>
            </a>
            <a href="pharrell-williams.html" class="producer-index-card">
                <div class="card-content">
                    <div class="card-role">Neptunes Sound</div>
                    <h2>Pharrell</h2>
                </div>
            </a>
            <a href="dr-dre.html" class="producer-index-card">
                <div class="card-content">
                    <div class="card-role">G-Funk Architect</div>
                    <h2>Dr. Dre</h2>
                </div>
            </a>
        </div>
    </div>

    <footer>
        <div class="container">
            <div class="footer-bottom">
                 <p>&copy; 2026 Hao Ling Sheng. All educational content is provided for learning purposes.</p>
            </div>
        </div>
    </footer>
</body>
</html>
"""

# Template for the main index file
INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Legendary Music Producers & Artists | Hao Ling Sheng</title>
    <meta name="description" content="Explore profiles of the world's greatest music producers, from Max Martin to Rick Rubin. Learn about their signature sounds and hit records.">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="https://www.haolingsheng.com/singer/index.html">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="Legendary Music Producers & Artists | Hao Ling Sheng">
    <meta property="og:description" content="Explore profiles of the world's greatest music producers, from Max Martin to Rick Rubin.">
    <meta property="og:url" content="https://www.haolingsheng.com/singer/index.html">
    <meta property="og:site_name" content="Hao Ling Sheng">

    <link rel="stylesheet" href="../styles.css?v=5">
    <link rel="stylesheet" href="producers.css?v=1">
</head>
<body class="producer-body">
    <header>
        <div class="container">
            <div class="logo">
                <img src="../logo.svg" alt="Hao Ling Sheng Logo" class="logo-image">
                <a href="../index.html" class="logo-text">
                    <h1>Hao Ling Sheng</h1>
                    <p class="tagline">Professional Music Education</p>
                </a>
            </div>
            <nav>
                <ul>
                    <li><a href="../gepu/">Music Notation</a></li>
                    <li><a href="../geci/">Music Theory</a></li>
                    <li><a href="../music-production/">Production</a></li>
                    <li><a href="../music-business/">Music Business</a></li>
                    <li><a href="index.html" class="active">Producers</a></li>
                    <li><a href="../about.html">About</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <div class="producer-hero">
        <div class="container">
            <div class="producer-subtitle">The Architects of Sound</div>
            <h1>Legendary Producers</h1>
            <p class="producer-intro">Discover the masterminds behind your favorite songs. From pop geniuses to hip-hop moguls, meet the producers who shaped modern music history.</p>
        </div>
    </div>

    <div class="container">
        <div class="producer-index-grid">
            {cards}
        </div>
    </div>

    <footer>
        <div class="container">
            <div class="footer-bottom">
                 <p>&copy; 2026 Hao Ling Sheng. All educational content is provided for learning purposes.</p>
            </div>
        </div>
    </footer>
</body>
</html>
"""

producers = [
    {
        "filename": "max-martin.html",
        "name": "Max Martin",
        "role": "Pop Melody Genius",
        "subtitle": "The King of Pop Melodies",
        "description": "Profile of Max Martin, the Swedish songwriter and producer responsible for more #1 hits than anyone since Lennon & McCartney.",
        "intro": "Karl Martin Sandberg, known professionally as Max Martin, is a Swedish record producer and songwriter. He is widely acknowledged as one of the most successful pop music producers in history, crafting hits for artists ranging from Britney Spears to Taylor Swift and The Weeknd.",
        "sound": "Max Martin is famous for 'Melodic Math' &ndash; a theory that the melody is king. His tracks notoriously feature extremely catchy hooks, polished vocal production, and a structure designed to get to the chorus as effectively as possible.",
        "hits": """
            <li><span class="track-name">...Baby One More Time</span> <span class="artist-name">Britney Spears</span></li>
            <li><span class="track-name">I Want It That Way</span> <span class="artist-name">Backstreet Boys</span></li>
            <li><span class="track-name">Shake It Off</span> <span class="artist-name">Taylor Swift</span></li>
            <li><span class="track-name">Blinding Lights</span> <span class="artist-name">The Weeknd</span></li>
            <li><span class="track-name">Roar</span> <span class="artist-name">Katy Perry</span></li>
        """,
        "impact": "With over 25 Billboard Hot 100 number-one singles as a writer or co-writer, Max Martin has defined the sound of modern pop radio for three decades. His collaborative approach and mentorship have spawned a new generation of Swedish pop dominance."
    },
    {
        "filename": "rick-rubin.html",
        "name": "Rick Rubin",
        "role": "Minimalist Visionary",
        "subtitle": "The Zen Master of Reduction",
        "description": "Rick Rubin's production style focuses on stripping away the unnecessary to reveal the raw emotion of the artist.",
        "intro": "Frederick Jay 'Rick' Rubin is an American record executive and record producer. He is the co-founder of Def Jam Recordings and established American Recordings. Rubin helped popularize hip hop music before transcending all genres.",
        "sound": "Rubin is known for a stripped-down sound, often referred to as 'dry'. He avoids heavy reverb and unnecessary instrumentation, preferring to capture the authentic performance of the artist in a room. He listens not for technical perfection, but for feeling.",
        "hits": """
            <li><span class="track-name">Walk This Way</span> <span class="artist-name">Run-D.M.C. ft. Aerosmith</span></li>
            <li><span class="track-name">Hurt</span> <span class="artist-name">Johnny Cash</span></li>
            <li><span class="track-name">99 Problems</span> <span class="artist-name">Jay-Z</span></li>
            <li><span class="track-name">Under the Bridge</span> <span class="artist-name">Red Hot Chili Peppers</span></li>
            <li><span class="track-name">Chop Suey!</span> <span class="artist-name">System of a Down</span></li>
        """,
        "impact": "Rubin has successfully produced for artists across metal, hip hop, rock, and country. His work with Johnny Cash on the 'American Recordings' series is legendary for revitalizing Cash's career and proving that great art transcends age."
    },
    {
        "filename": "quincy-jones.html",
        "name": "Quincy Jones",
        "role": "The Maestro",
        "subtitle": "The Titan of Music",
        "description": "Quincy Jones is a legendary producer, composer, and arranger, best known for his work with Michael Jackson on Thriller.",
        "intro": "Quincy Delight Jones Jr. is an American record producer, musician, songwriter, composer, arranger, and film and television producer. His career spans over 70 years in the entertainment industry, earning him 28 Grammys.",
        "sound": "Quincy's sound is characterized by lush orchestration, impeccable jazz-influenced arrangements, and a groove that is undeniable. He is a master of blending genres, from big band to funk and pop, always serving the song.",
        "hits": """
            <li><span class="track-name">Billie Jean</span> <span class="artist-name">Michael Jackson</span></li>
            <li><span class="track-name">Thriller</span> <span class="artist-name">Michael Jackson</span></li>
            <li><span class="track-name">We Are the World</span> <span class="artist-name">USA for Africa</span></li>
            <li><span class="track-name">Fly Me to the Moon</span> <span class="artist-name">Frank Sinatra (Arr.)</span></li>
            <li><span class="track-name">Give Me the Night</span> <span class="artist-name">George Benson</span></li>
        """,
        "impact": "Producing 'Thriller', the best-selling album of all time, cements his legacy. He broke down racial barriers in the music industry and brought jazz sophistication to pop music."
    },
    {
        "filename": "timbaland.html",
        "name": "Timbaland",
        "role": "Rhythm Innovator",
        "subtitle": "The Beat Magician",
        "description": "Timbaland revolutionized R&B and Hip Hop with his unique stuttering drums and sampling style.",
        "intro": "Timothy Zachary Mosley, known professionally as Timbaland, is an American record producer, rapper, singer, and songwriter. He has received widespread acclaim for his innovative production work with Missy Elliott, Aaliyah, and Justin Timberlake.",
        "sound": "Timbaland's signature sound involves complex, syncopated drum patterns, beatboxing used as percussion, and creative use of foreign samples and vocal grunts. He created a futuristic sound that defined the 2000s.",
        "hits": """
            <li><span class="track-name">Cry Me a River</span> <span class="artist-name">Justin Timberlake</span></li>
            <li><span class="track-name">Get Ur Freak On</span> <span class="artist-name">Missy Elliott</span></li>
            <li><span class="track-name">Promiscuous</span> <span class="artist-name">Nelly Furtado</span></li>
            <li><span class="track-name">SexyBack</span> <span class="artist-name">Justin Timberlake</span></li>
            <li><span class="track-name">Dirt Off Your Shoulder</span> <span class="artist-name">Jay-Z</span></li>
        """,
        "impact": "His partnership with Missy Elliott and Justin Timberlake produced some of the most innovative pop and R&B tracks of the century. He proved that hip-hop beats could drive global pop smashes."
    },
    {
        "filename": "pharrell-williams.html",
        "name": "Pharrell Williams",
        "role": "The Hitmaker",
        "subtitle": "The Neptune Sound",
        "description": "Pharrell Williams, part of The Neptunes, brings a funk-infused, minimal, and infectious energy to his productions.",
        "intro": "Pharrell Lanscilo Williams is an American record producer, rapper, singer, and songwriter. Alongside Chad Hugo, he formed the hip hop and R&B production duo The Neptunes, creating the soundtrack of the early 2000s.",
        "sound": "The Neptunes' sound is instantly recognizable: dry, punchy drums, Korg Triton presets, specific guitar strums, and a four-count start. It's minimalist funk adjusted for the digital age.",
        "hits": """
            <li><span class="track-name">Happy</span> <span class="artist-name">Pharrell Williams</span></li>
            <li><span class="track-name">Drop It Like It's Hot</span> <span class="artist-name">Snoop Dogg</span></li>
            <li><span class="track-name">Hollaback Girl</span> <span class="artist-name">Gwen Stefani</span></li>
            <li><span class="track-name">Hot in Herre</span> <span class="artist-name">Nelly</span></li>
            <li><span class="track-name">Get Lucky</span> <span class="artist-name">Daft Punk (Co-prod)</span></li>
        """,
        "impact": "Pharrell redefined 'cool' in music and fashion. The Neptunes dominated radio in the early 2000s, producing hits for everyone from Britney Spears to Clipse."
    },
    {
        "filename": "dr-dre.html",
        "name": "Dr. Dre",
        "role": "Hip-Hop Icon",
        "subtitle": "The West Coast Architect",
        "description": "Dr. Dre pioneered G-Funk and launched the careers of Eminem, Snoop Dogg, and 50 Cent.",
        "intro": "Andre Romelle Young, known professionally as Dr. Dre, is an American rapper, record producer, and entrepreneur. He is the founder and CEO of Aftermath Entertainment and Beats Electronics.",
        "sound": "G-Funk: slower tempos, deep basslines, whiny synthesizers (like the Moog), and soulful female backing vocals. Dre is a perfectionist known for the cleanest mixing and drums in hip-hop history.",
        "hits": """
            <li><span class="track-name">Nuthin' but a 'G' Thang</span> <span class="artist-name">Dr. Dre ft. Snoop Dogg</span></li>
            <li><span class="track-name">Still D.R.E.</span> <span class="artist-name">Dr. Dre ft. Snoop Dogg</span></li>
            <li><span class="track-name">In Da Club</span> <span class="artist-name">50 Cent</span></li>
            <li><span class="track-name">My Name Is</span> <span class="artist-name">Eminem</span></li>
            <li><span class="track-name">California Love</span> <span class="artist-name">2Pac</span></li>
        """,
        "impact": "Dre not only created the G-Funk sound but also discovered diverse talents like Eminem and 50 Cent, proving he has the best ear for talent in the game."
    }
]

def generate_pages():
    os.makedirs('singer', exist_ok=True)
    
    cards_html = ""
    
    for producer in producers:
        # Generate individual page
        full_url = f"https://www.haolingsheng.com/singer/{producer['filename']}"
        html_content = TEMPLATE.format(
            name=producer['name'],
            subtitle=producer['subtitle'],
            description=producer['description'],
            url=full_url,
            intro=producer['intro'],
            sound=producer['sound'],
            hits=producer['hits'],
            impact=producer['impact']
        )
        
        with open(f"singer/{producer['filename']}", 'w') as f:
            f.write(html_content)
        print(f"Generated {producer['filename']}")
        
        # Add to index card list
        cards_html += f"""
        <a href="{producer['filename']}" class="producer-index-card">
            <div class="card-content">
                <div class="card-role">{producer['role']}</div>
                <h2>{producer['name']}</h2>
                <div class="card-subtitle">{producer['subtitle']}</div>
                <p class="card-intro">{producer['intro'][:120]}...</p>
            </div>
            <div class="card-footer">
                <span class="read-more-btn">Read Profile →</span>
            </div>
        </a>
        """

    # Generate Index Page
    index_content = INDEX_TEMPLATE.format(cards=cards_html)
    with open('singer/index.html', 'w') as f:
        f.write(index_content)
    print("Generated singer/index.html")

if __name__ == "__main__":
    generate_pages()
