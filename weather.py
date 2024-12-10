import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta

class ScrapeWeather:
	def scrapeWeather(token):
		today = date.today()
		tomorrow = today + timedelta(days=1)
		
		if(token == 'today' or (type(token) is datetime and token == today)):
			url = "https://www.wunderground.com/weather/us/ny/bayport/"
			
			input = "2024-12-10"
			today = date.today()
			tomorrow = today + timedelta(days=1)
			
			html = requests.get(url).content
			soup = BeautifulSoup(html, 'html.parser')
			
			ps = soup.find_all('a')
			return ps[29].text

	def scrapeWeatherWithDiagnostics(token):
		today = date.today()
		tomorrow = today + timedelta(days=1)
		
		if(token == 'today' or (type(token) is datetime and token == today)):
			url = "https://www.wunderground.com/weather/us/ny/bayport/"
			
			input = "2024-12-10"
			today = date.today()
			tomorrow = today + timedelta(days=1)
			
			html = requests.get(url).content
			soup = BeautifulSoup(html, 'html.parser')
			
			ps = soup.find_all('a')
			i = 0
			for p in ps:
				print(str(i) + ' ' + p.text)
				i += 0
			
			print(ps[29].text)
			return ps[29].text

	if __name__ == "__main__":
		scrapeWeatherWithDiagnostics()
