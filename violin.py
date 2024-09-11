import numpy as np
import simpleaudio as sa
import pygame

# Function to generate a sine wave for a given frequency
def generate_sine_wave(freq, duration, sample_rate=44100, amplitude=32767):
    t = np.linspace(0, duration, int(sample_rate * duration), False)  # Time axis
    wave = amplitude * np.sin(2 * np.pi * freq * t)  # Generate sine wave
    wave = wave.astype(np.int16)  # Convert to 16-bit data
    return wave

# Play sound at a specific frequency (Hertz)
def play_sound(freq, duration=2):
    wave = generate_sine_wave(freq, duration)
    audio = sa.play_buffer(wave, 1, 2, 44100)  # Play buffer (mono, 16-bit, 44100 Hz)
    audio.wait_done()  # Wait until the sound is done playing

# Initialize Pygame for key detection
pygame.init()
window = pygame.display.set_mode((200, 200))  # Create a small window

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Detect if Ctrl key is pressed down
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                play_sound(659)  # Play the open E string sound (659 Hz)

# Quit Pygame when done
pygame.quit()
