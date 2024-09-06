import sys
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Define note-to-file mapping
note_files = {
    'G': '196.wav',
    'D': '293.wav',
    'A': '440.wav',
    'E': '659.wav'
}

def play_sound(note):
    if note in note_files:
        sound_file = note_files[note]
        sound = pygame.mixer.Sound(sound_file)
        sound.play()
    else:
        print(f"Note {note} not found!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        note = sys.argv[1]
        play_sound(note)
