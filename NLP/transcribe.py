import sounddevice as sd
import numpy as np
import whisper

class AudioRecorder:
    def __init__(self, model_name='base', device_name='MacBook Pro Microphone', sample_rate=16000, duration=10, amplification_factor=10.0):
        # Load the Whisper model
        self.model = whisper.load_model(model_name)
        # Set the recording device
        sd.default.device = device_name
        # Set the audio parameters
        self.sample_rate = sample_rate
        self.duration = duration
        self.amplification_factor = amplification_factor
        self.audio_data = []

    def callback(self, indata, frames, time, status):
        """This function is called for each audio block."""
        if status:
            print(status, flush=True)
        # Append the audio data to the list
        self.audio_data.append(indata.copy())

    def record_audio(self):
        """Start recording audio."""
        print("Listening... Press Ctrl+C to stop.")
        try:
            with sd.InputStream(callback=self.callback, channels=1, samplerate=self.sample_rate):
                while True:
                    sd.sleep(int(self.duration * 1000))
        except KeyboardInterrupt:
            print("Stopping...")

    def process_audio(self):
        """Process the recorded audio."""
        # Convert the list of audio data to a single numpy array
        audio_data = np.concatenate(self.audio_data, axis=0).flatten()

        # Normalize the audio data based on peak volume
        max_val = np.max(np.abs(audio_data))
        if max_val > 0:
            audio_data /= max_val

        # Optionally amplify the audio signal if needed
        audio_data *= self.amplification_factor

        # Ensure the amplified data is within the expected range
        audio_data = np.clip(audio_data, -1.0, 1.0)

        return audio_data

    def transcribe_audio(self, audio_data):
        """Transcribe the processed audio data."""
        result = self.model.transcribe(audio_data, fp16=False)
        transcription = result['text']
        return transcription

    def run(self):
        """Run the full audio recording and transcription process."""
        self.record_audio()
        processed_audio = self.process_audio()
        transcription = self.transcribe_audio(processed_audio)
        print("Transcription:")
        return transcription

# Instantiate the AudioRecorder class and run it
audio_recorder = AudioRecorder()
audio_recorder.run()