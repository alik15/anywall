import turtle
import random
import time

turtle.speed(0)
screen=turtle.Screen()
turtle.hideturtle()

screen.bgcolor("black")
all_colors=["grey"]

screen.setup(1000, 1000)


def square():
    starting_angle = 0 # starting angle
    size = 7 # starting size
    sizeIncreaseRate = 0.1
    angleIncrement = 3 
    for i in range(5000):
        turtle.tracer(False)
        time.sleep(0.04) 
        turtle.color(random.choice(all_colors))
        turtle.right(angleIncrement) # rotation after every complete square
        # drawing a complete square
        for x in range(4):
            turtle.forward(size) 
            turtle.right(starting_angle + 90) # turns 90 degrees after every line to complete a square
            size+=sizeIncreaseRate # increase in the square size after every square, also adds a little length to each line
        turtle.update()
            
   
square()
