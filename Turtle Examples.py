from turtle import *
from random import *

turtle = Turtle()
turtle.shape("classic")
turtle.color("grey")
turtle.width(15)
turtle.speed(500)

screen = Screen()
screen.bgcolor("black")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
colour = 0

# Different shapes:
#
# def shape(walls):
#     for i in range(walls):
#         turtle.forward(40)
#         turtle.right(360/walls)
#
# for i in range(3, 11):
#     turtle.color(colours[colour])
#     shape(i)
#     colour += 1


# Random direction:
#
# def random_walk(counter):
#     direction = [0, 90, 180, 270]
#     for i in range(counter):
#         turtle.setheading(choice(direction))
#         turtle.color(choice(colours))
#         turtle.forward(30)
#
# random_walk(1000)


# # Random colour:
#
# colormode(255)
#
# def random_colour():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     random_colour = (r, g, b)
#     return random_colour
#
# for i in range(100):
#     turtle.width(3)
#     turtle.color(random_colour())
#     turtle.forward(i * 5)
#     turtle.right(90)


# # Spirograph:
#
# def draw_spirograph(gap):
#     for i in range(360 // gap):
#         turtle.width(1)
#         turtle.color(choice(colours))
#         turtle.circle(100)
#         turtle.setheading(turtle.heading() + gap)
#
# draw_spirograph(3)

screen.exitonclick()
