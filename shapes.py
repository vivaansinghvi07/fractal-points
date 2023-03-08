import math
import random

# cool stuff:  
# -.502 .8632 - makes a fun ball shape thing

# gets constant
print("a + bi")

c = float(input("a: "))
d = float(input("b: "))
depth = int(input("Depth: "))

# function that computes the squaring and addition of two imaginary points a + bi and c + di
xFunc = lambda a, b: (a+c)**2-(b+d)**2
yFunc = lambda a, b: 2*(a+c)*(b+d)

# calculates distance from center of the point
def test(a, b):
    for _ in range(depth):
        temp = a
        a = xFunc(a, b)
        b = yFunc(temp, b)
    return math.sqrt(a**2 + b**2)

while True:
    # sets bounds for the point generation
    e = (random.random() - 0.5) * 4
    f = (random.random() - 0.5) * 4
    try:
        # gets value to be analyzed
        val = test(e, f)
        if val <= 1:
            print(f"({e}, {f})")
    except OverflowError:
        continue