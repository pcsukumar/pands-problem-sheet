#This program displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
#Author : Prasanth Sukumar

import numpy as np
import matplotlib.pyplot as plt

xlist = np.linspace(0,4,100)
ylist = xlist
plt.plot(xlist, ylist, label="f(x)=x")

ylist = xlist**2
plt.plot(xlist, ylist, label="g(x)=X^2")

ylist = xlist**3
plt.plot(xlist, ylist, label="g(x)=X^3")

plt.title('Plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4]')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend() # show a legend on the plot
plt.show()

#Reference
# 1. Adding a legend https://stackoverflow.com/questions/19125722/adding-a-legend-to-pyplot-in-matplotlib-in-the-simplest-manner-possible