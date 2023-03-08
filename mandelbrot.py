import math
import random
import pandas as pd

# mandelbrot set maker 

# gets depth
depth = int(input("Depth: "))

# gets bounds
x1, x2, y1, y2 = list(map(float, input("Enter bounds here in the following format; x1 x2 y1 y2: ").split(" ")))

# gets a random number within the bounds
def randomInBounds(min, max):
    return (random.random()) * (max - min) + min

# runs mandelbrot set algorithm
def test(a, b):
    
    xvalue = 0
    yvalue = 0

    for _ in range(depth):
        xtemp = xvalue
        xvalue = (xvalue)**2-(yvalue)**2
        yvalue = 2*(xtemp)*(yvalue)
        
        xvalue = xvalue + a
        yvalue = yvalue + b
    
    # can set bounds for border
    if math.sqrt(xvalue**2 + yvalue**2) < 2:
        return True

while True:
    # sets bounds for points
    e, f = randomInBounds(x1, x2), randomInBounds(y1, y2)

    # prints point if test passed
    try:
        if test(e, f):
            print(f"({e}, {f})")
    except OverflowError:
        continue