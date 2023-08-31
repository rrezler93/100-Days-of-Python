# This script checks, if the provided year is a leap year or not

year = int(input("Which year do you want to check? "))

by_four = year % 4
by_hundred = year % 100
by_four_hundred = year % 400

if by_four == 0:
    if by_hundred == 0:
        if by_four_hundred == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

#if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#    print("Leap year.")
#else:
#    print("Not leap year.")

