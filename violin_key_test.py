import pygame

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Load sound file
violin_sound = pygame.mixer.Sound('violin_sound.wav')  # Ensure this file is in the same directory

# Set up the display
pygame.display.set_mode((200, 100))  # Small window for testing
pygame.display.set_caption("Virtual Violin")

# Function to play sound
def play_sound():
    violin_sound.play()
    print("Playing sound...")

# Function to stop sound
def stop_sound():
    violin_sound.stop()
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
                    play_sound()
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
