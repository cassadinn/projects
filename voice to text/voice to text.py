import speech_recognition as sr

def convert_voice_to_text(input_file, output_file):
    recognizer = sr.Recognizer()

    audio_file = sr.AudioFile(input_file)

    with audio_file as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        print("Transcription: ", text)

        with open(output_file, 'w') as out_file:
            out_file.write(text)

        print(f"Transcription saved to {output_file}")

    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")

if __name__ == "__main__":
    input_file = "example.wav"  #file you want to transform
    output_file = "text.txt"    #the file 

    convert_voice_to_text(input_file, output_file)
