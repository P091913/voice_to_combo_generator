import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import keyboard



def voice():
    # Ask the user for the recording duration
    recording_duration = float(input("Enter the number of seconds you want to record: "))

    print(f"Your voice is now being recorded for {recording_duration} seconds...")

    # Parameters
    samplerate = 22050
    channels = 1  # Set to 1 for mono audio (adjust as needed)
    audio_data = []
    chunk_duration = 0.1  # Record in 0.1 second chunks

    # Total number of chunks to record
    num_chunks = int(recording_duration / chunk_duration)

    # Start recording in chunks
    for _ in range(num_chunks):
        chunk = sd.rec(int(samplerate * chunk_duration), samplerate=samplerate, channels=channels, dtype='float32',
                       blocking=True)
        audio_data.append(chunk)

    print("Recording stopped")

    # Concatenate all audio chunks into a single array
    audio_data = np.concatenate(audio_data, axis=0)

    # Save the audio data to a WAV file
    write("recordings/output.wav", samplerate, np.array(audio_data, dtype=np.float32))

    print("Audio saved as 'recordings/output.wav'")

    return True
