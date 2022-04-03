#This program asks the user to input any positive integer.  
#If it is even, divide it by 2; if it is odd, multiply it by 3 and add 1. 
#Program ends when the current value is 1.
#Author : Prasanth Sukumar

inputNumber = int(input("Please enter a positive integer:"))
result = [inputNumber] #a list to save number from each iteration, start with the input number https://stackoverflow.com/questions/57344985/storing-data-from-while-loop-in-array
while (inputNumber > 1): #While loop continue untile the value reaches 1
    if (inputNumber % 2) == 0: #Check if the value is even
        inputNumber = inputNumber/2 #if even, devide by 2
    else:
        inputNumber = (inputNumber*3)+1 #else if odd, multiply by 3 and add 1
    result.append(int(inputNumber)) #append result from each iteration to the list
print(*result) #print the numbers in a single row without brackets https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row