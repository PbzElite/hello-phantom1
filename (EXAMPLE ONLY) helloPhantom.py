#Discontinued program meant to run all functions from the other files
#It has been correctly implemented on the Raspberry Pi via running the files in one directory, importing them as methods

import speech_recognition as sr
from text_to_speech import save
import datetime
import requests
from bs4 import BeautifulSoup

class HelloPhantom:

    #Constructor I think (idk I don't know python too well)
    def __init__(self, prompt, date, text):
        self.prompt = ""
        self.date = ""
        self.text = "january first"

    #Uses Vosk speech recognition and an offline language model to transcribe speech
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

    #logic portion of code, takes in the transcribed text and looks for key words
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
            
            monthArr = ["january","february","march","april","may","june","july","august","september","october","november","december"]
            dayArr = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 
                    'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 
                    'eighteenth', 'nineteenth', 'twentieth', 'twenty-first', 'twenty-second', 'twenty-third', 
                    'twenty-fourth', 'twenty-fifth', 'twenty-sixth', 'twenty-seventh', 'twenty-eighth', 
                    'twenty-ninth', 'thirtieth', 'thirty-first']

            for i in range(len(monthArr)):
                if month == monthArr[i]:
                    monthNum = i + 1

            for i in range(len(dayArr)):
                if day == dayArr[i]:
                    dayNum = i + 1
            
            current = datetime.date.today() 
            self.date = (current.year, monthNum, dayNum)
                
            if time == "today":
                self.date = datetime.date.today()
            elif time == "yesterday":
                self.date = datetime.date.today() - datetime.timedelta(days=1)
            elif time == "tomorrow":
                self.date = datetime.date.today() + datetime.timedelta(days=1)

    #webscraper, gets information from websites
    def webscraper():

        url = "https://www.wunderground.com/weather/us/ny/bayport/"

        input = "2024-05-10"
        today = date.today()
        tomorrow = today + timedelta(days=1)

        if input != str(today) and input != str(today):

            url = f"https://www.wunderground.com/hourly/us/ny/bayport/KISP/date/{input}"

        html = requests.get(url).content

        soup = BeautifulSoup(html, 'html.parser')

        # print(soup.prettify())

        if input == str(today):
            temperature = soup.find('div', attrs={'class': 'current-temp'}).text
            hilo = soup.find('div', attrs={'class': 'hi-lo'}).text
            blurb = soup.findAll('div', attrs={'class': 'columns small-6 medium-12'})

            blurb = blurb[1].text
            #print(blurb)
            percent, amount, high, wind = blurb.split(". ", 3)
            percent = percent.split(" ")
            amount = amount.split("°")
            wind = wind[0].lower() + wind[1:]
            hilo = hilo.split(" | ")

            print(f"The current temperature is {temperature}. The high is {hilo[0]} and the low is {hilo[1]}. The chance of rain is {percent[0]}. The amount of rain today is {amount[0].replace('/ ', '').strip()} inches. Current {wind.replace('winds ', 'winds are ')} ")

        elif input == str(tomorrow):
            next = soup.findAll('div', attrs={'class': 'hook'})
            next = next[0]
            print(f"{next}")

    #Uses an offline text-to-speech library and saves it as a .mp3 file (can be played with a later playsound call from playsound3)
    def tts():
        text = "Hello"
        language = "en"  # Specify the language (IETF language tag)
        output_file = "output.mp3"  # Specify the output file (only accepts .mp3)

        save(text, language, file=output_file)


#Finished product would look something along the lines of (current methods don't have arguments nor return statements, these are conceptual):
#input = stt()
#intent = recognizer(input)
#result = webscrape(intent)
#tts(result)

