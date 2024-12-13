#from vosk import 


import pyaudio
import speech_recognition as sr




class stt:

    def voskRecognize():
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Say something!")
            audio = r.listen(source, 10, 3)
            
        try:
            print(r.recognize_vosk(audio))
        except sr.UnknownValueError:
            print("what are you doing")
        
    if __name__ == "__main__":
        voskRecognize()
