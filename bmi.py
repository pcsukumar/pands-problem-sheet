#This program is to calculate the BMI when weight (Kg) and height (cm) given.
weight = float(input('Weight (kg): '))
height = float(input('Height (cm): '))
bmi = round(weight/(height/100)**2, 2)  # Found how to round to 2 decimal places form this page https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python
print("Your BMI is:", bmi)