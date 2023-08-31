# Prompt the user to input a list of student heights separated by spaces
student_heights = input("Input a list of student heights: ").split()

# Convert the input string into a list of integers (assuming all inputs are valid integers)
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Initialize variables to keep track of the total number of heights and the sum of heights
how_many = 0  # To count the number of heights
how_much = 0  # To sum up the heights

# Iterate through the list of student heights to calculate the sum and count
for height in student_heights:
    how_many += 1  # Increment the count
    how_much += height  # Add the height to the sum

# Calculate the average height (rounded to the nearest integer)
average_height = round(how_much / how_many)

# Print the rounded average height
print(average_height)
