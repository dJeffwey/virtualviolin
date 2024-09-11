import pygame

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Load sound file
violin_sound = 'violin_sound.wav'

# Set up the display
info = pygame.display.Info()
window = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
pygame.display.set_caption("Virtual Violin")

# Function to play sound
def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)  # Loop the sound indefinitely
    print("Playing sound...")

# Function to stop sound
def stop_sound():
    pygame.mixer.music.stop()
    print("Sound stopped.")

# Main loop
running = True
sound_playing = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:  # Check if Left Control is pressed
                if not sound_playing:
                    play_sound(violin_sound)
                    sound_playing = True
                    print("CTRL pressed.")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LCTRL:  # Check if Left Control is released
                if sound_playing:
                    stop_sound()
                    sound_playing = False
                    print("CTRL released.")

# Quit Pygame
pygame.quit()
