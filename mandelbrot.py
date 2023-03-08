import math
import random

# mandelbrot set maker 

depth = int(input("Depth: "))

def test(a, b):
    
    xvalue = 0
    yvalue = 0

    for _ in range(depth):
        xtemp = xvalue
        xvalue = (xvalue)**2-(yvalue)**2
        yvalue = 2*(xtemp)*(yvalue)
        
        xvalue = xvalue + a
        yvalue = yvalue + b
    
    if math.sqrt(xvalue**2 + yvalue**2) < 2:
        return True

for i in range(1000000):
    e = (random.random() - 0.5) * 6
    f = (random.random() - 0.5) * 6
    try:
        if test(e, f):
            print(f"({e}, {f})")
    except OverflowError:
        continue