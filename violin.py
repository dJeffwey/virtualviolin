import os
import winsound

# Sound files for the open strings of a violin (G, D, A, E)
sound_files = {
    'G': '196.wav',  # G open string
    'D': '293.wav',  # D open string
    'A': '440.wav',  # A open string
    'E': '659.wav',  # E open string
}

def play_sound(note):
    """Plays the sound for the given violin string note."""
    if note in sound_files:
        sound_path = os.path.join(os.getcwd(), sound_files[note])
        winsound.PlaySound(sound_path, winsound.SND_FILENAME)
    else:
        print(f"Note {note} not found!")

def virtual_violin():
    """Allows users to play violin strings by pressing keys."""
    while True:
        print("Press G, D, A, E to play the open strings or 'q' to quit:")
        note = input().upper()
        if note == 'Q':
            break
        play_sound(note)

if __name__ == "__main__":
    virtual_violin()
