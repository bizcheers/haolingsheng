import wave
import struct
import math
import os

def generate_tone(filename, duration=10, freq=440.0, wave_type='sine', volume=0.5):
    sample_rate = 44100
    num_samples = int(duration * sample_rate)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sample_rate)
        
        for i in range(num_samples):
            t = float(i) / sample_rate
            
            if wave_type == 'sine':
                # Zen style: Pure sine waves with fade out
                fade = 1.0 - (float(i) / num_samples)
                value = math.sin(2.0 * math.pi * freq * t) * fade
            elif wave_type == 'sawtooth':
                # Retro/8-bit style
                value = (2.0 * (t * freq - math.floor(t * freq + 0.5)))
            elif wave_type == 'noise':
                # SFX/Nature style (simple random)
                import random
                value = random.uniform(-1, 1)
            elif wave_type == 'chirp':
                # Loudest/Functional: Rising frequency
                current_freq = freq + (i / num_samples) * 1000
                value = math.sin(2.0 * math.pi * current_freq * t)
            else:
                value = math.sin(2.0 * math.pi * freq * t)

            sample = int(value * volume * 32767)
            wav_file.writeframesraw(struct.pack('<h', sample))

# List of files to generate
audio_dir = "/Users/bizcheers/jan-20-haolingsheng/haolingsheng/lingsheng/mp3/audio/"

files_to_make = [
    # Zen & Calm
    ("zen-calm-loop.wav", 10, 432.0, 'sine', 0.4),
    # Animal
    ("rooster-crowing-loop.wav", 5, 880.0, 'chirp', 0.6),
    ("goat-scream-loop.wav", 3, 600.0, 'sawtooth', 0.5),
    ("duck-quack-loop.wav", 1, 400.0, 'sawtooth', 0.3),
    ("bird-chirp-loop.wav", 2, 1200.0, 'sine', 0.4),
    ("cat-meow-loop.wav", 2, 1000.0, 'sine', 0.4),
    ("dog-bark-loop.wav", 1, 200.0, 'sawtooth', 0.6),
    ("rain-loop.wav", 10, 0, 'noise', 0.2),
    # Nostalgia
    ("classic-nokia-loop.wav", 5, 659.25, 'sine', 0.5), # E5
    ("classic-moto-loop.wav", 3, 440.0, 'sawtooth', 0.5),
    # Gaming
    ("zelda-inspired-loop.wav", 4, 392.0, 'sine', 0.5),
    ("gta-inspired-loop.wav", 5, 110.0, 'sawtooth', 0.6),
    ("halo-inspired-loop.wav", 8, 220.0, 'sine', 0.4),
    ("cyberpunk-inspired-loop.wav", 6, 60.0, 'sawtooth', 0.7),
    # Lo-Fi / Cinematic
    ("lofi-preview-loop.wav", 10, 300.0, 'sine', 0.5),
    ("8bit-retro-loop.wav", 5, 440.0, 'sawtooth', 0.5),
    ("cinematic-impact-loop.wav", 4, 50.0, 'noise', 0.6),
    # Loudest / Device
    ("loudest-optimized-loop.wav", 5, 2500.0, 'chirp', 0.8),
    ("samsung-inspired-loop.wav", 6, 523.25, 'sine', 0.5), # C5
    ("pixel-inspired-loop.wav", 5, 783.99, 'sine', 0.4), # G5
    # Phase 5: Additional Hubs
    ("messenger-inspired-loop.wav", 2, 800.0, 'sine', 0.5),
    ("faith-inspired-loop.wav", 8, 440.0, 'sine', 0.4),
    ("gospel-inspired-loop.wav", 6, 330.0, 'sine', 0.5),
    ("xmas-inspired-loop.wav", 4, 1000.0, 'sine', 0.5),
    ("halloween-inspired-loop.wav", 6, 150.0, 'sine', 0.4),
    ("fart-inspired-loop.wav", 1, 80.0, 'noise', 0.6),
    ("crazyfrog-inspired-loop.wav", 3, 500.0, 'sawtooth', 0.5),
    ("annoying-beep-loop.wav", 0.5, 3000.0, 'chirp', 0.8),
    ("laugh-inspired-loop.wav", 2, 400.0, 'sawtooth', 0.5),
    ("slap-inspired-loop.wav", 0.3, 200.0, 'noise', 0.6),
    ("chicken-inspired-loop.wav", 1.5, 600.0, 'sawtooth', 0.5),
    ("onepiece-inspired-loop.wav", 2, 900.0, 'chirp', 0.5),
    ("shing-inspired-loop.wav", 0.5, 4000.0, 'chirp', 0.6),
    ("batman-inspired-loop.wav", 4, 100.0, 'sine', 0.5),
    ("kim-inspired-loop.wav", 1, 1500.0, 'chirp', 0.5),
]

for name, dur, freq, wtype, vol in files_to_make:
    path = os.path.join(audio_dir, name)
    print(f"Generating {name}...")
    generate_tone(path, dur, freq, wtype, vol)

print("Done generating audio files.")
