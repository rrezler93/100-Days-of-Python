# Simple program that calculates cans of paints needed for the job

# Import the math module to use the ceiling function for rounding up
import math  
def paint_calc(height, width, cover):
    # Calculate the number of cans needed using the formula: area / coverage
    cans = math.ceil(height * width / cover)

    # Print the result
    print(f"You'll need {cans} cans of paint.")

# Get user input for the height and width of the wall
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

# Set the coverage per can (5 square meters, as per the code)
coverage = 5

# Call the paint_calc function with user-provided values and the coverage value
paint_calc(height=test_h, width=test_w, cover=coverage)

