# Prompt the user to input a list of student scores separated by spaces
student_scores = input("Input a list of student scores: ").split()

# Convert the input string into a list of integers
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Print the list of student scores
print(student_scores)

# Initialize a variable to keep track of the highest score
highest = 0

# Iterate through the list of student scores to find the highest score
for i in student_scores:
    if i > highest:
        highest = i

# Print the highest score found in the class
print(f"The highest score in the class is: {highest}")

