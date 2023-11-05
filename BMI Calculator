# Simple BMI (Body Mass Index) Calculator

# Function to calculate BMI
def calculate_bmi(weight, height):
    # Calculate BMI using the formula BMI = weight (kg) / (height (m) ^ 2)
    bmi = weight / (height ** 2)
    return bmi

# Function to interpret the BMI result
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Input data from the user
weight = float(input("Enter your weight (in kilograms): "))
height = float(input("Enter your height (in meters): "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Interpret the result
interpretation = interpret_bmi(bmi)

# Display the result
print(f"Your BMI is: {bmi}")
print(f"BMI interpretation: {interpretation}")
