import math
import random

# cool stuff:  
# -.502 .8632 - makes a fun ball shape thing

# gets constant
print("a + bi")

c = float(input("a: "))
d = float(input("b: "))
depth = int(input("Depth: "))
x1, x2, y1, y2 = list(map(float, input("Enter bounds here in the format \"x1 x2 y1 y2\":").split(" ")))

# function that computes the squaring and addition of two imaginary points a + bi and c + di
xFunc = lambda a, b: (a+c)**2-(b+d)**2
yFunc = lambda a, b: 2*(a+c)*(b+d)

# gets a random number within the bounds
def randomInBounds(min, max):
    return (random.random()) * (max - min) + min

# calculates distance from center of the point
def test(a, b):
    for _ in range(depth):
        temp = a
        a = xFunc(a, b)
        b = yFunc(temp, b)
    return math.sqrt(a**2 + b**2)

while True:
    # sets bounds for the point generation - usually +-2
    e, f = randomInBounds(x1, x2), randomInBounds(y1, y2)

    try:
        # gets value to be analyzed
        val = test(e, f)
        if val <= 1:
            print(f"({e}, {f})")
    except OverflowError:
        continue