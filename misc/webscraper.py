
import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
from Event import *

#used at one point to convert string to date
def convert_string_to_date(date_str,year=2024):
    date_obj = datetime.datetime.strptime(date_str, "%b %d")
    full_date = datetime.date(year,date_obj.month,date_obj.day)
    return full_date

def webscrape(intent, string):
    if (intent == "weather"):
        url = "https://www.wunderground.com/weather/us/ny/bayport/"

        input = string
        today = date.today()
        tomorrow = today + timedelta(days=1)

        if input != str(today) and input != str(today):

            url = f"https://www.wunderground.com/hourly/us/ny/bayport/KISP/date/{input}"

        html = requests.get(url).content

        soup = BeautifulSoup(html, 'html.parser')
        
        #print("DIAGNOSTIC:")
        #print(soup.find('p').text)


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

            return (f"The current temperature is {temperature}. The high is {hilo[0]} and the low is {hilo[1]}. The chance of rain is {percent[0]}. The amount of rain today is {amount[0].replace('/ ', '').strip()} inches. Current {wind.replace('winds ', 'winds are ')} ")

        elif input == str(tomorrow):
            next = soup.findAll('div', attrs={'class': 'hook'})
            next = next[0]
            #print(f"{next}")
    elif (intent == "calendar" or intent.find("event") != -1):

        #month,day arrays, used for finding events on certain days
        monthArr = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        dayArr = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
        full_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        low_months = [month.lower() for month in monthArr]
        # List of first three letters of each month
        short_months = [month[:3] for month in monthArr]
        
        #will be returned later
        text = ""
        #Added the events of a calendar, requires some tweaking
        # URL of the events page, making it run yearlong by going 2 weeks ago to a little over a month
        startdate = datetime.date.today() - datetime.timedelta(days=14)
        enddate = datetime.date.today() + datetime.timedelta(days=40)
        start = datetime.date(startdate.year,startdate.month,startdate.day)
        end = datetime.date(enddate.year,enddate.month,enddate.day)
        url = f"https://bayportbluepointny.sites.thrillshare.com/events?start_date={start}&end_date={end}&filter_ids=327083,327083,325682"
        #input = "What are the recent events"

        # Send a GET request to the webpage
        response = requests.get(url)

        # Check if the request was successful and see if the input is asking for events
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the container that holds the events
            events_container = soup.find_all('div', class_='event-list-item')  # Adjust the class based on the actual HTML structure
            #print(events_container)

            recentEvents = []
                      
            #I kept these but wasn't sure what route we'll end up going down -Shlok
            index = 0
            minDiff = 100
            # Iterate over each event and extract relevant details
            for event in events_container:
                title = event.find('div', class_='title').text.strip() if event.find('div', class_='title') else 'No Title'
                day = event.find('div', class_='month').text.strip() if event.find('div', class_='month') else 'No Day'
                day += " " + event.find('div', class_='day').text.strip() if event.find('div', class_='day') else 'No Day'
                time = event.find('div', class_='hour').text.strip() if event.find('div', class_='hour') else 'No Time'
                location = event.find('div', class_='venue').text.strip() if event.find('div', class_='venue') else 'No Location'


