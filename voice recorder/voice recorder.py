

import sounddevice as sd
import numpy as np
import wave
import keyboard

def record_voice_until_enter(filename):
    # Set the sampling frequency and channels
    fs = 44100  # 44.1 kHz
    channels = 2  # Stereo

    # Initialize recording buffer
    recording = []

    print("Press Enter to start recording...")
    keyboard.wait("enter")

    # Record audio until Enter is pressed again
    with sd.InputStream(samplerate=fs, channels=channels, dtype=np.int16) as stream:
        stream.start()

        print("Recording... Press Enter to stop recording.")
        while True:
            chunk, overflowed = stream.read(1024)
            recording.extend(chunk)
            if keyboard.is_pressed("enter"):
                break

    # Save the recorded audio to a WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)  # 16-bit audio
        wf.setframerate(fs)
        wf.writeframes(np.array(recording).tobytes())

if __name__ == "__main__":
    # Set the filename for the recorded audio
    output_filename = "recorded_voice.wav"

    # Record the voice until Enter is pressed
    record_voice_until_enter(output_filename)

    print(f"Recording saved as {output_filename}")





