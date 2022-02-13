#This program ask the user to inpurt a string and output every second letter in reverse order.
#Author: Prasanth Sukumar

stringToReverse = input('Please enter a string:') #Asking user to enter a string

reversedString = stringToReverse[::-1] [::2] #How to reverse a sting found on this page; https://www.w3schools.com/python/python_howto_reverse_string.asp
                                             #How to print every second letter found here; https://stackoverflow.com/questions/509211/understanding-slice-notation
                                             #This line of code first reverse the string and then take every second letter from the reversed sting and store in the variable

print('The string reversed is: {}'.format(reversedString)) #Print the reversedString variable 