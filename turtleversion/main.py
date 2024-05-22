import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("#e0e0e0")
screen.setup(width=1.0, height=1.0)  # Set screen size to full screen

colors = ['#aec6cf', '#c9c0e2', '#b2d8b2', '#f3a7a7', '#f9d6ac', '#aec8d7', '#a5d9ea', '#c7b3e5', '#f0c5d2', '#fad2e1']

sizes = [1]
turtles = []
rates = [0.1, 0.15, 0.25]

def create_turtle():
    t = turtle.Turtle()
    t.color(random.choice(colors))
    t.penup()
    t.goto(random.randint(-screen.window_width() // 2, screen.window_width() // 2),  # Adjust position to fit full screen
           random.randint(-screen.window_height() // 2, screen.window_height() // 2))
    t.pendown()
    t.speed(10)
    t.hideturtle()
    t.rate = random.choice(rates)
    t.size = 7
    t.count = 0
    turtles.append(t)

def move_turtles():
    startingAngle = 0  # Starting angle
    angleIncrement = 3
    while True:
        time.sleep(0.04)
        turtle.tracer(False)
        random_number = random.randint(1, 100)
        if len(turtles)<10:
            if random_number == 1:
                screen.ontimer(create_turtle, random.randint(200, 800))  # Create new turtle every 1 to 5 seconds
        for t in turtles:
                t.right(angleIncrement)
                for _ in range(4):
                    t.forward(t.size)
                    t.right(startingAngle + 90)
                    t.size += t.rate
                t.count += 1
                if t.count == 250:
                    t.clear()  # Use clear instead of reset for better performance
                    turtles.remove(t)
        turtle.update()

move_turtles()

screen.exitonclick()
