#This program is to calculate the BMI when weight (Kg) and height (cm) given.
#Author : Prasanth Sukumar

weight = float(input('Weight (kg): ')) #Asking user to input weight and convert the value into float (ref 1)
height = float(input('Height (cm): ')) #Asking user to input height and convert the value into float

bmi = weight/(height/100)**2  # Calculate BMI

print("Your BMI is (kg/m2): {:.2f}" .format(bmi)) # ':.2f' used to round BMI value to two decimels

#References
# 1. Python float() Function https://www.w3schools.com/python/ref_func_float.asp
# 2. How to display 2 decimal places in Python https://tutorial.eyehunts.com/python/how-to-display-2-decimal-places-in-python-example-code/