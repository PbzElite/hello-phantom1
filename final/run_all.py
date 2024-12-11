import keyboard

#imports scrape_control class to be easily called
from scrape_control import Scraper

#loop meant to simulate runtime conditions; iterates each time alt is pressed, until ` is pressed (exits loop and stops program)
while not keyboard.is_pressed('`'):
    if keyboard.is_pressed('alt'):
      #code to run in loop starts here
        print(Scraper.scrapeControl('weather', 'na'))
