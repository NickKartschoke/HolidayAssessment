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
           
    #Add a holiday 
    def addHoliday(self,holidayObj):
        try:
            temp = Holiday(holidayObj.name, holidayObj.date)
            self.innerHolidays.append(temp)
            print(f"Successfully added holiday {holidayObj}.")
        except TypeError:
            print("Error: that is not a Holiday object.")

    #Check date *************************************************************?
    def isValidDate(date):
        format = "%Y-%m-%d"
        x = False
        while x == False: 
            try:
                datetime.datetime.strptime(date,format)
                x=True
                return date
            except ValueError:
                print("Invalid date. Please try again.") 
                date = input(str("Date (yyyy-mm-dd): "))

    def findHoliday(self, h):
        for i in self.innerHolidays:
            if i.name == h.name and i.date == h.date:
                return i
            
        return None
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

    def save_to_json():
        with open("holidayList.json", "w") as f:
            json.dump(innerHolidays, f, indent = 1)

        f.close()
        # Write out json file to selected file.

    def scrapeHolidays():
        years = ["2020","2021","2022","2023","2024"]
        months = {"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}

        for i in years:
            url = f"https://www.timeanddate.com/holidays/us/{i}"
            response = requests.get(url).text
                        
            soup = BeautifulSoup(response, 'html.parser')
            holiday_table = soup.find('table',attrs={'id':'holidays-table'})
            for row in holiday_table.find_all_next('tr',attrs={'class':'showrow'}):
                date_tag = row.find('th')           #find the tag with the date in it
                date_text = date_tag.string         #extract the raw string from the tag
                date_month = date_text[0:2]         #extract the 3-letter month code
                date_month = months[date_month]     #convert it to number code based on above dictionary
                date_day = date_text[-2:].strip()   #extract the 2-digit day
                if len(date_day) == 1:              #if day is only 1 digit (eg. '2')
                    date_day = f"0{date_day}"       #convert it to 2-digit format (eg. '02')
                combined_date = f"{i}-{date_month}-{date_day}"  #create formatted date
                
                name_tag = row.find('a')            #find the tag with the holiday name
                name_text = name_tag.string         #extract the string from the tag
                
                holi = Holiday(name_text, combined_date)
                if findHoliday(holi) == False:   #if new holiday is not in the list
                    addHoliday(holi)            #add it to the list
        print("Successfully scraped holiday data for 2020-2024")
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        # Check to see if name and date of holiday is in innerHolidays array
        # Add non-duplicates to innerHolidays
        # Handle any exceptions.     

    def displayHolidaysInWeek(self):
        for i in self.innerHolidays:
            print(str(i))

    def numHolidays(self):
        return print('There are ' + str(len(HolidayList.innerHolidays)) + ' holidays in the file')
        #Return the total number of holidays in innerHolidays
        
    
    def filter_holidays_by_week(year, week_number):

        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays
        pass

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