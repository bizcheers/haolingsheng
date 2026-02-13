#!/usr/bin/env python3
"""
Add strategic internal links to articles based on topic clusters.
Each article gets 2 contextual internal links to related content.
EXPANDED VERSION - covers 80+ articles
"""

import os
import re
from pathlib import Path

# Define topic clusters and their related articles
TOPIC_CLUSTERS = {
    # ===== AI MUSIC TOOLS CLUSTER =====
    'music-production/udio-ai-music-guide.html': [
        ('music-production/suno-vs-udio-2026.html', 'Suno vs Udio comparison'),
        ('music-production/top-ai-production-tools-2026.html', 'top AI production tools')
    ],
    'music-production/stable-audio-guide.html': [
        ('music-production/top-ai-production-tools-2026.html', 'AI production tools'),
        ('music-production/ai-audio-separation-guide.html', 'AI audio separation')
    ],
    'music-production/vocal-synthesis-guide.html': [
        ('music-production/auto-tune-vs-pitch-correction.html', 'Auto-Tune vs pitch correction'),
        ('music-production/vocal-production-masterclass.html', 'vocal production techniques')
    ],
    'music-production/ai-audio-separation-guide.html': [
        ('music-production/stable-audio-guide.html', 'Stable Audio guide'),
        ('music-production/top-ai-production-tools-2026.html', 'AI production tools')
    ],
    'music-production/ai-mixing-workflow.html': [
        ('music-production/ai-mastering-tools-comparison.html', 'AI mastering tools'),
        ('music-production/compression-basics-guide.html', 'compression basics')
    ],
    'music-production/top-ai-production-tools-2026.html': [
        ('music-production/suno-vs-udio-2026.html', 'Suno vs Udio'),
        ('music-business/ai-music-copyright-guide.html', 'AI music copyright')
    ],
    
    # ===== DAW WORKFLOW CLUSTER =====
    'music-production/what-is-daw.html': [
        ('music-production/ableton-vs-fl-studio-comparison.html', 'Ableton vs FL Studio'),
        ('music-production/best-audio-interfaces-2026.html', 'best audio interfaces')
    ],
    'music-production/best-fl-studio-plugins.html': [
        ('music-production/fl-studio-selection-guide.html', 'FL Studio selection guide'),
        ('music-production/free-vst-plugins-guide.html', 'free VST plugins')
    ],
    'music-production/ableton-shortcuts-cheat-sheet.html': [
        ('music-production/ableton-vs-fl-studio-comparison.html', 'Ableton vs FL Studio'),
        ('music-production/ableton-sharps-to-flats.html', 'sharps to flats in Ableton')
    ],
    'music-production/serum-for-ableton-guide.html': [
        ('music-production/what-is-lfo.html', 'LFO basics'),
        ('music-production/ableton-shortcuts-cheat-sheet.html', 'Ableton shortcuts')
    ],
    'music-production/what-is-lfo.html': [
        ('music-production/serum-for-ableton-guide.html', 'Serum for Ableton'),
        ('music-production/what-is-daw.html', 'DAW basics')
    ],
    
    # ===== MIXING TECHNIQUES CLUSTER =====
    'music-production/kick-drum-eq-guide.html': [
        ('music-production/eq-basics-guide.html', 'EQ basics'),
        ('music-production/sub-bass-vs-mid-bass-guide.html', 'sub-bass mixing')
    ],
    'music-production/phase-cancellation-explained.html': [
        ('music-production/soothe-2-mixing-guide.html', 'Soothe 2 guide'),
        ('music-production/stereo-imaging-guide.html', 'stereo imaging')
    ],
    'music-production/what-is-mix-bus.html': [
        ('music-production/compression-basics-guide.html', 'compression basics'),
        ('music-production/mastering-chain-basics.html', 'mastering chain')
    ],
    'music-production/saturation-and-distortion-guide.html': [
        ('music-production/compression-basics-guide.html', 'compression basics'),
        ('music-production/reference-tracks-mastery.html', 'reference tracks')
    ],
    'music-production/reference-tracks-mastery.html': [
        ('music-production/how-many-lufs-mastering-guide.html', 'LUFS standards'),
        ('music-production/mastering-chain-basics.html', 'mastering chain')
    ],
    'music-production/sub-bass-vs-mid-bass-guide.html': [
        ('music-production/multiband-compression-guide.html', 'multiband compression'),
        ('music-production/kick-drum-eq-guide.html', 'kick drum EQ')
    ],
    'music-production/stereo-imaging-guide.html': [
        ('music-production/phase-cancellation-explained.html', 'phase cancellation'),
        ('music-production/reverb-and-delay-guide.html', 'reverb and delay')
    ],
    'music-production/reverb-and-delay-guide.html': [
        ('music-production/stereo-imaging-guide.html', 'stereo imaging'),
        ('music-production/automation-techniques-guide.html', 'automation techniques')
    ],
    'music-production/automation-techniques-guide.html': [
        ('music-production/reverb-and-delay-guide.html', 'reverb and delay'),
        ('music-production/transitions-and-ear-candy-guide.html', 'transitions and ear candy')
    ],
    'music-production/transitions-and-ear-candy-guide.html': [
        ('music-production/automation-techniques-guide.html', 'automation techniques'),
        ('music-production/gross-beat-tape-stop-guide.html', 'tape stop effects')
    ],
    
    # ===== VOCAL PRODUCTION CLUSTER =====
    'music-production/vocal-production-masterclass.html': [
        ('music-production/auto-tune-vs-pitch-correction.html', 'Auto-Tune vs pitch correction'),
        ('music-production/vocal-doubling-and-layering.html', 'vocal doubling techniques')
    ],
    'music-production/auto-tune-vs-pitch-correction.html': [
        ('music-production/vocal-production-masterclass.html', 'vocal production masterclass'),
        ('music-production/vocal-synthesis-guide.html', 'AI vocal synthesis')
    ],
    'music-production/vocal-doubling-and-layering.html': [
        ('music-production/vocal-production-masterclass.html', 'vocal production techniques'),
        ('music-production/home-vocal-recording-guide.html', 'home vocal recording')
    ],
    'music-production/home-vocal-recording-guide.html': [
        ('music-production/vocal-doubling-and-layering.html', 'vocal layering'),
        ('music-production/best-audio-interfaces-2026.html', 'best audio interfaces')
    ],
    'music-production/vocal-comping-mastery.html': [
        ('music-production/vocal-production-masterclass.html', 'vocal production'),
        ('music-production/auto-tune-vs-pitch-correction.html', 'pitch correction')
    ],
    
    # ===== MASTERING CLUSTER =====
    'music-production/mastering-chain-basics.html': [
        ('music-production/how-many-lufs-mastering-guide.html', 'LUFS standards'),
        ('music-production/reference-tracks-mastery.html', 'reference tracks')
    ],
    'music-production/how-many-lufs-mastering-guide.html': [
        ('music-production/mastering-chain-basics.html', 'mastering chain'),
        ('music-production/ai-mastering-tools-comparison.html', 'AI mastering tools')
    ],
    'music-production/auditory-fatigue-guide.html': [
        ('music-production/reference-tracks-mastery.html', 'reference tracks'),
        ('music-production/how-many-lufs-mastering-guide.html', 'LUFS standards')
    ],
    
    # ===== MUSIC BUSINESS - DISTRIBUTION =====
    'music-business/distrokid-pricing-plans.html': [
        ('music-business/distrokid-complete-guide.html', 'DistroKid complete guide'),
        ('music-business/cd-baby-vs-distrokid-2026-comparison.html', 'CD Baby vs DistroKid')
    ],
    'music-business/distrokid-customer-service-support.html': [
        ('music-business/distrokid-complete-guide.html', 'DistroKid guide'),
        ('music-business/distrokid-change-artist-name-guide.html', 'change artist name')
    ],
    'music-business/distrokid-change-artist-name-guide.html': [
        ('music-business/music-metadata-isrc-upc-guide.html', 'music metadata guide'),
        ('music-business/distrokid-complete-guide.html', 'DistroKid guide')
    ],
    'music-business/free-music-distributors-2026.html': [
        ('music-business/distrokid-vs-tunecore-comparison.html', 'DistroKid vs TuneCore'),
        ('music-business/cd-baby-complete-guide.html', 'CD Baby guide')
    ],
    'music-business/tunecore-complete-guide.html': [
        ('music-business/distrokid-vs-tunecore-comparison.html', 'DistroKid vs TuneCore'),
        ('music-business/cd-baby-vs-distrokid-2026-comparison.html', 'distributor comparison')
    ],
    'music-business/cd-baby-complete-guide.html': [
        ('music-business/cd-baby-vs-distrokid-2026-comparison.html', 'CD Baby vs DistroKid'),
        ('music-business/free-music-distributors-2026.html', 'free distributors')
    ],
    'music-business/distrokid-alternatives-2026.html': [
        ('music-business/distrokid-vs-tunecore-comparison.html', 'DistroKid vs TuneCore'),
        ('music-business/free-music-distributors-2026.html', 'free distributors')
    ],
    'music-business/how-to-upload-to-spotify-without-distributor.html': [
        ('music-business/distrokid-complete-guide.html', 'DistroKid guide'),
        ('music-business/spotify-for-artists-complete-guide.html', 'Spotify for Artists')
    ],
    
    # ===== MUSIC BUSINESS - MONETIZATION =====
    'music-business/spotify-pay-per-stream-2026.html': [
        ('music-business/how-to-make-money-from-music.html', 'make money from music'),
        ('music-business/spotify-for-artists-complete-guide.html', 'Spotify for Artists')
    ],
    'music-business/how-to-make-money-from-music.html': [
        ('music-business/sync-licensing-for-beginners.html', 'sync licensing'),
        ('music-business/spotify-pay-per-stream-2026.html', 'Spotify royalties')
    ],
    'music-business/sync-licensing-for-beginners.html': [
        ('music-business/how-to-make-money-from-music.html', 'monetization strategies'),
        ('music-business/sampling-clearance-101.html', 'sample clearance')
    ],
    'music-business/songtrust-royalties-guide.html': [
        ('music-business/pro-explained-ascap-bmi-sesac.html', 'PROs explained'),
        ('music-business/mechanical-licensing-mlc-guide.html', 'mechanical licensing')
    ],
    'music-business/pro-explained-ascap-bmi-sesac.html': [
        ('music-business/songtrust-royalties-guide.html', 'Songtrust guide'),
        ('music-business/soundexchange-complete-guide.html', 'SoundExchange')
    ],
    'music-business/soundexchange-complete-guide.html': [
        ('music-business/pro-explained-ascap-bmi-sesac.html', 'PROs explained'),
        ('music-business/neighborhood-rights-explained.html', 'neighboring rights')
    ],
    
    # ===== MUSIC BUSINESS - LEGAL =====
    'music-business/ai-music-copyright-guide.html': [
        ('music-production/suno-vs-udio-2026.html', 'Suno vs Udio'),
        ('music-business/music-copyright-essentials.html', 'copyright essentials')
    ],
    'music-business/work-for-hire-contracts-guide.html': [
        ('music-business/songwriter-split-sheets-guide.html', 'split sheets'),
        ('music-business/music-copyright-essentials.html', 'copyright basics')
    ],
    'music-business/mechanical-licensing-mlc-guide.html': [
        ('music-business/songtrust-royalties-guide.html', 'Songtrust guide'),
        ('music-business/pro-explained-ascap-bmi-sesac.html', 'PROs explained')
    ],
    'music-business/neighborhood-rights-explained.html': [
        ('music-business/soundexchange-complete-guide.html', 'SoundExchange'),
        ('music-business/pro-explained-ascap-bmi-sesac.html', 'PROs')
    ],
    'music-business/sampling-clearance-101.html': [
        ('music-business/sync-licensing-for-beginners.html', 'sync licensing'),
        ('music-business/music-copyright-essentials.html', 'copyright essentials')
    ],
    'music-business/songwriter-split-sheets-guide.html': [
        ('music-business/work-for-hire-contracts-guide.html', 'work for hire'),
        ('music-business/publishing-admin-vs-standard.html', 'publishing deals')
    ],
    'music-business/publishing-admin-vs-standard.html': [
        ('music-business/songwriter-split-sheets-guide.html', 'split sheets'),
        ('music-business/songtrust-royalties-guide.html', 'Songtrust')
    ],
    'music-business/music-metadata-isrc-upc-guide.html': [
        ('music-business/distrokid-complete-guide.html', 'DistroKid guide'),
        ('music-business/music-copyright-essentials.html', 'copyright basics')
    ],
    'music-business/music-copyright-essentials.html': [
        ('music-business/ai-music-copyright-guide.html', 'AI copyright'),
        ('music-business/sampling-clearance-101.html', 'sample clearance')
    ],
    
    # ===== MUSIC BUSINESS - PLATFORMS =====
    'music-business/spotify-for-artists-complete-guide.html': [
        ('music-business/spotify-playlist-pitching-guide.html', 'playlist pitching'),
        ('music-business/how-to-get-verified-on-spotify.html', 'Spotify verification')
    ],
    'music-business/spotify-playlist-pitching-guide.html': [
        ('music-business/spotify-for-artists-complete-guide.html', 'Spotify for Artists'),
        ('music-business/music-promotion-strategies-2026.html', 'promotion strategies')
    ],
    'music-business/how-to-get-verified-on-spotify.html': [
        ('music-business/spotify-for-artists-complete-guide.html', 'Spotify for Artists'),
        ('music-business/youtube-music-verification.html', 'YouTube verification')
    ],
    'music-business/apple-music-for-artists-guide.html': [
        ('music-business/spotify-for-artists-complete-guide.html', 'Spotify for Artists'),
        ('music-business/amazon-music-for-artists-guide.html', 'Amazon Music')
    ],
    'music-business/amazon-music-for-artists-guide.html': [
        ('music-business/apple-music-for-artists-guide.html', 'Apple Music for Artists'),
        ('music-business/spotify-for-artists-complete-guide.html', 'Spotify for Artists')
    ],
    'music-business/youtube-official-artist-channel-setup.html': [
        ('music-business/claim-youtube-topic-channel-distrokid.html', 'claim Topic channel'),
        ('music-business/youtube-music-verification.html', 'YouTube verification')
    ],
    'music-business/claim-youtube-topic-channel-distrokid.html': [
        ('music-business/youtube-official-artist-channel-setup.html', 'YouTube OAC setup'),
        ('music-business/distrokid-complete-guide.html', 'DistroKid guide')
    ],
    'music-business/youtube-music-verification.html': [
        ('music-business/youtube-official-artist-channel-setup.html', 'YouTube OAC'),
        ('music-business/how-to-get-verified-on-spotify.html', 'Spotify verification')
    ],
    
    # ===== MUSIC BUSINESS - PROMOTION =====
    'music-business/music-promotion-strategies-2026.html': [
        ('music-business/tiktok-music-promotion-guide.html', 'TikTok promotion'),
        ('music-business/spotify-playlist-pitching-guide.html', 'playlist pitching')
    ],
    'music-business/tiktok-music-promotion-guide.html': [
        ('music-business/music-promotion-strategies-2026.html', 'promotion strategies'),
        ('music-business/instagram-for-musicians-guide.html', 'Instagram for musicians')
    ],
    'music-business/instagram-for-musicians-guide.html': [
        ('music-business/tiktok-music-promotion-guide.html', 'TikTok promotion'),
        ('music-business/music-promotion-strategies-2026.html', 'promotion strategies')
    ],
    'music-business/what-is-an-epk.html': [
        ('music-business/music-press-release-template.html', 'press release template'),
        ('music-business/royalty-logo-design-guide.html', 'logo design')
    ],
    'music-business/royalty-logo-design-guide.html': [
        ('music-business/what-is-an-epk.html', 'EPK guide'),
        ('music-business/music-press-release-template.html', 'press releases')
    ],
    'music-business/music-press-release-template.html': [
        ('music-business/what-is-an-epk.html', 'EPK basics'),
        ('music-business/music-promotion-strategies-2026.html', 'promotion strategies')
    ],
    
    # ===== MUSIC BUSINESS - OTHER =====
    'music-business/ep-vs-lp-explanation.html': [
        ('music-business/lp-meaning-in-music.html', 'LP meaning'),
        ('music-business/distrokid-complete-guide.html', 'distribution guide')
    ],
    'music-business/lp-meaning-in-music.html': [
        ('music-business/ep-vs-lp-explanation.html', 'EP vs LP'),
        ('music-business/distrokid-complete-guide.html', 'distribution')
    ],
    'music-business/best-sample-marketplaces.html': [
        ('music-production/sampling-clearance-101.html', 'sample clearance'),
        ('music-business/bbc-sound-effects-library-guide.html', 'BBC sound effects')
    ],
    'music-business/bbc-sound-effects-library-guide.html': [
        ('music-business/best-sample-marketplaces.html', 'sample marketplaces'),
        ('music-production/foley-recording-guide.html', 'foley recording')
    ],
    'music-business/platform-performance-uncovered.html': [
        ('music-business/spotify-pay-per-stream-2026.html', 'Spotify royalties'),
        ('music-business/distrokid-complete-guide.html', 'distribution guide')
    ],
    
    # ===== MUSIC THEORY - SCALES & MODES =====
    'geci/major-scale-explained.html': [
        ('geci/minor-scales-explained.html', 'minor scales'),
        ('geci/key-signatures-simplified.html', 'key signatures')
    ],
    'geci/minor-scales-explained.html': [
        ('geci/major-scale-explained.html', 'major scale'),
        ('geci/relative-parallel-scales.html', 'relative scales')
    ],
    'geci/musical-modes-explained.html': [
        ('geci/dorian-mode-explained.html', 'Dorian mode'),
        ('geci/major-scale-explained.html', 'major scale')
    ],
    'geci/dorian-mode-explained.html': [
        ('geci/musical-modes-explained.html', 'musical modes'),
        ('music-production/how-to-make-lofi-hip-hop.html', 'lofi hip hop')
    ],
    'geci/phrygian-dominant-scale.html': [
        ('geci/musical-modes-explained.html', 'modes overview'),
        ('geci/harmonic-series-timbre.html', 'harmonic series')
    ],
    'geci/relative-parallel-scales.html': [
        ('geci/minor-scales-explained.html', 'minor scales'),
        ('geci/key-signatures-simplified.html', 'key signatures')
    ],
    'geci/key-signatures-simplified.html': [
        ('geci/circle-of-fifths-guide.html', 'circle of fifths'),
        ('geci/major-scale-explained.html', 'major scale')
    ],
    'geci/circle-of-fifths-guide.html': [
        ('geci/key-signatures-simplified.html', 'key signatures'),
        ('geci/modulation-masterclass.html', 'modulation')
    ],
    
    # ===== MUSIC THEORY - CHORDS & HARMONY =====
    'geci/triads-and-seventh-chords.html': [
        ('geci/how-to-build-chords.html', 'build chords'),
        ('geci/chord-progressions-explained.html', 'chord progressions')
    ],
    'geci/diminished-chords-explained.html': [
        ('geci/how-to-build-chords.html', 'chord building'),
        ('geci/secondary-dominants-explained.html', 'secondary dominants')
    ],
    'geci/secondary-dominants-explained.html': [
        ('geci/chord-progressions-explained.html', 'chord progressions'),
        ('geci/cadences-explained.html', 'cadences')
    ],
    'geci/cadences-explained.html': [
        ('geci/chord-progressions-explained.html', 'progressions'),
        ('geci/voice-leading-basics.html', 'voice leading')
    ],
    'geci/modulation-masterclass.html': [
        ('geci/circle-of-fifths-guide.html', 'circle of fifths'),
        ('geci/voice-leading-basics.html', 'voice leading')
    ],
    'geci/jazz-chord-progressions.html': [
        ('geci/jazz-piano-chords-for-beginners.html', 'jazz piano chords'),
        ('geci/secondary-dominants-explained.html', 'secondary dominants')
    ],
    'geci/jazz-piano-chords-for-beginners.html': [
        ('geci/jazz-chord-progressions.html', 'jazz progressions'),
        ('geci/neo-soul-theory-masterclass.html', 'neo soul theory')
    ],
    'geci/minor-chord-progressions.html': [
        ('geci/chord-progressions-explained.html', 'chord progressions'),
        ('geci/minor-scales-explained.html', 'minor scales')
    ],
    'geci/chord-progressions-guitar.html': [
        ('geci/chord-progressions-explained.html', 'progressions theory'),
        ('geci/how-to-build-chords.html', 'build chords')
    ],
    
    # ===== MUSIC THEORY - SONGWRITING =====
    'geci/song-structure-basics.html': [
        ('geci/bridge-in-music-explanation.html', 'bridge explained'),
        ('geci/how-to-write-catchy-chorus.html', 'catchy chorus')
    ],
    'geci/bridge-in-music-explanation.html': [
        ('geci/song-structure-basics.html', 'song structure'),
        ('geci/melodic-contour-guide.html', 'melodic contour')
    ],
    'geci/how-to-write-catchy-chorus.html': [
        ('geci/song-structure-basics.html', 'song structure'),
        ('geci/melodic-contour-guide.html', 'melody writing')
    ],
    'geci/melodic-contour-guide.html': [
        ('geci/how-to-write-catchy-chorus.html', 'catchy chorus'),
        ('geci/voice-leading-basics.html', 'voice leading')
    ],
    'geci/bossa-nova-songs-guide.html': [
        ('geci/jazz-chord-progressions.html', 'jazz progressions'),
        ('geci/rhythm-notation-guide.html', 'rhythm notation')
    ],
    
    # ===== MUSIC THEORY - ADVANCED =====
    'geci/harmonic-series-timbre.html': [
        ('geci/what-is-interval.html', 'intervals'),
        ('music-production/eq-basics-guide.html', 'EQ basics')
    ],
    'geci/what-is-interval.html': [
        ('geci/harmonic-series-timbre.html', 'harmonic series'),
        ('geci/how-to-build-chords.html', 'build chords')
    ],
    'geci/non-chord-tones-guide.html': [
        ('geci/voice-leading-basics.html', 'voice leading'),
        ('geci/counterpoint-basics.html', 'counterpoint')
    ],
    'geci/counterpoint-basics.html': [
        ('geci/voice-leading-basics.html', 'voice leading'),
        ('geci/non-chord-tones-guide.html', 'non-chord tones')
    ],
    'geci/modern-theory-atonality.html': [
        ('geci/harmonic-series-timbre.html', 'harmonic series'),
        ('geci/counterpoint-basics.html', 'counterpoint')
    ],
    'geci/music-cognitive-development.html': [
        ('geci/harmonic-series-timbre.html', 'harmonic perception'),
        ('geci/rhythm-notation-guide.html', 'rhythm basics')
    ],
    'geci/music-dynamics-explained.html': [
        ('geci/rhythm-notation-guide.html', 'rhythm notation'),
        ('music-production/automation-techniques-guide.html', 'automation')
    ],
    'geci/rhythm-notation-guide.html': [
        ('geci/compound-time-signatures.html', 'time signatures'),
        ('geci/music-dynamics-explained.html', 'dynamics')
    ],
    'geci/compound-time-signatures.html': [
        ('geci/rhythm-notation-guide.html', 'rhythm basics'),
        ('geci/bossa-nova-songs-guide.html', 'bossa nova')
    ],
    
    # ===== PRODUCTION - TOOLS & GEAR =====
    'music-production/best-audio-interfaces-2026.html': [
        ('music-production/audio-cable-types-guide.html', 'audio cables'),
        ('music-production/home-vocal-recording-guide.html', 'home recording')
    ],
    'music-production/audio-cable-types-guide.html': [
        ('music-production/best-audio-interfaces-2026.html', 'audio interfaces'),
        ('music-production/what-is-daw.html', 'DAW basics')
    ],
    'music-production/best-producer-laptop-2026.html': [
        ('music-production/what-is-daw.html', 'DAW requirements'),
        ('music-production/best-audio-interfaces-2026.html', 'audio interfaces')
    ],
    'music-production/acoustic-treatment-guide.html': [
        ('music-production/home-vocal-recording-guide.html', 'home recording'),
        ('music-production/stereo-imaging-guide.html', 'stereo imaging')
    ],
    'music-production/free-vst-plugins-guide.html': [
        ('music-production/best-fl-studio-plugins.html', 'FL Studio plugins'),
        ('music-production/serum-for-ableton-guide.html', 'Serum')
    ],
    'music-production/best-free-vocal-vst-plugins.html': [
        ('music-production/free-vst-plugins-guide.html', 'free VST plugins'),
        ('music-production/vocal-production-masterclass.html', 'vocal production')
    ],
    
    # ===== PRODUCTION - TECHNIQUES =====
    'music-production/sidechain-compression-guide.html': [
        ('music-production/compression-basics-guide.html', 'compression basics'),
        ('music-production/how-to-make-lofi-hip-hop.html', 'lofi production')
    ],
    'music-production/parallel-processing-techniques.html': [
        ('music-production/compression-basics-guide.html', 'compression'),
        ('music-production/reverb-and-delay-guide.html', 'reverb and delay')
    ],
    'music-production/drum-programming-basics.html': [
        ('music-production/kick-drum-eq-guide.html', 'kick drum EQ'),
        ('music-production/how-to-make-lofi-hip-hop.html', 'lofi drums')
    ],
    'music-production/foley-recording-guide.html': [
        ('music-business/bbc-sound-effects-library-guide.html', 'BBC sound effects'),
        ('music-production/home-vocal-recording-guide.html', 'recording techniques')
    ],
    'music-production/gross-beat-tape-stop-guide.html': [
        ('music-production/transitions-and-ear-candy-guide.html', 'transitions'),
        ('music-production/fl-studio-selection-guide.html', 'FL Studio')
    ],
    'music-production/how-to-make-lofi-hip-hop.html': [
        ('geci/dorian-mode-explained.html', 'Dorian mode'),
        ('music-production/sidechain-compression-guide.html', 'sidechain compression')
    ],
    
    # ===== PRODUCTION - UTILITIES =====
    'music-production/audio-file-formats-guide.html': [
        ('music-production/how-many-lufs-mastering-guide.html', 'mastering standards'),
        ('music-business/music-metadata-isrc-upc-guide.html', 'music metadata')
    ],
    'music-production/pitch-shift-calculator.html': [
        ('music-production/note-to-hz-frequency-chart.html', 'frequency chart'),
        ('music-production/auto-tune-vs-pitch-correction.html', 'pitch correction')
    ],
    'music-production/note-to-hz-frequency-chart.html': [
        ('music-production/pitch-shift-calculator.html', 'pitch calculator'),
        ('music-production/eq-basics-guide.html', 'EQ basics')
    ],
    'music-production/piano-frequency-chart.html': [
        ('music-production/note-to-hz-frequency-chart.html', 'frequency reference'),
        ('music-production/eq-basics-guide.html', 'EQ guide')
    ],
    'music-production/midi-note-to-frequency.html': [
        ('music-production/note-to-hz-frequency-chart.html', 'frequency chart'),
        ('music-production/what-is-daw.html', 'DAW basics')
    ],
    'music-production/dynamic-eq-mixing-guide.html': [
        ('music-production/eq-basics-guide.html', 'EQ basics'),
        ('music-production/soothe-2-mixing-guide.html', 'Soothe 2')
    ],
    'music-production/binaural-mixing-guide.html': [
        ('music-production/stereo-imaging-guide.html', 'stereo imaging'),
        ('music-production/reverb-and-delay-guide.html', 'spatial effects')
    ],
}

