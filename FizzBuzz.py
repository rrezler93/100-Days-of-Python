# Iterate through numbers from 1 to 100 (inclusive)
for i in range(1, 101):
    # Check if the number is divisible by 3
    if i % 3 == 0:
        # Check if the number is also divisible by 5
        if i % 5 == 0:
            print("FizzBuzz")  # Divisible by both 3 and 5
        else:
            print("Fizz")  # Divisible by 3 but not 5
    # Check if the number is divisible by 5 (and not by 3, as we've already checked that)
    elif i % 5 == 0:
        print("Buzz")  # Divisible by 5 but not 3
    else:
        print(i)  # Not divisible by 3 or 5
