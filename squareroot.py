#This program takes a positive floating-point number as input and outputs an approximation of its square root.
#Author: Prasanth Sukumar

#Source: slightly updated the code found in this video https://www.youtube.com/watch?v=tUFzOLDuvaE

def approxSqrt(num):
	guess = num					# First guess is just num itself
	diff = 999999999			# diff is used to check terminating condition
	while diff > 0.0001:        # Loop until difference is too small
		# Apply Newton's Method
		newGuess = guess - ((guess**2 - num) / (2*guess))
		
		# Calculate the absolute difference between the two guesses
		diff = newGuess - guess
		if diff < 0:
			diff *= -1
			
		# Update existing guess
		guess = newGuess
		
	return guess
	
num = float(input("Please enter a positive number:"))
sqrt = approxSqrt(num)
print("The square root of {} is approx. {:.1f}".format(num, sqrt))