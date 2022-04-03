## Pands Problem Sheet - README
___
### Week 2 - Calculating BMI
This program is to calculate the BMI when weight (Kg) and height (cm) given.
User inputed values first convert to float, then do the calculations and print the results.     

    
### Week 3 - Extract second letter and print in reverese order
This program ask the user to inpurt a string and output every second letter in reverse order. Python string slicing method is used to do this task.
  
  
### Week 4 - Collatz
This program asks the user to input any positive integer.  
If it is even, divide it by 2; if it is odd, multiply it by 3 and add 1. Program ends when the current value is 1.

An array named 'result' is created with input number as first element. Checks input number is odd or even using modulus operator. A while loop runs untile the value reaches 1. Result from each iteration appends to the 'result' array and finally print the array without brackets in a single line.
  
### Week 5 - Week day
This program checks whether today is a weekday or not and print a message accordingly.
 
This program start with importing date from datetime module. Then gets the day number in the week and if else statement is used to print the text depends on the day number.

### Week 6 - Find approximate square root
This program takes a positive floating-point number as input and outputs an approximation of its square root.  
Variable 'diff' is initated with a large value. A while loop runs until the difference between the square of the guessed number and the actual number is less than 0.05. 


### Week 7 - A program that reads in a text file and outputs the number of e's it contains.
This program reads in a text file and outputs the number of e's it contains. The assumption is that the file may contain both uppercase and lowercase e's. To count all e's irrespective of upper or lower, the progrm first convert the file content to lower case and then read all lowercase e's. The ArgumentParser is used to  take the filename as an argument on the command line.

### Week 8 - Write a program that displays a plot of a function
This program displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.