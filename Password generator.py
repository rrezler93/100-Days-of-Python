# Imports 
import random
import string

# Generate password with desired characters 
def generate_password():
    length = int(input("Enter the length of the password: "))
    num_letters = int(input("Enter the number of letters in the password: "))
    num_digits = int(input("Enter the number of digits in the password: "))
    num_special_chars = int(input("Enter the number of special characters in the password: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'

    if num_letters + num_digits + num_special_chars > length:
        print("The sum of letters, digits, and special characters exceeds the total length.")
        return

    if include_uppercase and num_letters > length:
        print("The number of letters exceeds the total length.")
        return

    chars = ""
    if num_letters > 0:
        chars += string.ascii_lowercase
        if include_uppercase:
            chars += string.ascii_uppercase
    if num_digits > 0:
        chars += string.digits
    if num_special_chars > 0:
        chars += string.punctuation

    if len(chars) == 0:
        print("Please select at least one type of character (letters, digits, or special characters).")
        return

    password = ''.join(random.choices(chars, k=length))
    print("Generated password:", password)

if __name__ == "__main__":
    generate_password()
