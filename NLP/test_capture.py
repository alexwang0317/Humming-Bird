import sounddevice as sd
import numpy as np

print(sd.query_devices())


sample_rate = 16000
duration = 5  # Record for 5 seconds

sd.default.device = 'MacBook Pro Microphone'



def callback(indata, frames, time, status):
    if status:
        print(status)
    print("Captured audio data (first 10 samples):", indata[:10])

print("Recording...")
with sd.InputStream(callback=callback, channels=1, samplerate=sample_rate, blocksize=2048):
    sd.sleep(duration * 1000)
