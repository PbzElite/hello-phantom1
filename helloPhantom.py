import speech_recognition as sr
from text_to_speech import save
import datetime

class HelloPhantom:
    
    def __init__(self, prompt, date, text):
        self.prompt = ""
        self.date = ""
        self.text = "january first"
        
    def stt():
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Say something!")
            audio = r.listen(source)
            
        try:
            self.text = r.recognize_vosk(audio, show_All=True)
        except sr.UnknownValueError:
            print("what are you doing")

    def tts():
        text = "Hello"
        language = "en"  # Specify the language (IETF language tag)
        output_file = "output.mp3"  # Specify the output file (only accepts .mp3)

        save(text, language, file=output_file)
        
    def recognizer():
        string = self.text
        words = string.split(' ')

        for i in range(len(words)):
            if words[i] == "weather" or words[i] == "temperature" or words[i] == "calendar" or words[i] == "events" or words[i] == "announcements":
                self.prompt = words[i]
                break
            else:
                self.prompt = "not found"
        print(prompt)

        for i in range(len(words)):
            if words[i] == "yesterday" or words[i] == "today" or words[i] == "tomorrow":
                time = words[i]
                break
            elif words[i] == "january" or words[i] == "february" or words[i] == "march" or words[i] == "april" or words[i] == "may" or words[i] == "june" or words[i] == "july" or words[i] == "august" or words[i] == "september" or words[i] == "october" or words[i] == "november" or words[i] == "december":
                month = words[i]
                if words[i+1] == "first" or words[i+1] == "second" or words[i+1] == "third" or words[i+1] == "fourth" or words[i+1] == "fifth" or words[i+1] == "sixth" or words[i+1] == "seventh" or words[i+1] == "eighth" or words[i+1] == "ninth" or words[i+1] == "tenth" or words[i+1] == "eleventh" or words[i+1] == "twelfth" or words[i+1] == "thirteenth" or words[i+1] == "fourteenth" or words[i+1] == "fifteenth" or words[i+1] == "sixteenth" or words[i+1] == "seventeenth" or words[i+1] == "eighteenth" or words[i+1] == "nineteenth" or words[i+1] == "twentieth" or words[i+1] == "twenty-first" or words[i+1] == "twenty-second" or words[i+1] == "twenty-third" or words[i+1] == "twenty-fourth" or words[i+1] == "twenty-fifth" or words[i+1] == "twenty-sixth" or words[i+1] == "twenty-seventh" or words[i+1] == "twenty-eighth" or words[i+1] == "twenty-ninth" or words[i+1] == "thirtieth" or words[i+1] == "thirty-first":
                    day = words[i+1]
                    break
            else:
                self.date = datetime.date.today()
            
            #simplified code for the month and day system
            monthArr = ["january","february","march","april","may","june","july","august","september","october","november","december"]
            dayArr = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 
                    'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 
                    'eighteen', 'nineteen', 'twenty', 'twenty-one', 'twenty-two', 'twenty-three', 
                    'twenty-four', 'twenty-five', 'twenty-six', 'twenty-seven', 'twenty-eight', 
                    'twenty-nine', 'thirty', 'thirty-one']
            
            for i in range(len(monthArr)):
                if month == monthArr[i]:
                    monthArr = i + 1
 
            for i in range(len(dayArr)):
                if day == dayArr[i]:
                    dayArr = i + 1
            
            current = datetime.date.today() 
            self.date = (current.year, monthNum, dayNum)
                
            if time == "today":
                self.date = datetime.date.today()
            elif time == "yesterday":
                self.date = datetime.date.today() - datetime.timedelta(days=1)
            elif time == "tomorrow":
                self.date = datetime.date.today() + datetime.timedelta(days=1)

