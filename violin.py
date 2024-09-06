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
            key = pygame.key.name(event.key)
            if key in sounds:
                if key not in playing_sounds:
                    play_sound(sounds[key])
                    playing_sounds[key] = sounds[key]
        elif event.type == pygame.KEYUP:
            key = pygame.key.name(event.key)
            if key in playing_sounds:
                stop_sound()
                del playing_sounds[key]

pygame.quit()
