# Prompt the user to input their height in meters
height = float(input("Enter your height in meters: "))

# Prompt the user to input their weight in kilograms
weight = float(input("Enter your weight in kilograms: "))

# Calculate the BMI using the provided formula (weight / height^2)
BMI = round(weight / height ** 2)

# Determine the BMI category and print an appropriate message
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
