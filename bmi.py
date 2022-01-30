#This program is to calculate the BMI when weight (Kg) and height (cm) given.
#Author : Prasanth Sukumar

weight = float(input('Weight (kg): ')) #Asking user to input weight and convert the value into float
height = float(input('Height (cm): ')) #Asking user to input height and convert the value into float

bmi = round(weight/(height/100)**2, 2)  # Found how to round to 2 decimal places form this page https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python

print("Your BMI is:{}" .format(bmi))
