import pygame

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Load sound file
sound_file = 'violin_sound.wav'  # Ensure this file is in the same directory

# Function to play sound
def play_sound(sound_file):
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
    pygame.time.delay(2000)  # Play sound for 2 seconds

# Play the sound
play_sound(sound_file)

# Quit Pygame
pygame.quit()
