print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? £"))
people = int(input("How many people to split the bill? "))
tip = int(input("How much tip would you like to give? ")) / 100

person = (bill / people) * (1 + tip)

print("It is £{:0.2f} per person.".format(person))
