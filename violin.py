import pygame
import time

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Load sound files
sounds = {
    # E string notes
    'e': '659.wav',   # E (Open E)
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
    'd#': '1244.51.wav', # D#

    # A string notes
    'a2': '440.wav',  # A (Open A)
    'b2': '246.94.wav',  # B
    'c2': '261.63.wav',  # C
    'd2': '293.66.wav',  # D
    'e2': '329.63.wav',  # E
    'f2': '349.23.wav',  # F
    'g2': '392.00.wav',  # G
    'a3': '440.00.wav',  # A
    'b3': '493.88.wav',  # B

    # D string notes
    'd3': '293.wav',  # D (Open D)
    'e3': '329.63.wav',  # E
    'f3': '349.23.wav',  # F
    'g3': '392.00.wav',  # G
    'a3': '440.00.wav',  # A
    'b3': '493.88.wav',  # B
    'c4': '523.25.wav',  # C
    'd4': '587.33.wav',  # D
    'e4': '659.25.wav',  # E

    # G string notes
    'g3': '392.00.wav',  # G (Open G)
    'a3': '440.00.wav',  # A
    'b3': '493.88.wav',  # B
    'c4': '523.25.wav',  # C
    'd4': '587.33.wav',  # D
    'e4': '659.25.wav',  # E
    'f4': '698.46.wav',  # F
    'g4': '783.99.wav'   # G
}

# Set up the display in fullscreen mode
info = pygame.display.Info()
window = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
pygame.display.set_caption("Virtual Violin")

# Key to sound mapping
key_map = {
    # E string notes
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
    pygame.K_EQUALS: 'd#',   # = key to D# sound

    # A string notes
    pygame.K_q: 'a2',   # Q key to A (Open A) sound

    # D string notes
    pygame.K_a: 'd3',   # A key to D sound

    # G string notes
    pygame.K_z: 'g3'    # Z key to G sound
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
