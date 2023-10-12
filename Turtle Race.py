# Imports
from turtle import Turtle, Screen
import random

# Basic settings
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

# Create an empty list to store all the turtle objects that will participate in the race
all_turtles = []

# Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# If the user has placed a bet, set the race status to 'True' to start the race
if user_bet:
    is_race_on = True

# This loop continues as long as the race is still ongoing, based on the value of 'is_race_on.'
while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.clear()
                turtle.goto(x=-230, y=0)
                turtle.write(f"You've won! The {winning_color} turtle is the winner!", font=("Arial", 12, "normal"))
            else:
                screen.clear()
                turtle.goto(x=-230, y=0)
                turtle.write(f"You've lost! The {winning_color} turtle is the winner!", font=("Arial", 12, "normal"))

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Start
screen.exitonclick()
