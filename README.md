# Hao Ling Sheng - Free Music Education Website

A static HTML website providing free sheet music, music theory tutorials, and instrument learning resources. All content is based on public domain music to ensure AdSense compliance and avoid copyright issues.

## 🎯 Project Goals

- Provide high-quality, free music education resources
- Generate AdSense revenue through educational content
- Avoid copyright issues by using only public domain music
- Create hundreds of SEO-optimized static HTML pages
- Maintain existing domain authority (DR 60) for haolingsheng.com

## 📁 Project Structure

```
haolingsheng/
├── index.html              # Homepage
├── styles.css              # Main stylesheet
├── sheet-music/            # Sheet music section
│   ├── piano/              # Piano music
│   ├── guitar/             # Guitar tabs
│   ├── violin/             # Violin music
│   ├── flute/              # Flute music
│   └── sheet-detail.css    # Detail page styles
├── music-theory/           # Music theory tutorials
├── instruments/            # Instrument learning guides
├── data/                   # CSV data files
│   └── sample-sheet-music.csv
├── generate.py             # HTML page generator script
└── README.md              # This file
```

## 🚀 Quick Start

### View Sample Pages

1. Open `index.html` in your browser to see the homepage
2. Open `sheet-music/piano/beethoven-moonlight-sonata.html` to see a detailed sheet music page

### Generate Pages from CSV Data

1. **Prepare your CSV file** with the following columns:
   - piece_name
   - full_title
   - composer
   - composer_years
   - opus
   - instrument
   - genre
   - difficulty
   - duration
   - pages
   - preview_note
   - meta_description
   - keywords
   - content
   - practice_tips

2. **Edit generate.py** to specify your CSV file and output directory:
   ```python
   generate_sheet_music_pages('data/your-data.csv', 'sheet-music/piano/')
   ```

3. **Run the generator**:
   ```bash
   python3 generate.py
   ```

## 📊 Content Strategy

### Sheet Music Categories

- **Piano**: Classical pieces, exercises, popular songs
- **Guitar**: Tabs, chord charts, fingerstyle arrangements
- **Violin**: Classical repertoire, folk songs
- **Flute**: Beginner to advanced pieces

### Music Theory Topics

- Scales and modes
- Chord theory
- Rhythm and timing
- Harmony and composition
- Music notation

### Target Keywords

- "free sheet music"
- "piano music pdf"
- "guitar tabs"
- "music theory basics"
- "learn [instrument]"

## 💰 AdSense Optimization

### Ad Placements

Each page includes 3-4 ad placements:
1. Below hero section (728x90 leaderboard)
2. Mid-content (336x280 rectangle)
3. Bottom of content (728x90 leaderboard)
4. Sidebar (300x250 rectangle)

### Content Guidelines

✅ **Do:**
- Use public domain music (pre-1928 or explicitly public domain)
- Create original educational content
- Provide detailed music theory explanations
- Include practice tips and historical context

❌ **Don't:**
- Use copyrighted song lyrics
- Provide copyrighted sheet music
- Include download links to copyrighted material
- Copy content from other websites

## 🎵 Public Domain Music Sources

### Composers (Life+70 years rule)

- Johann Sebastian Bach (1685-1750)
- Wolfgang Amadeus Mozart (1756-1791)
- Ludwig van Beethoven (1770-1827)
- Frédéric Chopin (1810-1849)
- Franz Schubert (1797-1828)
- Traditional folk songs

### Resources

- IMSLP (International Music Score Library Project)
- Musopen
- Public Domain 4U
- Traditional folk music collections

## 🔧 Customization

### Modify Styles

Edit `styles.css` and `sheet-music/sheet-detail.css` to customize:
- Colors (CSS variables in `:root`)
- Fonts
- Layout
- Responsive breakpoints

### Add New Instruments

1. Create directory: `sheet-music/[instrument]/`
2. Update navigation in templates
3. Create index page for the instrument
4. Add CSV data for pieces

### Extend Generator

The `generate.py` script can be extended to:
- Generate music theory pages
- Create instrument guide pages
- Build sitemap.xml
- Generate category index pages

## 📈 SEO Best Practices

### On-Page SEO

- ✅ Unique, descriptive titles (under 60 characters)
- ✅ Meta descriptions (150-160 characters)
- ✅ Header hierarchy (H1 → H2 → H3)
- ✅ Internal linking
- ✅ Breadcrumb navigation
- ✅ Mobile-responsive design
- ✅ Fast loading (static HTML)

### Content SEO

- ✅ Original, valuable content (500+ words per page)
- ✅ Keyword optimization (natural placement)
- ✅ Related content suggestions
- ✅ Educational focus

## 🌐 Deployment

### Option 1: Free Hosting + Cloudflare

1. **Choose a free PHP host** (even though site is static):
   - InfinityFree
   - 000webhost
   - Awardspace

2. **Upload files** via FTP

3. **Configure Cloudflare**:
   - Add domain to Cloudflare
   - Update nameservers
   - Enable proxy (orange cloud)
   - Configure security rules

### Option 2: GitHub Pages

1. Create GitHub repository
2. Push files to `main` branch
3. Enable GitHub Pages in settings
4. Point domain to GitHub Pages

### Option 3: Netlify/Vercel

1. Connect repository
2. Deploy automatically
3. Configure custom domain

## 📝 Next Steps

### Phase 1: Content Creation (Week 1-2)
- [ ] Generate 100 piano sheet music pages
- [ ] Generate 100 guitar tab pages
- [ ] Create 50 music theory pages
- [ ] Write instrument learning guides

### Phase 2: SEO Optimization (Week 3)
- [ ] Generate sitemap.xml
- [ ] Create robots.txt
- [ ] Submit to Google Search Console
- [ ] Build internal linking structure

### Phase 3: AdSense Application (Week 4)
- [ ] Ensure 30+ high-quality pages
- [ ] Add privacy policy and terms pages
- [ ] Apply for AdSense
- [ ] Implement ad code once approved

### Phase 4: Expansion (Ongoing)
- [ ] Add more instruments (cello, clarinet, etc.)
- [ ] Create video tutorials
- [ ] Build music tools (metronome, tuner)
- [ ] Develop blog section

## 🤝 Contributing

This is a personal project, but suggestions are welcome!

## 📄 License

All code is provided as-is for educational purposes. Sheet music content must be verified as public domain before use.

---

**Note**: Always verify that music is in the public domain in your jurisdiction before publishing. When in doubt, consult with a legal professional.
