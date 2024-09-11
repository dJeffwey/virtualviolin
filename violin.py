import numpy as np
import pygame
import time

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Create a window for Pygame to work properly
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Virtual Violin")

# Define sampling rate and duration
SAMPLE_RATE = 44100  # Hertz
DURATION = 5  # seconds

# Frequency of open E string
E_FREQ = 659.26

# Generate a more realistic violin-like sound
def generate_violin_sound(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    
    # Vibrato parameters
    vibrato_frequency = 5.0  # Hz
    vibrato_depth = 0.005    # Depth of vibrato effect

    # Envelope parameters
    attack_time = 0.1  # seconds
    decay_time = 0.2   # seconds
    sustain_level = 0.6
    release_time = 0.3 # seconds

    # Generate the fundamental frequency with vibrato
    vibrato = vibrato_depth * np.sin(2 * np.pi * vibrato_frequency * t)
    fundamental_wave = np.sin(2 * np.pi * (frequency + vibrato) * t)
    
    # Add harmonics for a richer sound
    harmonic1 = 0.5 * np.sin(2 * np.pi * (2 * frequency + vibrato) * t)  # Second harmonic
    harmonic2 = 0.3 * np.sin(2 * np.pi * (3 * frequency + vibrato) * t)  # Third harmonic
    harmonic3 = 0.2 * np.sin(2 * np.pi * (4 * frequency + vibrato) * t)  # Fourth harmonic
    
    # Combine harmonics
    sound_wave = fundamental_wave + harmonic1 + harmonic2 + harmonic3
    
    # Apply ADSR (Attack, Decay, Sustain, Release) envelope
    attack = np.clip(t / attack_time, 0, 1)
    decay = np.clip((duration - t) / decay_time, 0, 1)
    sustain = np.clip((t - (duration - release_time)) / release_time, 0, 1)
    envelope = np.minimum(attack, decay) * sustain_level + sustain * (1 - sustain_level)
    
    sound_wave *= envelope
    
    # Ensure sound is in the range [-1, 1]
    sound_wave = np.clip(sound_wave, -1, 1)
    
    # Convert to 16-bit PCM format
    sound_wave_pcm = np.int16(sound_wave * 32767)
    
    # Convert to bytes for pygame
    sound_data = sound_wave_pcm.tobytes()
    return sound_data

# Generate the violin sound for open E string
violin_e_sound_data = generate_violin_sound(E_FREQ, DURATION, SAMPLE_RATE)

# Create a sound object in pygame from the generated data
violin_e_sound = pygame.mixer.Sound(buffer=violin_e_sound_data)

def play_violin_e():
    violin_e_sound.play()

def stop_violin_e():
    violin_e_sound.stop()

# Main loop to handle key press
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if CTRL key is held
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:  # Left or right CTRL
        if not pygame.mixer.get_busy():
            print("Playing Violin E sound...")
            play_violin_e()
    else:
        stop_violin_e()

    time.sleep(0.1)

# Quit pygame
pygame.quit()
