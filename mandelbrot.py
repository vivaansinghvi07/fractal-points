import math
import random

# mandelbrot set maker 

# gets depth
depth = int(input("Depth: "))

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
    e = (random.random() - 0.5) * 6
    f = (random.random() - 0.5) * 6
    # prints point if test passed
    try:
        if test(e, f):
            print(f"({e}, {f})")
    except OverflowError:
        continue