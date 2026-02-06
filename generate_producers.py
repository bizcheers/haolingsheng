import os

# Base template for producer pages
TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Music Producer Profile | Hao Ling Sheng</title>
    <meta name="description" content="{description}">
    <link rel="icon" type="image/png" href="../favicon.png">
    
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
            <div class="producer-intro">{intro}</div>
        </div>
    </div>

    <div class="container content-grid">
        <section class="feature-section signature-sound-box">
            <h3><div class="icon-box">🎛️</div> Signature Sound & Techniques</h3>
            <div class="rich-text">
                {sound}
            </div>
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
            <div class="rich-text">
                {impact}
            </div>
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
    <link rel="icon" type="image/png" href="../favicon.png">
    
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
        "intro": """
            <p>Karl Martin Sandberg, better known as <strong>Max Martin</strong>, is arguably the most successful songwriter and producer of the last three decades. With over <strong>25 Billboard Hot 100 number-one hits</strong> to his name—trailing only Paul McCartney and John Lennon—Martin has single-handedly sculpted the sound of modern pop radio.</p>
            <p>Emerging from the Swedish glam metal scene of the 80s (as the frontman for <em>It's Alive</em>), Martin was mentored by the legendary producer Denniz Pop at Cheiron Studios. There, he transitioned from rock to pop, bringing a rock musician's ear for power and dynamics into the realm of dance-pop. His work spans generations, from the bubblegum pop of <strong>Britney Spears</strong> and <strong>Backstreet Boys</strong> in the late 90s to the polished rock-pop of <strong>Kelly Clarkson</strong> and <strong>P!nk</strong>, and onto the modern synth-pop dominance of <strong>Taylor Swift</strong>, <strong>The Weeknd</strong>, and <strong>Ariana Grande</strong>.</p>
            <p>Unlike many producers who fade as trends shift, Martin has remained at the pinnacle of the industry by constantly adapting his sound while maintaining his core philosophy: <strong>Melody is King.</strong></p>
        """,
        "sound": """
            <h4>The Theory of "Melodic Math"</h4>
            <p>Max Martin's production philosophy is often described as "Melodic Math." This isn't about formulaic rigidity, but rather a deep understanding of listener psychology. He believes a song must capture the listener's attention immediately and never let go. His tracks are meticulously structured so that there is a new melodic or hook element every 7 seconds—the average human attention span for passive listening.</p>
            
            <h4>Technical Trademarks</h4>
            <ul>
                <li><strong>Comping Intensity:</strong> Martin is famous for his rigorous vocal comping. A single lead vocal track might be sewn together from dozens of different takes to ensure every syllable has the perfect pitch, tone, and rhythmic attack.</li>
                <li><strong>The "Pop" Song Structure:</strong> He strictly adheres to traditional song structures (Verse-Chorus-Verse-Chorus-Bridge-Chorus), often shortening intro lengths significantly to get to the vocal as fast as possible.</li>
                <li><strong>Wall of Sound Layers:</strong> Borrowing from his rock background, he treats synths like distorted guitars. Choruses often feature massive, stacked chords (Super Saws or layered pads) that provide a sudden burst of energy and width compared to the verses.</li>
                <li><strong>Melody Over Lyrics:</strong> Martin famously prioritizes the phonetic sound of words over their grammatical correctness. If a word sounds better sung a certain way, grammar is ignored (e.g., "Hit me baby one more time" or "I want it that way," which are grammatically ambiguous but phonetically punchy).</li>
            </ul>

            <h4>Key Gear Usage</h4>
            <p>In his early Cheiron days, the <strong>Juno-106</strong> and <strong>Pro Tools</strong> became his weapons of choice. He was one of the earliest adopters of hybrid digital/analog workflows. Today, while his studios are state-of-the-art, he still relies on simple, catchy motifs often written on a piano or acoustic guitar before any production begins. He uses <strong>Melodyne</strong> extensively not just for pitch correction, but to rewrite melodies after the fact, treating audio like MIDI.</p>
        """,
        "hits": """
            <li><span class="track-name">...Baby One More Time</span> <span class="artist-name">Britney Spears</span></li>
            <li><span class="track-name">I Want It That Way</span> <span class="artist-name">Backstreet Boys</span></li>
            <li><span class="track-name">It's My Life</span> <span class="artist-name">Bon Jovi</span></li>
            <li><span class="track-name">Shake It Off</span> <span class="artist-name">Taylor Swift</span></li>
            <li><span class="track-name">Blinding Lights</span> <span class="artist-name">The Weeknd</span></li>
            <li><span class="track-name">Can't Stop the Feeling!</span> <span class="artist-name">Justin Timberlake</span></li>
            <li><span class="track-name">Roar</span> <span class="artist-name">Katy Perry</span></li>
        """,
        "impact": """
            <h4>The "Swedish Music Miracle"</h4>
            <p>Max Martin is the central figure of the "Swedish Music Miracle," a phenomenon where a small nation became the world's third-largest exporter of music. He established a lineage of mentorship that has produced fellow titans like <strong>Shellback</strong>, <strong>Benny Blanco</strong>, and <strong>Savan Kotecha</strong>. His studio operates like a collaborative compound, where ideas are shared freely, removing the ego from the creative process.</p>
            
            <h4>Redefining the Producer's Role</h4>
            <p>Before Martin, producers were often seen as technicians or vibe-setters. Martin re-established the producer as the <em>primary songwriter</em>. He proved that the "track" and the "song" are inseparable in modern music. His influence is so vast that for the last 25 years, if you turned on Top 40 radio at any random moment, there was a statistically high chance you were listening to a song written or produced by him or his disciples.</p>
        """
    },
    {
        "filename": "rick-rubin.html",
        "name": "Rick Rubin",
        "role": "Minimalist Visionary",
        "subtitle": "The Zen Master of Reduction",
        "description": "Rick Rubin's production style focuses on stripping away the unnecessary to reveal the raw emotion of the artist.",
        "intro": """
            <p><strong>Rick Rubin</strong> is an anomaly in the music world. He doesn't play instruments. He doesn't touch a mixing board. He often lays on a couch during sessions with his eyes closed. Yet, he is arguably the most important producer for bringing raw authenticity back to music. Co-founder of <strong>Def Jam Recordings</strong>, Rubin revolutionized hip-hop in the 80s by removing the disco/funk band elements and focusing on the raw drum machine and DJ scratching.</p>
            <p>His career is defined by his ability to transcend genres. He took hip-hop to the suburbs with the <strong>Beastie Boys</strong> and <strong>Run-D.M.C.</strong>, defined thrash metal production with <strong>Slayer</strong>, and resurrected <strong>Johnny Cash's</strong> career when Nashville had written him off. Rubin sees himself not as a "producer" in the technical sense, but as a "reducer"—someone who strips away the artifice to reveal the pure essence of the song and the artist.</p>
        """,
        "sound": """
            <h4>The Art of Reduction</h4>
            <p>Rubin's signature is the absence of signature. Unlike Timbaland's distinct drums or Max Martin's polished synths, a Rick Rubin track is defined by what isn't there. He famously says, "I try to get the artist to be naked."</p>

            <h4>Production Philosophy</h4>
            <ul>
                <li><strong>Dry and In-Your-Face:</strong> In the reverb-soaked 80s, Rubin went the opposite direction. On Slayer's <em>Reign in Blood</em> and Run-D.M.C.'s <em>Raising Hell</em>, he removed almost all reverb. The drums are bone-dry, hitting the listener directly in the chest. This creates an immediate, confrontational aggressive sound.</li>
                <li><strong>No "Bumper Cards":</strong> Rubin dislikes "production tricks" that smooth over mistakes. If a band is playing, he wants to hear the band in the room. He often records acts playing live together rather than overdubbing individually, capturing the "push and pull" of human timing.</li>
                <li><strong>Genre Agnosticism:</strong> He applies the same philosophy to every genre. For hip-hop, it was "just the beat and the rhyme." For Johnny Cash, it was "just the man and the guitar." For Adele, it was "just the voice and the piano." He believes that if the core song is good enough, it needs no decoration.</li>
            </ul>

            <h4>The "Loudness War" Controversy</h4>
            <p>Rubin has been a central figure in the "Loudness War"—the trend of mastering albums to be as loud as physically possible, often at the expense of dynamic range. His work on Red Hot Chili Peppers' <em>Californication</em> and Metallica's <em>Death Magnetic</em> drew criticism for audible digital clipping specifically to achieve maximum impact. While controversial, it underscores his obsession with "impact" and "feeling" over technical perfection.</p>
        """,
        "hits": """
            <li><span class="track-name">Walk This Way</span> <span class="artist-name">Run-D.M.C. ft. Aerosmith</span></li>
            <li><span class="track-name">Fight For Your Right</span> <span class="artist-name">Beastie Boys</span></li>
            <li><span class="track-name">Hurt</span> <span class="artist-name">Johnny Cash</span></li>
            <li><span class="track-name">Under the Bridge</span> <span class="artist-name">Red Hot Chili Peppers</span></li>
            <li><span class="track-name">99 Problems</span> <span class="artist-name">Jay-Z</span></li>
            <li><span class="track-name">Chop Suey!</span> <span class="artist-name">System of a Down</span></li>
        """,
        "impact": """
            <h4>The Def Jam Legacy</h4>
            <p>By founding Def Jam in his NYU dorm room, Rubin legitimized hip-hop as a global force. He bridged the gap between rock and rap (Run-D.M.C. + Aerosmith), creating the blueprint for rap-rock that would dominate the late 90s.</p>

            <h4>The Guru Figure</h4>
            <p>Rubin's impact today is almost spiritual. Artists go to his Shangri-La studio not just to record, but to be "healed" creatively. His book, <em>The Creative Act: A Way of Being</em>, has codified his philosophy that art is a practice of observation and tuning into the universe. He proved that a producer's greatest tool is their taste and their ability to create a safe environment for vulnerability.</p>
        """
    },
    {
        "filename": "quincy-jones.html",
        "name": "Quincy Jones",
        "role": "The Maestro",
        "subtitle": "The Titan of Music",
        "description": "Quincy Jones is a legendary producer, composer, and arranger, best known for his work with Michael Jackson on Thriller.",
        "intro": """
            <p><strong>Quincy Jones</strong> is the bridge between the 20th-century jazz orchestra and the modern pop blockbuster. With a career spanning over 70 years and 28 Grammy Awards, "Q" has done it all: touring trumpeter used by Ray Charles and Elvis Presley, a film composer, a big band arranger, and the producer of the best-selling album of all time, Michael Jackson's <em>Thriller</em>.</p>
            <p>Jones brought a level of harmonic sophistication and orchestrational complexity to pop music that had simply never existed before. He treated a pop song like a film score, where every instrument, from the rhythmic breathing to the shaker, had a specifically noted place in the frequency spectrum. He is the ultimate "Arranger-Producer," proving that technical discipline and popular appeal are not mutually exclusive.</p>
        """,
        "sound": """
            <h4>The "Acusonic" Approach</h4>
            <p>Working with his longtime engineer <strong>Bruce Swedien</strong>, Jones pioneered the "Acusonic Recording Process." This involved synchronizing multiple 24-track tape machines to allow for virtually unlimited overdubbing while maintaining pristine fidelity. This allowed them to record hundreds of vocal takes for Michael Jackson's harmonies, creating a incredibly lush, wide stereo image that still stands as the benchmark for mixing.</p>

            <h4>Technical Mastery</h4>
            <ul>
                <li><strong>Syncopation & Groove:</strong> Coming from a Jazz background, Q understood swing. The basslines in his productions (often played by Louis Johnson) are never just "on the grid." They sit in a specific "pocket" that forces the body to move. The iconic bassline on "Billie Jean" is a masterclass in tension and release.</li>
                <li><strong>Genre Fusion:</strong> Jones fearlessly blended genres. On "Beat It," he hired Eddie Van Halen for the solo to merge Hard Rock with R&B. On "Thriller," he used Vincent Price for a theatrical spoken word. He treated the studio as a casting agency, bringing in the absolute best specialist for each specific sound.</li>
                <li><strong>Dynamic Range:</strong> Unlike modern compressed mixes, Jones' productions have massive dynamic range. The punch of the snare drum on a Quincy Jones record hits hard because he left room for it. He famously said, "If you don't have dynamics, you don't have music."</li>
            </ul>

            <h4>Arrangement as Production</h4>
            <p>Quincy didn't just loop a beat. He <em>wrote</em> every part. If you listen to the horn sections in "Rock with You" or the string swells in "Human Nature," you are hearing advanced jazz voicings applied to pop loops. He understood how to voice chords so they didn't clash with the vocal, using counter-melody to keep the listener engaged during gaps in the singing.</p>
        """,
        "hits": """
            <li><span class="track-name">Billie Jean</span> <span class="artist-name">Michael Jackson</span></li>
            <li><span class="track-name">Thriller</span> <span class="artist-name">Michael Jackson</span></li>
            <li><span class="track-name">We Are the World</span> <span class="artist-name">USA for Africa</span></li>
            <li><span class="track-name">Fly Me to the Moon</span> <span class="artist-name">Frank Sinatra (Arrangement)</span></li>
            <li><span class="track-name">Give Me the Night</span> <span class="artist-name">George Benson</span></li>
            <li><span class="track-name">Soul Bossa Nova</span> <span class="artist-name">Quincy Jones</span></li>
        """,
        "impact": """
            <h4>Breaking Barriers</h4>
            <p>Quincy Jones broke down the walls between "Black music" and "White music." Before <em>Thriller</em>, MTV refused to play black artists. The undeniable quality of Jones' production forced them to air it, integrating the music industry forever. He became the first African American high-level executive at a major record label (Mercury Records).</p>

            <h4>The Blueprint for the "Super-Producer"</h4>
            <p>Jones was the prototype for the modern super-producer mogul. He showed that a producer could be a star in their own right. His work on "We Are The World," managing dozens of distinct starry egos in one room ("Check your ego at the door" was his sign), demonstrated that producing is as much about people management as it is about music theory.</p>
        """
    },
    {
        "filename": "timbaland.html",
        "name": "Timbaland",
        "role": "Rhythm Innovator",
        "subtitle": "The Beat Magician",
        "description": "Timbaland revolutionized R&B and Hip Hop with his unique stuttering drums and sampling style.",
        "intro": """
            <p><strong>Timbaland</strong> (Timothy Mosley) is the sonic architect who defined the sound of the 2000s. Alongside his childhood friend Missy Elliott, and later Justin Timberlake, he took R&B and Hip-Hop and injected it with a futuristic, avant-garde weirdness that somehow became massive pop success. If Max Martin is "Melodic Math," Timbaland is "Rhythmic Chaos."</p>
            <p>Before Timbaland, hip-hop production was largely based on looping funk breaks (like James Brown). Timbaland threw that out the window. He built beats from scratch using bizarre sounds—babies crying, crickets chirping, intricate beatboxing, and Egyptian flutes—creating a stuttering, syncopated bounce that was instantly recognizable and impossible to copy.</p>
        """,
        "sound": """
            <h4>The "Stutter" and Syncopation</h4>
            <p>Timbaland's drums are never straightforward. He popularized <strong>double-time drum patterns</strong> (hi-hats moving twice as fast as the beat) over slow, grinding grooves. He heavily uses <strong>triplets</strong> and 32nd notes in his hi-hat rolls, a technique that would later influence the entire Trap music genre. His kick drums often land on unexpected off-beats, creating a jerky, funk-infused rhythm that forces dancers to adapt.</p>

            <h4>Beatboxing as Percussion</h4>
            <p>A unique trademark of Timbaland is his use of his own voice as a percussion instrument. On tracks like Aaliyah's "Are You That Somebody?", the backing rhythm is largely composed of him beatboxing, gasping, and making percussive mouth sounds, layered with real drums. This gave his tracks a human, organic feel despite their electronic nature.</p>

            <h4>Creative Sampling & The ASR-10</h4>
            <p>Timbaland was a master of the <strong>Ensoniq ASR-10</strong> sampler. He would take ordinary presets or samples of Middle Eastern and Asian records (World Music) and pitch-shift/timestretch them into unrecognizable textures. The flute on "Big Pimpin'" or the strings on "Get Ur Freak On" introduced global sounds to American urban radio, creating a cross-cultural fusion that sounded like it came from the year 3000.</p>
        """,
        "hits": """
            <li><span class="track-name">Cry Me a River</span> <span class="artist-name">Justin Timberlake</span></li>
            <li><span class="track-name">Get Ur Freak On</span> <span class="artist-name">Missy Elliott</span></li>
            <li><span class="track-name">Pony</span> <span class="artist-name">Ginuwine</span></li>
            <li><span class="track-name">Promiscuous</span> <span class="artist-name">Nelly Furtado</span></li>
            <li><span class="track-name">Dirt Off Your Shoulder</span> <span class="artist-name">Jay-Z</span></li>
            <li><span class="track-name">SexyBack</span> <span class="artist-name">Justin Timberlake</span></li>
        """,
        "impact": """
            <h4>Shifting the Center of Pop</h4>
            <p>Timbaland was instrumental in shifting the center of Pop music towards R&B. His work on Justin Timberlake's <em>FutureSex/LoveSounds</em> proved that a pop "boy band" star could make credible, edgy, experimental urban music. This album laid the groundwork for the genre-blurring pop landscape we see today.</p>

            <h4>Influence on Modern Trap</h4>
            <p>While often uncredited, Timbaland's use of rapid-fire hi-hat rolls and heavy 808 sub-bass in the late 90s (on tracks for Ginuwine and Aaliyah) is the direct ancestor of modern Trap production. Producers like Metro Boomin and Pierre Bourne stand on the shoulders of the rhythmic complexities Timbaland introduced to potential radio hits.</p>
        """
    },
    {
        "filename": "pharrell-williams.html",
        "name": "Pharrell Williams",
        "role": "The Hitmaker",
        "subtitle": "The Neptune Sound",
        "description": "Pharrell Williams, part of The Neptunes, brings a funk-infused, minimal, and infectious energy to his productions.",
        "intro": """
            <p><strong>Pharrell Williams</strong> is the definition of "cool." As one half of the production duo <strong>The Neptunes</strong> (with Chad Hugo), he dominated the early 2000s radio waves with a sound that was stark, dry, and impossibly funky. While other producers were adding more layers, Pharrell was taking them away.</p>
            <p>He is a true polymath: producer, rapper, singer, fashion designer, and cultural icon. His production style merges the raw energy of skate-punk, the chord progressions of Stevie Wonder-era soul, and the knocking drums of boom-bap hip-hop. Whether producing for Jay-Z, Britney Spears, or Daft Punk, Pharrell's fingerprints—specifically his four-count intros—are unmistakable.</p>
        """,
        "sound": """
            <h4>The "Neptunes Sound"</h4>
            <p>The core of Pharrell's production is <strong>minimalism</strong>. A typical Neptunes track often consists of only three variance elements: a thunderous, dry kick drum; a crisp, high-pitched snare; and a single, repetitive synth or guitar riff. This creates a massive amount of "sonic space" for the vocalist.</p>

            <h4>Technical Trademarks</h4>
            <ul>
                <li><strong>The Four-Count Start:</strong> Almost every Pharrell track begins with a four-beat loop of the first beat (1-2-3-4-Drop). This was originally done to ensure radio DJs knew exactly when the song started, but it became his audio signature tag.</li>
                <li><strong>Korg Triton & Clavichords:</strong> Pharrell heavily utilized the "preset" sounds of the Korg Triton, particularly the rock guitar emulation, bass plucks, and clavichords. He played these rigid digital sounds with a loose, funky jazz timing, creating a unique tension between "fake" sounds and "real" feeling.</li>
                <li><strong>Falsetto Harmonies:</strong> Influenced by Curtis Mayfield and Earth, Wind & Fire, Pharrell frequently arranges background vocals in tight, falsetto clusters. He often sings the hooks himself, adding a silky, smooth texture over his jagged, hard-hitting beats.</li>
                <li><strong>Unexpected Bridges:</strong> Pharrell is a master of the "left-turn" bridge. Just when a song feels repetitive, he will drop into a completely different chord progression, often incorporating jazz chords (7ths, 9ths, 13ths) that elevate a simple rap song into a musical composition.</li>
            </ul>
        """,
        "hits": """
            <li><span class="track-name">Happy</span> <span class="artist-name">Pharrell Williams</span></li>
            <li><span class="track-name">Drop It Like It's Hot</span> <span class="artist-name">Snoop Dogg</span></li>
            <li><span class="track-name">Hollaback Girl</span> <span class="artist-name">Gwen Stefani</span></li>
            <li><span class="track-name">Hot in Herre</span> <span class="artist-name">Nelly</span></li>
            <li><span class="track-name">Get Lucky</span> <span class="artist-name">Daft Punk</span></li>
            <li><span class="track-name">I'm A Slave 4 U</span> <span class="artist-name">Britney Spears</span></li>
        """,
        "impact": """
            <h4>Genre-Bending & Aesthetics</h4>
            <p>Pharrell was the first hip-hop producer to truly embrace the "skater" and "rock" aesthetic, breaking the stereotype of what a hip-hop producer should look and sound like. His band N.E.R.D. fused rock, funk, and rap years before it became common.</p>

            <h4>Longevity & Reinvention</h4>
            <p>Pharrell has effortlessly reinvented himself multiple times.From the gritty hip-hop of The Clipse ("Grindin'"), to the pop explosion of Gwen Stefani ("Hollaback Girl"), to the disco-revival of Daft Punk ("Get Lucky"), and finally to "Happy"—one of the best-selling singles of all time. He proved that a producer can be a frontman, a fashion mogul, and an artist simultaneously.</p>
        """
    },
    {
        "filename": "dr-dre.html",
        "name": "Dr. Dre",
        "role": "Hip-Hop Icon",
        "subtitle": "The West Coast Architect",
        "description": "Dr. Dre pioneered G-Funk and launched the careers of Eminem, Snoop Dogg, and 50 Cent.",
        "intro": """
            <p><strong>Dr. Dre</strong> (Andre Young) is widely considered the greatest hip-hop perfectionist of all time. He didn't just produce songs; he built entire dynasties (N.W.A., Death Row, Aftermath). Dre single-handedly defined the sound of West Coast Hip-Hop with <strong>G-Funk</strong>, a lazy, hazy, synthesizer-heavy sound inspired by George Clinton's P-Funk.</p>
            <p>Dre's reputation is built on quality over quantity. He releases music rarely (his album <em>Detox</em> was scrapped after a decade of work), but when he does, it shifts the entire axis of the culture. He discovered and molded superstars like <strong>Snoop Dogg</strong>, <strong>Eminem</strong>, <strong>50 Cent</strong>, and <strong>Kendrick Lamar</strong>, proving his ear for talent is as legendary as his mixing desk skills.</p>
        """,
        "sound": """
            <h4>The G-Funk Blueprint</h4>
            <p>G-Funk is characterized by slow, rolling tempos (around 90-95 BPM), deep sub-bass lines, and high-pitched, portamento synthesizer melodies (often a MiniMoog or SE-1) known as the "worm." This sound was designed for driving in Los Angeles—music to be felt in a car system.</p>

            <h4>Sonic Perfectionism (The "Dre Mix")</h4>
            <p>Dr. Dre is notorious for his mixing standards. A "Dre Mix" is the industry gold standard for clarity and low-end weight.</p>
            <ul>
                <li><strong>The Low End:</strong> Dre spends days just on the kick drum and bass relationship. He sculps the frequencies so they never clash, creating a physical "thump" that hits harder than any other record.</li>
                <li><strong>Live Replaying:</strong> Unlike East Coast producers who looped gritty samples from vinyl, Dre preferred to hire world-class session musicians to <em>replay</em> the samples. This allowed him to have clean, isolated audio stems (bass, keys, guitar) that he could mix with modern fidelity, avoiding the static/noise of old records while keeping the musical vibe.</li>
                <li><strong>MPC3000 Swing:</strong> His drum programming on the Akai MPC3000 is legendary for its swing. It's rigid enough to nod to, but human enough to groove.</li>
                <li><strong>The "Movie" Scope:</strong> Dre treats albums like cinematic experiences. He uses skits, sound effects (gunshots, car engines, sirens), and meticulous panning to create an immersive audio landscape.</li>
            </ul>
        """,
        "hits": """
            <li><span class="track-name">Nuthin' but a 'G' Thang</span> <span class="artist-name">Dr. Dre ft. Snoop Dogg</span></li>
            <li><span class="track-name">Still D.R.E.</span> <span class="artist-name">Dr. Dre ft. Snoop Dogg</span></li>
            <li><span class="track-name">In Da Club</span> <span class="artist-name">50 Cent</span></li>
            <li><span class="track-name">My Name Is</span> <span class="artist-name">Eminem</span></li>
            <li><span class="track-name">California Love</span> <span class="artist-name">2Pac</span></li>
            <li><span class="track-name">Family Affair</span> <span class="artist-name">Mary J. Blige</span></li>
        """,
        "impact": """
            <h4>The Business of Audio</h4>
            <p>Beyond music, Dre revolutionized the way music is consumed. By founding <strong>Beats by Dre</strong>, he convinced a generation of listeners to care about audio quality (or at least, the perception of bass) again, creating the first mass-market premium headphone brand. This acquisition by Apple made him the first billionaire in hip-hop.</p>

            <h4>The "Co-Sign" King</h4>
            <p>Dre's greatest legacy might be his family tree. He didn't just make beats; he taught his artists how to structure songs, how to deliver vocals, and how to become stars. Eminem, 50 Cent, The Game, and Kendrick Lamar all accredit their discipline and work ethic to Dr. Dre's boot camp.</p>
        """
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
                <div class="card-intro">{producer['description']}</div>
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
