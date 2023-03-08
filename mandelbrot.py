import math
import random
import matplotlib as mpl
import pandas as pd

# mandelbrot set maker 

# gets depth
depth = int(input("Depth: "))

# gets bounds
x1, x2, y1, y2 = list(map(float, input("Enter bounds here in the format \"x1 x2 y1 y2\": ").split(" ")))

# gets count of points
goal = int(input("Point Count: "))

# declares empty arrays that will store the points
xVals, yVals = [], []

# declares starting count
count = 0

# option for only showing the border; if you need a border then perform calculations to limit it
border = input("Only show a border? [y/n]: ") == "y"
lowerBound = (1.8 if depth < 20 else (1.6 if depth < 50 else (1.4 if depth < 100 else (1.2 if depth < 200 else 1)))) if border else 0

# gets a random number within the bounds
def randomInBounds(min, max):
    return (random.random()) * (max - min) + min

# runs mandelbrot set algorithm
def test(a, b, depth, lowerBound):
    
    # initializes starter values
    xValue = 0
    yValue = 0

    for _ in range(depth):

        # computes the square
        xTemp = xValue
        xValue = (xValue)**2-(yValue)**2
        yValue = 2*(xTemp)*(yValue)
        
        # adds the randomly generated constant point
        xValue = xValue + a
        yValue = yValue + b
    
    # can set bounds for border
    value = math.sqrt(xValue**2 + yValue**2)
    if value < 2 and value > lowerBound: # edit this to change the border width manually
        return True

while count < goal:
    # sets bounds for points
    e, f = randomInBounds(x1, x2), randomInBounds(y1, y2)

    # saves point if test passed
    try:
        if test(e, f, depth, lowerBound):
            xVals.append(e)
            yVals.append(f)
            count += 1
            if not count % (goal // 100): # shows progress
                print(str(count) + " points generated...")
    except OverflowError:
        continue

# plots the graph
df = pd.DataFrame({'x': xVals, 'y': yVals})
df.plot.scatter(x = 'x', y = 'y', s = 0.4)
mpl.pyplot.show()