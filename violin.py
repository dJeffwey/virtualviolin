import pygame
import time

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Load sound files
sounds = {
    'g': '196.wav',
    'd': '293.wav',
    'a': '440.wav',
    'e': '659.wav'
}

# Set up the display in fullscreen mode
info = pygame.display.Info()
window = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
pygame.display.set_caption("Virtual Violin")

# Key to sound mapping
key_map = {
    pygame.K_1: 'e',  # 1 key to E sound
    pygame.K_q: 'a',  # Q key to A sound
    pygame.K_a: 'd',  # A key to D sound
    pygame.K_z: 'g'   # Z key to G sound
}

# Function to play sound
def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)  # Loop the sound indefinitely

# Function to stop sound
def stop_sound():
    pygame.mixer.music.stop()

# Main loop
running = True
playing_sounds = {}  # Keep track of currently playing sounds

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in key_map:
                key = key_map[event.key]
                if key in sounds:
                    if key not in playing_sounds:
                        play_sound(sounds[key])
                        playing_sounds[key] = sounds[key]
        elif event.type == pygame.KEYUP:
            if event.key in key_map:
                key = key_map[event.key]
                if key in playing_sounds:
                    stop_sound()
                    del playing_sounds[key]

pygame.quit()
