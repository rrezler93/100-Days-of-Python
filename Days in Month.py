# Define a function to check if a year is a leap year
def is_leap(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If it is divisible by 100, also check if it's divisible by 400
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                return False
        else:
            return True
    else:
        return False

# Define a function to calculate the number of days in a given month of a year
def days_in_month(year, month):
    # Define a list of the number of days in each month (non-leap year)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check if the month is February (month == 2)
    if month == 2:
        # If it's February, check if the year is a leap year using the is_leap function
        if is_leap(year):
            answer = 29  # Leap year has 29 days in February
        else:
            answer = 28  # Non-leap year has 28 days in February
    else:
        # For other months, get the number of days from the month_days list
        answer = month_days[month - 1]

    return answer

# Get user input for the year and month
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

# Calculate the number of days in the given month and year
days = days_in_month(year, month)

# Print the result
print(days)
