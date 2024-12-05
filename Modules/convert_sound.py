from wit import Wit
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import io
import wave


# Your Wit.ai API access token
file = open("apikey.txt")
access_token = file.readline()

# Initialize Wit.ai client
client = Wit(access_token)


def convert_sound_text():
    """Recognize speech from a WAV file using Wit.ai."""
    try:
        # Open the WAV file
        with open("recordings/output.wav", 'rb') as f:
            # Send the WAV file to Wit.ai for speech recognition
            print("Recognizing speech...")
            response = client.speech(f, {"Content-Type": "audio/wav"})
            print("Wit.ai response:", response)

            # Extract the text from the response
            if "text" in response:
                return response["text"]
            else:
                return "Sorry, I couldn't understand that."
    except Exception as e:
        print(f"Error recognizing speech: {e}")
        return "Error in speech recognition."