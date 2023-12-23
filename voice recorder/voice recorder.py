

import sounddevice as sd
import numpy as np
import wave
import keyboard

def record_voice_until_enter(filename):
    fs = 44100 
    channels = 2

    recording = []

    print("Press Enter to start recording...")
    keyboard.wait("enter")

    with sd.InputStream(samplerate=fs, channels=channels, dtype=np.int16) as stream:
        stream.start()

        print("Recording... Press Enter to stop recording.")
        while True:
            chunk, overflowed = stream.read(1024)
            recording.extend(chunk)
            if keyboard.is_pressed("enter"):
                break

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)  
        wf.setframerate(fs)
        wf.writeframes(np.array(recording).tobytes())

if __name__ == "__main__":
    output_filename = "recorded_voice.wav" #file name

    record_voice_until_enter(output_filename)

    print(f"Recording saved as {output_filename}")





