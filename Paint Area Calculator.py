# Simple program that calculates cans of paints needed for the job

import math


def paint_calc(height, width, cover):
    cans = math.ceil(height * width / 5)

    print(f"You'll need {cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
