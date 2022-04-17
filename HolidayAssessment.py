import datetime
import json
import os
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass


@dataclass
class Holiday:
    
    name: str
    date: datetime.datetime
    
    def __str__ (self):
        return f"{self.name} ({self.date})"
                   
class HolidayList:
    def __init__(self):
        self.innerHolidays = []
           
    #CHECK DATE *************************************************************
    def isValidDate(date):
        format = "%Y-%m-%d"
        x = False
        while x == False: 
            try:
                datetime.datetime.strptime(date,format)
                x=True
                return date
            except ValueError:
                date = input(str("Error: Please try again. Use form (yyyy-mm-dd): "))

    #Add a holiday 
    def addHoliday(self,holidayObj):
        try:
            temp = Holiday(holidayObj.name, holidayObj.date)
            self.innerHolidays.append(temp)
            print(f"Successfully added holiday {holidayObj}")
        except TypeError:
            print("Error: Wrong type")

    #Find a holiday
    def findHoliday(self, HolidayName, Date):
        for i in self.innerHolidays:
            if i.name == HolidayName and i.date == Date:
                return i
        return None

    #Remove a holiday
    def removeHoliday(self, name, date):
        holiday = self.findHoliday(name, date)
        if holiday != None:
            self.innerHolidays.remove(holiday)
            print(f"Successfully removed {holiday}")
        else:
            print(f"Error:{name} is not on {date}")

    #Read in holidays.json
    def read_json(self, file):
        try:
            f = open(file, "r")
            reader = f.read()
            holidays = json.loads(reader)
            holidayDict = holidays['holidays']
        except:
            print(f"Error: Could not open or load file")
            return

        for i in holidayDict:
            h = Holiday(i["name"],datetime.datetime.fromisoformat(i["date"]))
            found = self.findHoliday(h.name, h.date)
            if not found:
                print(f"Error: Could not add holiday '{h}'")
                return
        f.close()

    #Save to json
    def save_to_json(self):
        with open("holidayList.json", "w") as f:
            json.dump(self.innerHolidays, f, indent = 1)

        f.close()

    #Web Scrape all holidays
    def scrapeHolidays(self):
        yearList = ["2020","2021","2022","2023","2024"]
        monthDict = {"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
        for i in yearList:
            url = f"https://www.timeanddate.com/holidays/us/{i}"
            response = requests.get(url)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            holidayTable = soup.find('tbody')
            
            for row in holidayTable.find_all('tr'):
                if 'hol_' not in row.get('id'):
                    htmlDate = row.find('th').string[0:3]
                    month = monthDict[htmlDate]
                    day = htmlDate[-2:].strip()
                    if len(day) == 1:
                        day = f"0{day}"
                    fullDate = f"{i}-{month}-{day}"
                    date = datetime.datetime.fromisoformat(fullDate)
                    findName = row.find('a')
                    name = findName.string
                    if self.findHoliday(name, date) == False:
                        holiday = Holiday(name, date)
                        self.addHoliday(holiday)

    def displayHolidaysInWeek(self):
        for i in self.innerHolidays:
            print(str(i))

    def numHolidays(self):
        return print('There are ' + str(len(HolidayList.innerHolidays)) + ' holidays in the file')
        #Return the total number of holidays in innerHolidays
        
    #Filter by week to get all of the holidays for a specific week of the year
    def filter_holidays_by_week(self, year, week_number):

        while week_number < 1 or week_number > 52:
            week_number = str(input("Which week? #[1-52, Leave blank for current week]: "))
            if week_number == "":
                my_date = datetime.date.today()
                week_number = my_date.isocalendar().week
                week_number = int(week_number)
        yearList = list(filter(lambda x: x.date.year == year, self.innerHolidays))
        weekList = list(filter(lambda x: x.date.isocalendar().week == week_number, yearList))
        return weekList

    def displayHolidaysInWeek(holidayList):
        for i in holidayList:
            print(str(i))
        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.

    def getWeather(weekNum):
        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.
        pass

    def viewCurrentWeek():
        # Use the Datetime Module to look up current week and year
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        # Use your displayHolidaysInWeek function to display the holidays in the week
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results
        pass


def mainMenu():
    print("Holiday Menu")
    print("================")
    print("1. Add a Holiday")
    print("2. Remove a Holiday")
    print("3. Save Holiday List")
    print("4. View Holidays")
    print("5. Exit")
    valid = False
    while valid == False:
        go =  int(input("Where would you like to go (1-5) "))
        goes= str(go)
        if goes.isnumeric():
            valid == True,
            return go
        else:
            continue

def choice1():
    print("Add a Holiday")
    print("=============")
    Name = input(str("Holiday: "))
    Date = input(str("Date (yyyy-mm-dd): "))
    HolidayList.isValidDate
    holidayObj = [Name, Date]
    HolidayList.addHoliday(holidayObj)
    print("The holiday " + Name + " on " + Date + " has been added to the calendar")

def choice2():
        print("Remove a Holiday")
        print ("================")
        name = str(input("Holiday Name: "))
        Date = input(str("Date (yyyy-mm-dd): "))
        HolidayList.isValidDate
        HolidayList.removeHoliday(name)
        print('The holiday ' + name + 'on ' + Date + ' has been removed from the calendar')

def choice3():
    print("Saving Holiday List")
    print("====================")
    answer = 'n'
    while answer != 'y':
        answer = str(input("Are you sure you want to save your changes? [y/n]"))
        if answer != 'y' and answer != 'n':
            print("Please only enter 'y' or 'n'")
        elif answer == 'y':
            HolidayList.save_to_json()
            print("Success: ")
            print("Your changes have been saved.")
            return
        else:
            print("Canceled")
            return

def choice4():
    print("View Holidays")
    print("=================")
    year = 0
    while year not in range(2019, 2024):
        year = int(input("Which year?: "))
        if year not in range(2019, 2023):
            print("Only the years 2019-2023 are loaded. Please enter a valid year")
    valid = False
    while valid == False:
        week = str(input("Which week? #[1-52, Leave blank for current week]: "))
        if week == "":
            my_date = datetime.date.today()
            week = year, week_num, day_of_week = my_date.isocalendar()
            week = int(week)
            holidayList = [week, year]
            HolidayList.displayHolidaysInWeek(holidayList)
            valid_weather = False
            while valid_weather == False:
                weather = str(input("Would you like to see this week's weather? [y/n]: "))
                if weather != 'y' and weather !='n':
                    print("Please only enter 'y' or 'n'")
                elif weather == 'y':
                    HolidayList.getWeather(week)
                    valid_weather == True
                else:
                    valid_weather == True
            print("These are the holidays for this week:")

            break
        week = int(week)
        if week in range (1, 53):
            holidayList = [week, year]
            print("These are the holidays for " + str(year) + " week #" + str(week) + " :")
            HolidayList.displayHolidaysInWeek(holidayList)
            break
        else:
            print("Please enter a valid week")
            continue  
    HolidayList.filter_holidays_by_week(year, week)
def choice5():
    print("Exit")
    print("=====")
    exit_valid = False
    while not exit_valid:
        exit = str(input("Are you sure you want to exit? [y/n]"))
        if exit != 'y' and exit != 'n':
            print("Please only enter 'y' or 'n'")
        elif exit =='n':
            print("You will now be directed back to the main menu") 
            exit_valid = True
        else: 
            exit_valid = True
    return exit
   

def main():
    HolidayList.read_json()
    print("Holiday Management")
    print("===================")
    print("There are 10 holidays stored in the system.")
    print(" ")
    print(" ")
    HolidayList.scrapeHolidays()
    end_program = False
    while end_program == False:
        choice = mainMenu()
        if choice == 1:
            choice1()
        elif choice == 2:
            choice2()
        elif choice == 3:
            choice3()
        elif choice == 4:
            choice4()
        elif choice == 5:
            exit = choice5()
            if exit == 'y':
                end_program = True
        else:
            print("Please only enter 1-5")
    
    # Large Pseudo Code steps
    # -------------------------------------
    # 1. Initialize HolidayList Object
    # 2. Load JSON file via HolidayList read_json function
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    # 3. Create while loop for user to keep adding or working with the Calender
    # 4. Display User Menu (Print the menu)
    # 5. Take user input for their action based on Menu and check the user input for errors
    # 6. Run appropriate method from the HolidayList object depending on what the user input is
    # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 


if __name__ == "__main__":
    main();
    #


# Additional Hints:
# ---------------------------------------------
# You may need additional helper functions both in and out of the classes, add functions as you need to.
#
# No one function should be more then 50 lines of code, if you need more then 50 lines of code
# excluding comments, break the function into multiple functions.
#
# You can store your raw menu text, and other blocks of texts as raw text files 
# and use placeholder values with the format option.
# Example:
# In the file test.txt is "My name is {fname}, I'm {age}"
# Then you later can read the file into a string "filetxt"
# and substitute the placeholders 
# for example: filetxt.format(fname = "John", age = 36)
# This will make your code far more readable, by seperating text from code.