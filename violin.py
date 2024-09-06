import pygame
import time

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Load sound files
sounds = {
    'e': '659.25.wav',   # E (Open E)
    'f': '698.46.wav',   # F
    'f#': '739.99.wav',  # F#
    'g': '783.99.wav',   # G
    'g#': '830.61.wav',  # G#
    'a': '880.00.wav',   # A
    'a#': '932.33.wav',  # A#
    'b': '987.77.wav',   # B
    'c': '1046.50.wav',  # C
    'c#': '1108.73.wav', # C#
    'd': '1174.66.wav',  # D
    'd#': '1244.51.wav'  # D#
}

# Set up the display in fullscreen mode
info = pygame.display.Info()
window = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
pygame.display.set_caption("Virtual Jeffreylin (violin lol)")

# Key to sound mapping
key_map = {
    pygame.K_1: 'e',    # 1 key to E (Open E) sound
    pygame.K_2: 'f',    # 2 key to F sound
    pygame.K_3: 'f#',   # 3 key to F# sound
    pygame.K_4: 'g',    # 4 key to G sound
    pygame.K_5: 'g#',   # 5 key to G# sound
    pygame.K_6: 'a',    # 6 key to A sound
    pygame.K_7: 'a#',   # 7 key to A# sound
    pygame.K_8: 'b',    # 8 key to B sound
    pygame.K_9: 'c',    # 9 key to C sound
    pygame.K_0: 'c#',   # 0 key to C# sound
    pygame.K_MINUS: 'd',    # - key to D sound
    pygame.K_EQUALS: 'd#'   # = key to D# sound
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
