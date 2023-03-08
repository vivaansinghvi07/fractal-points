# Factorial Generator
A python project I made a while ago that computes points on various kinds of fractals / cool shapes!

## Setup:
- Open a virtual python environment on your VS Code terminal (if using VS)
- Open a new python terminal
- If not already, install matplotlib and pandas
    - This can be done with `$ pip install matplotlib` and `$pip install pandas`
- You should be good to go! Read the instructions for each function if you use it!

## shapes.py
This function takes in a constant complex number, inputted with the prompt `a + bi`, where `a` is represented by `c` and `b` is represented by `d` within the code. Then, points are randomly generated, upon which the constant number is added, then the result is entered into the function again. Whichever points do not diverge to infinity are kept within the shape.

### Inputs
- `a` and `b`: The user can enter the complex number here
- `Depth`: This is the amount of times the function is executed. Generally, greater depths tend to allow less points to pass the test
- `Bounds (x1 x2 y1 y2)`: This is simply the boundaries in which points are generated
- `Point Count`: This is how many points are generated. The time can vary since shapes will have different sizes and 'tolerance'

### Output 
While calculating your points, the program will display messages telling you how many have been created. When it's done, a graph should automatically open on your computer, showing your completed shape. The graph can be manipulated using matplotlib's tools.


Suppose you have the following graph, generated with:<br>
 `a: -0.2`<br>
 `b: 0.627`<br>
 `Depth: 200`<br>
 `Bounds: 0.1 0.7 -0.4 0.1`<br>
 `Point Count: 20000000`<br>

![Fractal Graph](imgs/shapesOG.png)

You can zoom into the area selected here:

![Fractal Zoom Selected](imgs/shapesSELECTED.png)

Then, your graph will look like this:

![Fractal Zoomed](imgs/shapesZOOMED.png)

Note: Since there were 20 million points generated, the graph will look solid. However, upon zooming further, you would be able to see the dots.