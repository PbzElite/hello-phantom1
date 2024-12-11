import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta

class WeatherScrape:
	#token is the passed argument from scrape_control.py (the target date, in this case)
	def scrapeWeather(token):
		today = date.today()
		tomorrow = today + timedelta(days=1)

		#determines if they asked for today, and/or if the requested date is the same date as today 
		if(token == 'today' or (type(token) is date and token == today)):
			#spits weather html into a soup object
			url = "https://www.wunderground.com/weather/us/ny/bayport/"
			html = requests.get(url).content
			soup = BeautifulSoup(html, 'html.parser')

			#turns soup object into array of <a> objects, the 30th of which contains the target information (today's weather)
			ps = soup.find_all('a')
			#return the 30th <a> as plaintext
			return ps[29].text

		#same as today code, but with tomorrow's values and <a> locker
		elif(token == 'tomorrow' or (type(token) is date and token == tomorrow)):
			url = "https://www.wunderground.com/weather/us/ny/bayport/"
			
			html = requests.get(url).content
			soup = BeautifulSoup(html, 'html.parser')
			
			ps = soup.find_all('a')
			return ps[32].text
	
	
	#meant for diagnostic use, prints the entire array of <a> objects in plaintext w/ locker numbers, and prints the return statement
	def scrapeWeatherWithDiagnostics(token):
		today = date.today()
		tomorrow = today + timedelta(days=1)

		if(token == 'today' or (type(token) is date and token == today)):
			url = "https://www.wunderground.com/weather/us/ny/bayport/"
			
			html = requests.get(url).content
			soup = BeautifulSoup(html, 'html.parser')
			
			ps = soup.find_all('a')
			i = 0
			for p in ps:
				print(str(i) + ' ' + p.text)
				i += 1
			
			print(ps[29].text)
			return ps[29].text
		
		elif(token == 'tomorrow' or (type(token) is date and token == tomorrow)):
			url = "https://www.wunderground.com/weather/us/ny/bayport/"
			
			html = requests.get(url).content
			soup = BeautifulSoup(html, 'html.parser')
			
			ps = soup.find_all('a')
			return ps[32].text

	#obligatory diagnostic main
	if __name__ == "__main__":
		scrapeWeatherWithDiagnostics('today')
