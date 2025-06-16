import datetime
import pandas as pd

class eventscrape:
    #input: just a date
    def formatDate(self,prompt):
        #will format the prompts (today,tomorrow,yesterday)
        x = ""
        if prompt.find("today") != -1:
            x = datetime.date.today()
        elif prompt.find("yesterday") != -1:
            x = datetime.date.today() + datetime.timedelta(1)
        elif prompt.find("yesterday") != -1:
            x = datetime.date.today() - datetime.timedelta(1)
        print(f"{x.strftime("%b")} {x.strftime("%d")}")
        return x

    def scrapeEvents(self,month,day):
        eS = pd.read_excel('BBP_March_2025_Events.xlsx')
        text = ""
        prompt = "not2day"

        #TASK: fix logic to get all commands working: today (good),recent (needs checking),yesterday (good) ,tomorrow ( good),specific date (needs to be implemented), maybe even lookup specific events (needs to be implemented)
        if prompt.find("recent") != -1 or prompt.find("today") != -1 or prompt.find("tomorrow") != -1 or prompt.find("yesterday") != -1:
            count = 0
            print(f"225 {self.month[:3]} {self.day[:-2]}")

            for index, row in eS.iterrows():
                if str(row["Date"]).strip() == (f"{self.month[:3]} {self.day[:-2]}"):
                    if count != 0:
                        text += " and "
                    text += str(eS['Title'].iloc[index])
                    count += 1
            if count == 0:
                text = "There are no events"
        else:
            text = "There is a "
            count = 0   
            for index, row in eS.iterrows():
                if str(row["Date"]).strip() == (f"{month[:3]} {day[:-2]}"):
                    if count > 0:
                        text += " and "
                    text += str(eS['Title'].iloc[index])
                    count += 1
        return text
    
        #month arrars, later used
        #full_months = ["January", "February", "March", "April", "May", "June", 
        #    "July", "August", "September", "October", "November", "December"]
        