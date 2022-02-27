#This program checks whether today is a weekday or not and print a message accordingly.
#Author : Prasanth Sukumar

from datetime import date #import date from datetime module https://docs.python.org/3/library/datetime.html
today=date.today().weekday() # Return the day of the week as an integer, where Monday is 0 and Sunday is 6
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday") #A tuple is created with days of week
todayString = weekDays[today] #Extract the day of week as a string based on the 'today' value
if todayString == "Saturday" or todayString == "Sunday": #if statement is used to print the message according to the name of the week day
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")