def add_related_articles_section(html_content, related_links, file_path):
    """Add a 'Related Reading' section before the closing </article> tag."""
    
    # Check if already has related articles section
    if 'related-articles' in html_content or 'Related Articles' in html_content or 'Related Reading' in html_content:
        return html_content, False
    
    # Build the related articles HTML
    related_html = '\n                <div class="related-articles">\n'
    related_html += '                    <h3>Related Reading</h3>\n'
    related_html += '                    <ul>\n'
    
    for link_path, link_text in related_links:
        # Convert absolute path to relative path
        current_dir = os.path.dirname(file_path)
        if current_dir.startswith('music-production') and link_path.startswith('music-business'):
            rel_path = '../' + link_path
        elif current_dir.startswith('music-production') and link_path.startswith('geci'):
            rel_path = '../' + link_path
        elif current_dir.startswith('music-business') and link_path.startswith('music-production'):
            rel_path = '../' + link_path
        elif current_dir.startswith('music-business') and link_path.startswith('geci'):
            rel_path = '../' + link_path
        elif current_dir.startswith('geci') and link_path.startswith('music-production'):
            rel_path = '../' + link_path
        elif current_dir.startswith('geci') and link_path.startswith('music-business'):
            rel_path = '../' + link_path
        else:
            rel_path = os.path.basename(link_path)
        
        related_html += f'                        <li><a href="{rel_path}">{link_text.title()}</a></li>\n'
    
    related_html += '                    </ul>\n'
    related_html += '                </div>\n'
    
    # Find the closing </article> tag and insert before it
    article_close_match = re.search(r'(\s*)</article>', html_content)
    if not article_close_match:
        return html_content, False
    
    new_content = html_content[:article_close_match.start()] + related_html + html_content[article_close_match.start():]
    return new_content, True

