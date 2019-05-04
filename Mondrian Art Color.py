# Piotr Smietana
# CS1210
# Homework 12
# Draw random "art" in a Mondrian style

import turtle
import random

# Height and width of the turtle window
WIDTH = 1024
HEIGHT = 768

# Draw a rectange with the lower Right corner at (x, y)
def drawSquare(x, y, w, h, color,width, tur):
    tur.up()
    tur.goto(x,y)
    tur.setheading(90)
    tur.down()
    tur.width(int(width))
    tur.begin_fill()
    tur.fillcolor(color)
    for I in range(2):
        tur.forward(h)
        tur.right(90)
        tur.forward(w)
        tur.right(90)
    tur.end_fill()
    tur.up()

# Select a color randomly
def randomColor(y):
    # Define color lists
    redsList = ["red","#FF6A6A","#CD2626"]
    greensList = ["green","#00C957","#7FFF00"]
    bluesList = ["blue","skyblue","#00CED1"]
    brownsList = ["#9C661F","#D2691E","#D2B48C","#CDC8B1","#F8F8F8"]
    yellowsList = ["yellow","#FFD700","#FFB90F"]
    # Colors based on height of square
    if y < 120:
        return random.choice(yellowsList)
    elif y < 300:
        return random.choice(brownsList)
    elif y < 450:
        return random.choice(bluesList)
    elif y < 640:
        return random.choice(greensList)
    else:
        return random.choice(redsList)
    
# Select pen size randomly
def randomPenSize():
    penSize = random.randint(1,3)
    return penSize
    
# Split horizontally
def splitHoriz(x, y, w, h, tur):
    splitPoint = random.randint(33, 67) / 100
    leftWidth = splitPoint * w
    rightWidth = w - leftWidth
    art(x, y, leftWidth, h, tur)
    art(x + leftWidth, y, rightWidth, h, tur)

# Split vertically
def splitVert(x, y, w, h, tur):
    splitPoint = random.randint(33, 67) / 100
    topHeight = splitPoint * h
    bottomHeight = h - topHeight
    art(x, y, w, topHeight, tur)
    art(x, y + topHeight, w, bottomHeight, tur)
    
# Split both vertically and horizontally
def splitBoth(x, y, w, h, tur):
    splitPointH = random.randint(33, 67) / 100
    splitPointV = random.randint(33, 67) / 100
    leftWidth = splitPointH * w
    rightWidth = w - leftWidth
    topHeight = splitPointV * h
    bottomHeight = h - topHeight
    art(x, y, leftWidth, topHeight, tur)
    art(x + leftWidth, y, rightWidth, topHeight, tur)
    art(x, y + topHeight, leftWidth, bottomHeight, tur)
    art(x + leftWidth, y + topHeight, rightWidth, bottomHeight, tur)

# Decide at random whether or not to split
def doSplit(dim): 
    r = random.randint(120, max(round(1.5 * dim), 120))
    if r < dim:
        return True
    else:
        return False
    
# Use recursion to draw "art" in a Mondrian style
def art(x, y, w, h, tur):
    # Conditions to split
    if w > WIDTH / 32 and h > HEIGHT / 32:
        splitBoth(x, y, w, h, tur)
    elif w > WIDTH / 32:
        splitHoriz(x, y, w, h, tur)
    elif h > HEIGHT / 32:
        splitVert(x, y, w, h, tur)
    else:
        # Random split
        if doSplit(w) and doSplit(h):
            splitBoth(x, y, w, h, tur)
        elif doSplit(w):
            splitHoriz(x, y, w, h, tur)
        elif doSplit(h):
            splitVert(x, y, w, h, tur)
        # No split
        else:
            drawSquare(x, y, w, h, randomColor(y),randomPenSize(), tur)
        
# Set up turtle
def makeTurtle():
    # Set up the turtle
    turtle.setworldcoordinates(-10, -15, WIDTH+15, HEIGHT+10)
    turtle.setup()
    ourWindow = turtle.Screen()
    ourWindow.title('Recursive Art')
    tur = turtle.Turtle()
    tur.hideturtle()
    ourWindow.tracer(0)
    tur.pencolor("black")
    return tur
        
def main():
    # Create the turtle
    tur = makeTurtle()
    # Draw the art
    art(0, 0, WIDTH, HEIGHT, tur)
    # Done
    turtle.done()

main()