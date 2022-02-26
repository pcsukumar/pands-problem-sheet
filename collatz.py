#This program asks the user to input any positive integer.  
#If it is even, divide it by 2; if it is odd, multiply it by 3 and add 1. 
#Program ends when the current value is 1.
#Author : Prasanth Sukumar

inputNumber = int(input("Please enter a positive integer:"))
while (inputNumber > 1): #Continue untile the value reaches 1
    if (inputNumber % 2) == 0: #Check if the value is even
        inputNumber = inputNumber/2 #if even, devide by 2
    else:
        inputNumber = (inputNumber*3)+1 #else if odd, multiply by 3 and add 1
    print(int(inputNumber)) #print each iteration