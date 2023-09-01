from turtle import *
from random import *
from colorgram import *

turtle = Turtle()
colormode(255)
turtle.speed(10)
screen = Screen()
screen.bgcolor(229, 228, 226)
turtle.color(0, 0, 0)


# # Extracting colours from Hirst art:
#
# rgb_colours = []
# colours_extracted = extract("image.jpg", 26)
# for i in colours_extracted:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append((new_colour))

# Extracted colours:
final_colours = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53),
                 (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36),
                 (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151),
                 (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120)]


# Draw one dot:
def draw_dot(dots):
    for i in range(dots):
        turtle.pendown()
        turtle.dot(20, choice(final_colours))
        turtle.penup()
        turtle.forward(50)

# All dots combined:
def draw_square_art(dots_per_row):
    dots = 1
    for i in range((dots_per_row * 2) - 1):
        draw_dot(dots)
        turtle.left(90)

        if i % 2 == 1:
            dots += 1

# Draw whole art:
draw_square_art(11)

screen.exitonclick()
