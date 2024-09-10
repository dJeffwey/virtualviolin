import pygame
import time

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Load sound files
sounds = {
    # E string notes
    'e': '659.wav',    # Open E
    'es': '698.wav',   # Open E# or F
    'e1': '698.wav',   # 1st finger on E string, F
    'e1s': '740.wav',  # 1st finger on E string, F#
    'e2': '784.wav',   # 2nd finger on E string, G
    'e2s': '831.wav',  # 2nd finger on E string, G#
    'e3': '880.wav',   # 3rd finger on E string, A
    'e3s': '932.wav',  # 3rd finger on E string, A#
    'e4': '988.wav',   # 4th finger on E string, B
    'e4s': '1047.wav', # 4th finger on E string, C

    # A string notes
    'a': '440.wav',    # Open A
    'as': '466.wav',   # Open A# or Bb
    'a1': '466.wav',   # 1st finger on A string, A#
    'a1s': '494.wav',  # 1st finger on A string, B
    'a2': '494.wav',   # 2nd finger on A string, B
    'a2s': '523.wav',  # 2nd finger on A string, C
    'a3': '523.wav',   # 3rd finger on A string, C
    'a3s': '554.wav',  # 3rd finger on A string, C#
    'a4': '587.wav',   # 4th finger on A string, D
    'a4s': '622.wav',  # 4th finger on A string, D#

    # D string notes
    'd': '294.wav',    # Open D
    'ds': '311.wav',   # Open D# or Eb
    'd1': '311.wav',   # 1st finger on D string, D#
    'd1s': '330.wav',  # 1st finger on D string, E
    'd2': '330.wav',   # 2nd finger on D string, E
    'd2s': '370.wav',  # 2nd finger on D string, F#
    'd3': '370.wav',   # 3rd finger on D string, F#
    'd3s': '392.wav',  # 3rd finger on D string, G
    'd4': '392.wav',   # 4th finger on D string, G
    'd4s': '415.wav',  # 4th finger on D string, G#

    # G string notes
    'g': '196.wav',    # Open G
    'gs': '208.wav',   # Open G# or Ab
    'g1': '208.wav',   # 1st finger on G string, G#
    'g1s': '220.wav',  # 1st finger on G string, A
    'g2': '220.wav',   # 2nd finger on G string, A
    'g2s': '233.wav',  # 2nd finger on G string, A#
    'g3': '233.wav',   # 3rd finger on G string, A#
    'g3s': '247.wav',  # 3rd finger on G string, B
    'g4': '247.wav',   # 4th finger on G string, B
}

# Set up the display in fullscreen mode
info = pygame.display.Info()
window = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
pygame.display.set_caption("Virtual Jeffreylin (violin lol)")

# Key to sound mapping
key_map = {
    # E string notes
    pygame.K_1: 'e',    # 1 key to Open E
    pygame.K_2: 'es',   # 2 key to Open E# or F
    pygame.K_3: 'e1',   # 3 key to 1st finger on E string, F
    pygame.K_4: 'e1s',  # 4 key to 1st finger on E string, F#
    pygame.K_5: 'e2',   # 5 key to 2nd finger on E string, G
    pygame.K_6: 'e2s',  # 6 key to 2nd finger on E string, G#
    pygame.K_7: 'e3',   # 7 key to 3rd finger on E string, A
    pygame.K_8: 'e3s',  # 8 key to 3rd finger on E string, A#
    pygame.K_9: 'e4',   # 9 key to 4th finger on E string, B
    pygame.K_0: 'e4s',  # 0 key to 4th finger on E string, C

    # A string notes
    pygame.K_q: 'a',    # Q key to Open A
    pygame.K_w: 'as',   # W key to Open A# or Bb
    pygame.K_e: 'a1',   # E key to 1st finger on A string, A#
    pygame.K_r: 'a1s',  # R key to 1st finger on A string, B
    pygame.K_t: 'a2',   # T key to 2nd finger on A string, B
    pygame.K_y: 'a2s',  # Y key to 2nd finger on A string, C
    pygame.K_u: 'a3',   # U key to 3rd finger on A string, C
    pygame.K_i: 'a3s',  # I key to 3rd finger on A string, C#
    pygame.K_o: 'a4',   # O key to 4th finger on A string, D
    pygame.K_p: 'a4s',  # P key to 4th finger on A string, D#

    # D string notes
    pygame.K_a: 'd',    # A key to Open D
    pygame.K_s: 'ds',   # S key to Open D# or Eb
    pygame.K_d: 'd1',   # D key to 1st finger on D string, D#
    pygame.K_f: 'd1s',  # F key to 1st finger on D string, E
    pygame.K_g: 'd2',   # G key to 2nd finger on D string, E
    pygame.K_h: 'd2s',  # H key to 2nd finger on D string, F#
    pygame.K_j: 'd3',   # J key to 3rd finger on D string, F#
    pygame.K_k: 'd3s',  # K key to 3rd finger on D string, G
    pygame.K_l: 'd4',   # L key to 4th finger on D string, G
    pygame.K_semicolon: 'd4s',  # ; key to 4th finger on D string, G#

    # G string notes
    pygame.K_z: 'g',    # Z key to Open G
    pygame.K_x: 'gs',   # X key to Open G# or Ab
    pygame.K_c: 'g1',   # C key to 1st finger on G string, G#
    pygame.K_v: 'g1s',  # V key to 1st finger on G string, A
    pygame.K_b: 'g2',   # B key to 2nd finger on G string, A
    pygame.K_n: 'g2s',  # N key to 2nd finger on G string, A#
    pygame.K_m: 'g3',   # M key to 3rd finger on G string, A#
    pygame.K_comma: 'g3s',  # , key to 3rd finger on G string, B
    pygame.K_period: 'g4',   # . key to 4th finger on G string, B
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

# Quit Pygame
pygame.quit()
