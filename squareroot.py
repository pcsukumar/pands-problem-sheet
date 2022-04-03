#This program takes a positive floating-point number as input and outputs an approximation of its square root.
#Author: Prasanth Sukumar

#Source: slightly updated the code found here https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d

def sqrt(number):
    a = float(number) # number to get square root of
    diff = 99999999   # set a big number as difference
    while diff > 0.05: # iterate until difference between original number and squrare of guessed number is less than 0.05
        number = 0.5 * (number + a / number) # update using newtowns method x_(n+1) = 0.5 * (x_n +a / x_n)
        diff = abs(number**2-a)
    return number

num = float(input("Please enter a positive number:"))
sqroot = sqrt(num)
print("The square root of {} is approx. {:.1f}".format(num, sqroot))