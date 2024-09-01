import sounddevice as sd
import numpy as np
import whisper

# Load the Whisper model
model = whisper.load_model("base")

# Setting device. Change this to the appropriate device for your system, found in bluetooth. 
sd.default.device = 'MacBook Pro Microphone'


# Define audio parameters
sample_rate = 16000
duration = 10  # Duration of each audio segment in seconds
audio_data = []

def callback(indata, frames, time, status):
    """This function will be called for each audio block."""
    if status:
        print(status, flush=True)
    
    # Append the audio data to the list
    audio_data.append(indata.copy())

# Start the audio stream
print("Listening... Press Ctrl+C to stop.")
try:
    with sd.InputStream(callback=callback, channels=1, samplerate=sample_rate):
        while True:
            sd.sleep(int(duration * 1000))
except KeyboardInterrupt:
    print("Stopping...")

# Convert the list of audio data to a single numpy array
audio_data = np.concatenate(audio_data, axis=0).flatten()

# Normalize the audio data based on peak volume
max_val = np.max(np.abs(audio_data))
if max_val > 0:
    audio_data /= max_val

# Optionally amplify the audio signal if needed
amplification_factor = 10.0  # Adjust as needed
audio_data *= amplification_factor

# Ensure the amplified data is within the expected range
audio_data = np.clip(audio_data, -1.0, 1.0)

# Transcribe the audio data
result = model.transcribe(audio_data, fp16=False)
transcription = result['text']

# Output the transcription
print("Transcription:")
print(transcription)
