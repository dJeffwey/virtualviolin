import numpy as np
from scipy.io.wavfile import write

# Parameters for the sound
sample_rate = 44100  # Sample rate in Hz
duration = 2.0  # Duration in seconds
frequency = 659.25  # Frequency for the open E string in Hz

# Time array
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generate a sine wave
audio_data = 0.5 * np.sin(2 * np.pi * frequency * t)

# Add vibrato effect
vibrato_frequency = 5  # Vibrato frequency in Hz
vibrato_depth = 0.01  # Vibrato depth
vibrato = np.sin(2 * np.pi * vibrato_frequency * t) * vibrato_depth
audio_data = 0.5 * np.sin(2 * np.pi * frequency * (t + vibrato))

# Convert to 16-bit PCM format
audio_data = np.int16(audio_data * 32767)

# Write to a WAV file
write('violin_sound.wav', sample_rate, audio_data)

print("Violin sound generated and saved as 'violin_sound.wav'")
