import numpy as np
import matplotlib.pyplot as plt

# Define the x ranges for each interval
x1 = np.linspace(-2, 7, 10)  # for x < 1
# x2 = np.linspace(1, 3, 100)   # for 1 < x < 3
# x3 = np.linspace(3, 4, 100)   # for 3 < x < 4
# x4 = np.linspace(4, 7, 100)   # for x > 4

# # Define the functions for each interval
f1 = [4,3,2,0,5,6,5,5,8,11]
# f2 = x2 -1
# f3 = -x3 + 5
# f4 = x4 - 3

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each function on its interval
ax.plot(x1, f1, label='f(x) = -x + 2 for x < 1',color='black')
# ax.plot(x2, f2, label='f(x) = x for 1 < x < 3',color='black')
# ax.plot(x3, f3, label='f(x) = -x + 5 for 3 < x < 4',color='black')
# ax.plot(x4, f4, label='f(x) = x + 5 for x > 4',color='black')

# Set the limits of the plot
ax.set_xlim([-2, 7])
ax.set_ylim([0, 10])

# Adding labels and title
ax.set_xlabel('x')
ax.set_ylabel('Objective Function Value')
#ax.set_title('Piecewise function plot')

# Add a legend
#ax.legend()
plt.grid()
# Show the plot
plt.show()

def example(x):
    if(x<1):
        print('.')
        if(x==1):
            print('.')
    elif(x>4):
        print('.')
    print('.')