def process_file(file_path, related_links):
    """Add related articles section to a single file."""
    full_path = os.path.join('/Users/bizcheers/jan-20-haolingsheng/haolingsheng', file_path)
    
    if not os.path.exists(full_path):
        return False, f"File not found: {file_path}"
    
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content, modified = add_related_articles_section(content, related_links, file_path)
    
    if not modified:
        return False, "Already has related articles or no </article> tag"
    
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True, "Related articles added"

def main():
    results = {
        'success': [],
        'skipped': [],
        'failed': []
    }
    
    print(f"\nProcessing {len(TOPIC_CLUSTERS)} articles with internal links...\n")
    
    for file_path, related_links in TOPIC_CLUSTERS.items():
        success, message = process_file(file_path, related_links)
        
        if success:
            results['success'].append(file_path)
            print(f"✓ {file_path}")
        elif "Already has" in message:
            results['skipped'].append(file_path)
            # print(f"⊘ {file_path}")  # Suppress skipped messages for cleaner output
        else:
            results['failed'].append((file_path, message))
            print(f"✗ {file_path} - {message}")
    
    # Print summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"✓ Successfully processed: {len(results['success'])}")
    print(f"⊘ Skipped (already have links): {len(results['skipped'])}")
    print(f"✗ Failed: {len(results['failed'])}")
    
    if results['failed']:
        print("\nFailed files:")
        for file, reason in results['failed']:
            print(f"  - {file}: {reason}")

if __name__ == '__main__':
    main()
