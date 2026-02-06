import os

# Base template for producer pages
TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Music Producer Profile | Hao Ling Sheng</title>
    <meta name="description" content="{description}">
    <link rel="stylesheet" href="../styles.css">
    <link rel="stylesheet" href="../gepu/article.css">
    <style>
        .producer-header {{
            background: linear-gradient(135deg, #2c3e50, #4ca1af);
            color: white;
            padding: 40px 20px;
            text-align: center;
            border-radius: 12px;
            margin-bottom: 30px;
        }}
        .producer-header h1 {{
            margin: 0;
            font-size: 2.5em;
            color: white;
        }}
        .producer-header p {{
            margin-top: 10px;
            font-size: 1.2em;
            opacity: 0.9;
            color: #ecf0f1;
        }}
        .discography-list {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            border-left: 5px solid #4ca1af;
        }}
        .discography-list li {{
            margin-bottom: 10px;
            list-style: none;
            padding-left: 20px;
            position: relative;
        }}
        .discography-list li:before {{
            content: "🎵";
            position: absolute;
            left: 0;
        }}
        .signature-sound {{
            background: #fff3e0;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
    <header>
        <div class="logo">
            <a href="../index.html">Hao Ling Sheng</a>
        </div>
        <nav>
            <a href="../sheet-music/index.html">Sheet Music</a>
            <a href="../music-production/index.html">Production</a>
            <a href="../music-business/index.html">Business</a>
            <a href="index.html" class="active">Producers</a>
        </nav>
    </header>

    <div class="container">
        <div class="producer-header">
            <h1>{name}</h1>
            <p>{subtitle}</p>
        </div>

        <article class="content">
            <h2>The Legend Behind the Hits</h2>
            <p>{intro}</p>

            <div class="signature-sound">
                <h3>🎛️ Signature Sound</h3>
                <p>{sound}</p>
            </div>

            <h2>Notable Productions</h2>
            <p>Some of the most iconic tracks produced by {name} include:</p>
            <ul class="discography-list">
                {hits}
            </ul>

            <h2>Impact on Music Industry</h2>
            <p>{impact}</p>
        </article>

        <div class="related-producers">
            <h3>Explore More Producers</h3>
            <div class="grid-links">
                <a href="max-martin.html">Max Martin</a>
                <a href="rick-rubin.html">Rick Rubin</a>
                <a href="quincy-jones.html">Quincy Jones</a>
                <a href="timbaland.html">Timbaland</a>
                <a href="pharrell-williams.html">Pharrell Williams</a>
                <a href="dr-dre.html">Dr. Dre</a>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; 2024 Hao Ling Sheng. All rights reserved.</p>
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
    <link rel="stylesheet" href="../styles.css">
    <style>
        .producer-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }}
        .producer-card {{
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            transition: transform 0.2s;
            border: 1px solid #eee;
        }}
        .producer-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        }}
        .producer-card h2 {{
            margin-top: 0;
            color: #2c3e50;
        }}
        .producer-card .role {{
            color: #666;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: bold;
            display: block;
            margin-bottom: 15px;
        }}
        .producer-card p {{
            color: #555;
            line-height: 1.6;
        }}
        .read-more {{
            display: inline-block;
            margin-top: 15px;
            color: #3498db;
            text-decoration: none;
            font-weight: bold;
        }}
        .read-more:hover {{
            text-decoration: underline;
        }}
        .hero-section {{
            background: linear-gradient(135deg, #1a2a6c, #b21f1f, #fdbb2d);
            color: white;
            padding: 60px 20px;
            text-align: center;
            border-radius: 0 0 20px 20px;
            margin-bottom: 40px;
        }}
        .hero-section h1 {{ margin: 0; font-size: 3em; }}
        .hero-section p {{ font-size: 1.2em; opacity: 0.9; max-width: 600px; margin: 20px auto 0; }}
    </style>
</head>
<body>
    <header>
        <div class="logo">
            <a href="../index.html">Hao Ling Sheng</a>
        </div>
        <nav>
            <a href="../sheet-music/index.html">Sheet Music</a>
            <a href="../music-production/index.html">Production</a>
            <a href="../music-business/index.html">Business</a>
            <a href="index.html" class="active">Producers</a>
        </nav>
    </header>

    <div class="hero-section">
        <h1>The Architects of Sound</h1>
        <p>Discover the masterminds behind your favorite songs. From pop geniuses to hip-hop moguls, meet the producers who shaped modern music.</p>
    </div>

    <div class="container">
        <div class="producer-grid">
            {cards}
        </div>
    </div>

    <footer>
        <p>&copy; 2024 Hao Ling Sheng. All rights reserved.</p>
    </footer>
</body>
</html>
"""

producers = [
    {
        "filename": "max-martin.html",
        "name": "Max Martin",
        "subtitle": "The King of Pop Melodies",
        "description": "Profile of Max Martin, the Swedish songwriter and producer responsible for more #1 hits than anyone since Lennon & McCartney.",
        "intro": "Karl Martin Sandberg, known professionally as Max Martin, is a Swedish record producer and songwriter. He is widely acknowledged as one of the most successful pop music producers in history, crafting hits for artists ranging from Britney Spears to Taylor Swift and The Weeknd.",
        "sound": "Max Martin is famous for 'Melodic Math' &ndash; a theory that the melody is king. His tracks notoriously feature extremely catchy hooks, polished vocal production, and a structure designed to get to the chorus as effectively as possible.",
        "hits": """
            <li><strong>...Baby One More Time</strong> - Britney Spears</li>
            <li><strong>I Want It That Way</strong> - Backstreet Boys</li>
            <li><strong>Shake It Off</strong> - Taylor Swift</li>
            <li><strong>Blinding Lights</strong> - The Weeknd</li>
            <li><strong>Can't Feel My Face</strong> - The Weeknd</li>
        """,
        "impact": "With over 25 Billboard Hot 100 number-one singles as a writer or co-writer, Max Martin has defined the sound of modern pop radio for three decades. His collaborative approach and mentorship have spawned a new generation of Swedish pop dominance."
    },
    {
        "filename": "rick-rubin.html",
        "name": "Rick Rubin",
        "subtitle": "The Zen Master of Reduction",
        "description": "Rick Rubin's production style focuses on stripping away the unnecessary to reveal the raw emotion of the artist.",
        "intro": "Frederick Jay 'Rick' Rubin is an American record executive and record producer. He is the co-founder of Def Jam Recordings and also established American Recordings. Rubin helped popularize hip hop music.",
        "sound": "Rubin is known for a stripped-down sound, often referred to as 'dry'. He avoids heavy reverb and unnecessary instrumentation, preferring to capture the authentic performance of the artist in a room.",
        "hits": """
            <li><strong>Walk This Way</strong> - Run-D.M.C. ft. Aerosmith</li>
            <li><strong>Hurt</strong> - Johnny Cash</li>
            <li><strong>99 Problems</strong> - Jay-Z</li>
            <li><strong>Under the Bridge</strong> - Red Hot Chili Peppers</li>
            <li><strong>Chop Suey!</strong> - System of a Down</li>
        """,
        "impact": "Rubin has successfully produced for artists across metal, hip hop, rock, and country. His work with Johnny Cash on the 'American Recordings' series is legendary for revitalizing Cash's career."
    },
    {
        "filename": "quincy-jones.html",
        "name": "Quincy Jones",
        "subtitle": "The Titan of Music",
        "description": "Quincy Jones is a legendary producer, composer, and arranger, best known for his work with Michael Jackson on Thriller.",
        "intro": "Quincy Delight Jones Jr. is an American record producer, musician, songwriter, composer, arranger, and film and television producer. His career spans over 70 years in the entertainment industry.",
        "sound": "Quincy's sound is characterized by lush orchestration, impeccable jazz-influenced arrangements, and a groove that is undeniable. He is a master of blending genres, from big band to funk and pop.",
        "hits": """
            <li><strong>Billie Jean</strong> - Michael Jackson</li>
            <li><strong>Thriller</strong> - Michael Jackson</li>
            <li><strong>We Are the World</strong> - USA for Africa</li>
            <li><strong>Fly Me to the Moon</strong> - Frank Sinatra (Arrangement)</li>
            <li><strong>Give Me the Night</strong> - George Benson</li>
        """,
        "impact": "Producing 'Thriller', the best-selling album of all time, cements his legacy. He broke down racial barriers in the music industry and has won 28 Grammy Awards."
    },
    {
        "filename": "timbaland.html",
        "name": "Timbaland",
        "subtitle": "The Rhythm Innovator",
        "description": "Timbaland revolutionized R&B and Hip Hop with his unique stuttering drums and sampling style.",
        "intro": "Timothy Zachary Mosley, known professionally as Timbaland, is an American record producer, rapper, singer, and songwriter. He has received widespread acclaim for his production work.",
        "sound": "Timbaland's signature sound involves complex, syncopated drum patterns, beatboxing, and creative use of foreign samples and vocal grunts. He created a futuristic sound that defined the 2000s.",
        "hits": """
            <li><strong>Cry Me a River</strong> - Justin Timberlake</li>
            <li><strong>Get Ur Freak On</strong> - Missy Elliott</li>
            <li><strong>Promiscuous</strong> - Nelly Furtado</li>
            <li><strong>SexyBack</strong> - Justin Timberlake</li>
            <li><strong>Dirt Off Your Shoulder</strong> - Jay-Z</li>
        """,
        "impact": "His partnership with Missy Elliott and Justin Timberlake produced some of the most innovative pop and R&B tracks of the century. He proved that hip-hop beats could drive global pop smashes."
    },
    {
        "filename": "pharrell-williams.html",
        "name": "Pharrell Williams",
        "subtitle": "The Neptune Sound",
        "description": "Pharrell Williams, part of The Neptunes, brings a funk-infused, minimal, and infectious energy to his productions.",
        "intro": "Pharrell Lanscilo Williams is an American record producer, rapper, singer, and songwriter. Alongside Chad Hugo, he formed the hip hop and R&B production duo The Neptunes.",
        "sound": "The Neptunes' sound is instantly recognizable: dry, punchy drums, Korg Triton presets, specific guitar strums, and a four-count start. It's minimalist funk for the digital age.",
        "hits": """
            <li><strong>Happy</strong> - Pharrell Williams</li>
            <li><strong>Drop It Like It's Hot</strong> - Snoop Dogg</li>
            <li><strong>Hollaback Girl</strong> - Gwen Stefani</li>
            <li><strong>Hot in Herre</strong> - Nelly</li>
            <li><strong>Blurred Lines</strong> - Robin Thicke</li>
        """,
        "impact": "Pharrell redefined 'cool' in music and fashion. The Neptunes dominated radio in the early 2000s, producing hits for everyone from Britney Spears to Clipse."
    },
    {
        "filename": "dr-dre.html",
        "name": "Dr. Dre",
        "subtitle": "The West Coast Architect",
        "description": "Dr. Dre pioneered G-Funk and launched the careers of Eminem, Snoop Dogg, and 50 Cent.",
        "intro": "Andre Romelle Young, known professionally as Dr. Dre, is an American rapper, record producer, and entrepreneur. He is the founder and CEO of Aftermath Entertainment and Beats Electronics.",
        "sound": "G-Funk: slower tempos, deep basslines, whiny synthesizers (like the Moog), and soulful female backing vocals. Dre is a perfectionist known for the cleanest mixing in hip-hop.",
        "hits": """
            <li><strong>Nuthin' but a 'G' Thang</strong> - Dr. Dre ft. Snoop Dogg</li>
            <li><strong>Still D.R.E.</strong> - Dr. Dre ft. Snoop Dogg</li>
            <li><strong>In Da Club</strong> - 50 Cent</li>
            <li><strong>My Name Is</strong> - Eminem</li>
            <li><strong>California Love</strong> - 2Pac</li>
        """,
        "impact": "Dre not only created the G-Funk sound but also discovered diverse talents like Eminem and 50 Cent, proving he has the best ear for talent in the game."
    }
]

def generate_pages():
    os.makedirs('singer', exist_ok=True)
    
    cards_html = ""
    
    for producer in producers:
        # Generate individual page
        html_content = TEMPLATE.format(
            name=producer['name'],
            subtitle=producer['subtitle'],
            description=producer['description'],
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
        <div class="producer-card">
            <span class="role">Producer Profile</span>
            <h2>{producer['name']}</h2>
            <p>{producer['intro'][:120]}...</p>
            <a href="{producer['filename']}" class="read-more">Read Profile →</a>
        </div>
        """

    # Generate Index Page
    index_content = INDEX_TEMPLATE.format(cards=cards_html)
    with open('singer/index.html', 'w') as f:
        f.write(index_content)
    print("Generated singer/index.html")

if __name__ == "__main__":
    generate_pages()
