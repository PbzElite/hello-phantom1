#imports the weather webscraper from the webscrape folder (when several webscraper files are added, it may be better to streamline them using an __init__.py file in the webscraper folder)
from webscrape.weather import WeatherScrape

#defines the class to be called by run_all.py, which takes up to 2 args (can be increased if needed)
class Scraper:
#arg1 chooses the webscraper
#arg2+ are parameters to pass to the webscraper (e.g. 'today', 'tomorrow')
    def scrapeControl(arg1, arg2):
        if arg1 == 'weather':
            if arg2 == 'na':
                return WeatherScrape.scrapeWeather('today')
            else:
                 return WeatherScrape.scrapeWeather(arg2)

#main for test purposes
    if __name__ == "__main__":
        print('main executed')
        print(scrapeControl('weather', 'today'))
            
    