#                month = ""
 #               day = -1
  #              for months in monthArr:
   #                 if months.lower() == string[:month.find(months)]:
    #                    month = i+1 
                        
                #Event is a class created, the return statement of the Event object is the sentence / info about it
                recentEvents.append(Event(str(title),str(day),str(location)))
                
                if string.find("recent") != -1:
                    text = "current events include "
                    count = 0

                    for event in recentEvents:
                        for i in range(len(short_months)):
                            if(event.getDate()[:3] == short_months[i]):
                                num = int(event.getDate()[event.getDate().find(" ")+1:])
                                compDate = datetime.date(datetime.date.today().year,i+1,num)
                                if(count<3 and compDate >= datetime.date.today()):
                                    text += f"{event}"
                                    count+=1
                                break
                elif(string.find("tomorrow") != -1):
                    text = "Tomorrows events are "
                    count = 0
                    
                    #TASK: if the next day is not the same date as the target date, then it could end. 
                    for event in recentEvents:
                        if(count <3):
                            for i in range(len(short_months)):
                                if(event.getDate()[:3] == short_months[i]):
                                    num = int(event.getDate()[event.getDate().find(" ")+1:])
                                    cdate = datetime.date.today() + timedelta(days=1)
                                    compDate = datetime.date(cdate.year,cdate.month,cdate.day)
                                    
                                    if(compDate == convert_string_to_date(str(event.getDate()))):
                                        text += f"{event}"
                                        count+=1
                                        break
                                    else:
                                        break
                        else:
                            break
                    if count == 0:
                        text = "There are no events tomorrow"
                elif(string.find("yesterday") != -1):
                    text = "Yesterday's events were "
                    count = 0
                    
                    for event in recentEvents:
                        if(count <3):
                            for i in range(len(short_months)):
                                if(event.getDate()[:3] == short_months[i]):
                                    num = int(event.getDate()[event.getDate().find(" ")+1:])
                                    cdate = datetime.date.today() - timedelta(days=1)
                                    compDate = datetime.date(cdate.year,cdate.month,cdate.day)
                                    
                                    if(compDate == convert_string_to_date(str(event.getDate()))):
                                        text += f"{event}"
                                        count+=1
                                        break
                                    else:
                                        break
                        else:
                            break
                    if count == 0:
                        text = "There are no events yesterday"
                elif(string.find("today") != -1):
                    text = "todays events include "
                    count = 0

                    for event in recentEvents:
                        for i in range(len(short_months)):
                            if(event.getDate()[:3] == short_months[i]):
                                num = int(event.getDate()[event.getDate().find(" ")+1:])
                                compDate = datetime.date(datetime.date.today().year,i+1,num)
                                if(count<3 and compDate == datetime.date.today()):
                                    text += f"{event}"
                                    count+=1
                                break
                    if count == 0:
                        text = "There are no events today"
                else:
                    text = "The events on that day are "
                    count = 0

                    #TASK: string october seventh or twelve to convert into datetime.date
                                
                    # Create an array of corresponding numbers
                    days_numbers = list(range(1, 32))
                                    
                    days_string = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth", "twenty-first", "twenty-second","twenty-third", "twenty-fourth", "twenty-fifth", "twenty-sixth", "twenty-seventh", "twenty-eighth", "twenty-ninth", "thirtieth", "thirty-first"]

                    monthNum = -1
                    
                    #need logic for converting
                    
                    #compDate = datetime.date(datetime.date.today().year,i+1,num)

                    for event in recentEvents:
                        for i in range(len(short_months)):
                            if(event.getDate()[:3] == short_months[i]):
                                num = int(event.getDate()[event.getDate().find(" ")+1:])
                                datelook = datetime.date(2024,i+1,num)


                                # Loop through the array using array[i]
                                for i in range(len(days_strings)):
                                    print(f"205 {string[string.find(' ')+1]}")
                                    if days_strings[i] == string[string.find(" ")+1]:
                                        string = days_numbers[i]
                                        break

                                # Loop through the array using array[i]
                                for i in range(len(low_months)):
                                    print(f"205 {string[0:string.find(' ')+1]}")
                                    if low_months[i] == string[0:string.find(" ")+1]:
                                        day = datetime.date(2024,i,string)
                                        break
                                            
                                    
                                        
                                compDate = day
                                if(count<3 and compDate == datelook):
                                    text += f"{event}"
                                    count += 1
                                break
                    if count == 0:
                        text = "There are no events on that day"
            #print(f"{text}")
            return text
"""code from before, this is a totally viable option as well
                # Print the extracted details
                print(f"Title: {title}")
                print(f"Day: {day}")
                print(f"Time: {time}")
                print(f"Location: {location}") if location.strip() != "" else print("")
                print("-" * 40)
                
                print(int(day.split(" ")[1]))
                print(int(str(string).split("-")[2]))
                
                difference = abs(int(day.split(" ")[1]) - int(str(string).split("-")[2]))
                print("Difference: " + str(difference))
                if (difference < minDiff):
                    minDiff = difference
                    mindex = index
                    print("Closest event to time has been updated to " + str(difference) + " at locker " + str(index))
                    theTitle = title 
                    theDate = day
                    theTime = time
                index += 1
            #theEvent = events_container[mindex]
            return f"There is {theTitle} on {theDate} at {theTime}"
"""
"""          
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            
        index = 0
        for event in recentEvents:
            print(f"Current events include: {title} on  {date} at  {time}")
            difference = abs(int(date.split(" ")[1]) - int(string.split("-")[0]))
            print("Difference: " + difference)
            if (difference < minDiff):
                minDiff = difference
                print("Closest event to time has been updated to " + difference + " at locker " + index)
            index += 1
         
"""       
        #return

    

    
if __name__ == "__main__":
    print(webscrape("weather", date.today() + timedelta(days=1)))
