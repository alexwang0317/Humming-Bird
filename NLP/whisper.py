import openai
import sounddevice as sd
import numpy as np
import io
import os
from scipy.io.wavfile import write

# Set up your API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def callback(indata, frames, time, status):
    # Record audio into a numpy array
    if status:
        print(status)
    audio_data = np.frombuffer(indata, dtype=np.int16)

    # Save the captured audio to a temporary WAV file in memory
    wav_io = io.BytesIO()
    write(wav_io, 44100, audio_data)
    wav_io.seek(0)

    # Transcribe the audio using Whisper API
    transcript = openai.Audio.transcribe("whisper-1", file=wav_io)

    # Process the transcription
    command = transcript['text'].strip().lower()
    print(f"Recognized Command: {command}")


# Stream audio from the microphone and process it in real-time
with sd.InputStream(callback=callback, channels=1, samplerate=44100):
    print("Listening...")
    sd.sleep(-1)  # Keeps the script running

