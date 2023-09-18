# Checks if the number is prime, and print the results 
def prime_checker(number):
    no_rest = 0
    for i in range(1, number + 1):
        if number % i == 0:
            no_rest += 1
    if no_rest == 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Ask for a number
n = int(input("Check this number: "))
#Print the results 
prime_checker(number=n)
