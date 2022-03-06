#This program takes a positive floating-point number as input and outputs an approximation of its square root.
#Author: Prasanth Sukumar

#Source: slightly updated the code found here https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d

def sqrt(number, number_iters = 500):
    a = float(number) # number to get square root of
    for i in range(number_iters): # iteration number
        number = 0.5 * (number + a / number) # update , x_(n+1) = 0.5 * (x_n +a / x_n)
    return number

num = float(input("Please enter a positive number:"))
sqroot = sqrt(num)
print("The square root of {} is approx. {:.1f}".format(num, sqroot))