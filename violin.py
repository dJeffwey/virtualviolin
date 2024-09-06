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

    'a2': '440.wav',  # A (Open A)
    'a#2': '466.16.wav',  # A# (or Bb)
    'b2': '493.88.wav',  # B
    'c2': '523.25.wav',  # C
    'c#2': '554.37.wav', # C#
    'd2': '587.33.wav',  # D
    'd#2': '622.25.wav', # D#
    'e2': '659.25.wav',  # E
    'f2': '698.46.wav',  # F
    'f#2': '739.99.wav', # F#
    'g2': '783.99.wav',  # G
    'g#2': '830.61.wav', # G#
    'a3': '880.00.wav',  # A
    'a#3': '932.33.wav', # A# (or Bb)
    'b3': '987.77.wav',  # B

    # D string notes
    'd3': '293.wav',  # D (Open D)
    'd#3': '311.13.wav', # D#
    'e3': '329.63.wav',  # E
    'f3': '349.23.wav',  # F
    'f#3': '369.99.wav', # F#
    'g3': '392.00.wav',  # G
    'g#3': '415.30.wav', # G#
    'a3': '440.00.wav',  # A
    'a#3': '466.16.wav', # A# (or Bb)
    'b3': '493.88.wav',  # B
    'c4': '523.25.wav',  # C
    'c#4': '554.37.wav', # C#
    'd4': '587.33.wav',  # D
    'd#4': '622.25.wav', # D#
    'e4': '659.25.wav',  # E

    # G string notes
    'g3': '196.wav',  # G (Open G)
    'g#3': '207.65.wav', # G#
    'a3': '220.00.wav',  # A
    'a#3': '233.08.wav', # A# (or Bb)
    'b3': '246.94.wav',  # B
    'c4': '261.63.wav',  # C
    'c#4': '277.18.wav', # C#
    'd4': '293.66.wav',  # D
    'd#4': '311.13.wav', # D#
    'e4': '329.63.wav',  # E
    'f4': '349.23.wav',  # F
    'f#4': '369.99.wav', # F#
    'g4': '392.00.wav'   # G
}

# Set up the display in fullscreen mode
info = pygame.display.Info()
window = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
pygame.display.set_caption("Virtual Jeffreylin (violin lol)")

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
    pygame.K_w: 'a#2',  # W key to A# sound
    pygame.K_e: 'b2',   # E key to B sound
    pygame.K_r: 'c2',   # R key to C sound
    pygame.K_t: 'c#2',  # T key to C# sound
    pygame.K_y: 'd2',   # Y key to D sound
    pygame.K_u: 'd#2',  # U key to D# sound
    pygame.K_i: 'e2',   # I key to E sound
    pygame.K_o: 'f2',   # O key to F sound
    pygame.K_p: 'f#2',  # P key to F# sound
    pygame.K_LEFTBRACKET: 'g2',  # [ key to G sound
    pygame.K_RIGHTBRACKET: 'g#2', # ] key to G# sound
    pygame.K_BACKSLASH: 'a3',  # \ key to A sound
    pygame.K_SEMICOLON: 'a#3', # ; key to A# sound
    pygame.K_QUOTE: 'b3',    # ' key to B sound

    # D string notes
    pygame.K_a: 'd3',   # A key to D sound
    pygame.K_s: 'd#3',  # S key to D# sound
    pygame.K_d: 'e3',   # D key to E sound
    pygame.K_f: 'f3',   # F key to F sound
    pygame.K_g: 'f#3',  # G key to F# sound
    pygame.K_h: 'g3',   # H key to G sound
    pygame.K_j: 'g#3',  # J key to G# sound
    pygame.K_k: 'a3',   # K key to A sound
    pygame.K_l: 'a#3',  # L key to A# sound
    pygame.K_SEMICOLON: 'b3', # ; key to B sound
    pygame.K_QUOTE: 'c4',    # ' key to C sound
    pygame.K_RETURN: 'c#4',   # Enter key to C# sound
    pygame.K_LSHIFT: 'd4',   # Left Shift key to D sound
    pygame.K_RSHIFT: 'd#4',  # Right Shift key to D# sound
    pygame.K_LCTRL: 'e4',    # Left Control key to E sound

    # G string notes
    pygame.K_z: 'g3',   # Z key to G sound
    pygame.K_x: 'g#3',  # X key to G# sound
    pygame.K_c: 'a3',   # C key to A sound
    pygame.K_v: 'a#3',  # V key to A# sound
    pygame.K_b: 'b3',   # B key to B sound
    pygame.K_n: 'c4',   # N key to C sound
    pygame.K_m: 'c#4',  # M key to C# sound
    pygame.K_COMMA: 'd4',  # , key to D sound
    pygame.K_PERIOD: 'd#4', # . key to D# sound
    pygame.K_SLASH: 'e4',   # / key to E sound
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
