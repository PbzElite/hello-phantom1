import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta

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

    

