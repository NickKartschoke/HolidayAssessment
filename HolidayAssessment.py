import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass


# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------
@dataclass
class Holiday:
      
    def __init__(self, name, date):
        name: str
        date: str 
        #Your Code Here        
    
    def __str__ (self):
        return self.name, self.date
        # String output
        # Holiday output when printed.
          
           
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
class HolidayList:
    def __init__(self):
       self.innerHolidays = []

    def isValidDate(date):
        format = "%Y-%m-d"
        x = False
        while x == False: 
            try:
                datetime.datetime.strptime(date,format)
                x=True
                return date
            except ValueError:
                print("Invalid date. Please try again.") 
                date = input(str("Date (yyyy-mm-dd): "))

    def addHoliday(holidayObj):
        innerHolidays = []
        #print("Success:")
        innerHolidays.append(holidayObj)
        #print(Holiday.name + "(" + Holiday.date + ") has been added to the holiday list.")
        #print(type(innerHolidays['0']))
        return innerHolidays
        # Make sure holidayObj is an Holiday Object by checking the type
        # Use innerHolidays.append(holidayObj) to add holiday
        # print to the user that you added a holiday

    def findHoliday(self):
        find_holiday = str(input("What holiday would you like to find? "))
        if find_holiday in HolidayList.innerHolidays:
                Name = find_holiday
                return HolidayList.innerHolidays[Name]
        else:
            print("Could not find " + find_holiday + " in the list")
        # Find Holiday in innerHolidays
        # Return Holiday

    def removeHoliday(name):
        list = HolidayList.addHoliday(name)
        x = False
        while x is False:
            if name in list:
                list.remove[name]
                print(name + "has been removed from the holiday list.")
                x is True
            else:
                print(name + " not found.")
        # Find Holiday in innerHolidays by searching the name and date combination.
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday

    def read_json():
        with open('holidays.json', 'r') as j:
            data=json.loads(j.read())
        HolidayList.addHoliday(data)
        # Read in things from json file location
        # Use addHoliday function to add holidays to inner list.

    #def save_to_json(filelocation):
        # Write out json file to selected file.
        
    def scrapeHolidays():
        holidays = []
        for x in range(2019, 2024):
            html = requests.get("https://www.timeanddate.com/calendar/print.html?year=" + str(x) + "&country=1&hol=33554809&holm=1&df=1").text
            soup = BeautifulSoup(html, "html.parser")

            table = soup.find('table', attrs = {'class': 'cht lpad'})


            for row in table.find_all('tr'):
                cells = row.find_all('td')
                holiday = {}
                holiday['date'] = cells[0].string + " " + str(x)
                holiday['name'] = cells[1].string
                HolidayList.addHoliday(holiday)
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        # Check to see if name and date of holiday is in innerHolidays array
        # Add non-duplicates to innerHolidays
        # Handle any exceptions.     

    def numHolidays(self):
        return print('There are ' + str(len(HolidayList.innerHolidays)) + ' holidays in the file')
        #Return the total number of holidays in innerHolidays
        
    
    #def filter_holidays_by_week(year, week_number):

        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays

    #def displayHolidaysInWeek(holidayList):

        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.

    #def getWeather(weekNum):
        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.

    #def viewCurrentWeek():
        # Use the Datetime Module to look up current week and year
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        # Use your displayHolidaysInWeek function to display the holidays in the week
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results



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
        else:
            print("Canceled")

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
            #week = current week
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
    while exit_valid == False:
        exit = str(input("Are you sure you want to exit? [y/n]"))
        if exit != 'y' and exit != 'n':
            print("Please only enter 'y' or 'n'")
        elif exit =='n':
            print("You will now be directed back to the main menu")              
    return exit
   

def main():
    HolidayList.read_json()
    print("Holiday Management")
    print("===================")
    print("There are 10 holidays stored in the system.")
    print(" ")
    print(" ")
    HolidayList.scrapeHolidays()
    #end_program = False
    #while end_program == False:
    #    choice = mainMenu()
    #    if choice == 1:
    #        choice1()
    #    elif choice == 2:
    #        choice2()
    #    elif choice == 3:
    #        choice3()
    #    elif choice == 4:
    #        choice4()
    #    elif choice == 5:
    #        exit = choice5()
    #        if exit == 'y':
    #            end_program = True
    #    else:
    #        print("Please only enter 1-5")
    
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