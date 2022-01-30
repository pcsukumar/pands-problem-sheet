#This program is to calculate the BMI when weight (Kg) and height (cm) given.
#Author : Prasanth Sukumar

weight = float(input('Weight (kg): ')) #Asking user to input weight and convert the value into float
height = float(input('Height (cm): ')) #Asking user to input height and convert the value into float

bmi = weight/(height/100)**2  # Calculate BMI

print("Your BMI is (kg/m2): {:.2f}" .format(bmi)) # ':.2f' used to round BMI value to two decimels
