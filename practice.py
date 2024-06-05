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

'''
#Added the events of a calendar, requires some tweaking
# URL of the events page
url = "https://www.bbpschools.org/o/bbphs/events"
input = "What are the recent events"

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if input.find("event") && response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the container that holds the events
    events_container = soup.find_all('div', class_='events-container')  # Adjust the class based on the actual HTML structure
    print(events_container)
    
    # Iterate over each event and extract relevant details
    for event in events_container:
        title = event.find('div', class_='title').text.strip() if event.find('div', class_='title') else 'No Title'
        date = event.find('div', class_='month').text.strip() if event.find('div', class_='month') else 'No Date'
        date += " " + event.find('div', class_='day').text.strip() if event.find('div', class_='day') else 'No Date'
        time = event.find('div', class_='hour').text.strip() if event.find('div', class_='hour') else 'No Time'
        location = event.find('div', class_='venue').text.strip() if event.find('div', class_='venue') else 'No Location'

        # Print the extracted details
        print(f"Title: {title}")
        print(f"Date: {date}")
        print(f"Time: {time}")
        print(f"Location: {location}")
        print("-" * 40)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
'''
