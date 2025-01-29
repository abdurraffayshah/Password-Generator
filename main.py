#Libaries
import sys
from tabulate import tabulate
from pyfiglet import Figlet
import random
import string
import time

def main():
    # Display the title
    title()
    # Display the menu options
    menu()
    tries = 3  # Initialize the number of attempts
    while tries > 0:
        user = input("Input: ").lower()  # Get user input and convert to lowercase
        if user == "g":
            # Prompt for password length
            try:
                length = int(input("What should be the length of the password? "))
                print("Please wait as we generate your password. It can take up to a few seconds")
                for _ in range(6):
                    print(".", end="", flush=True)  # Print dots to indicate processing
                    time.sleep(0.5)
                print()
                # Generate and display the password
                print(f"New Password: {password_generator(user, length)}")
                sys.exit("Thank you for using our service")
            except ValueError:
                # Handle invalid input for password length
                print("Please input a valid number")
                tries -= 1  # Decrement the number of tries

        elif user == "r":
            print("Please wait as we generate your password. It can take up to a few seconds")
            for _ in range(6):
                print(".", end="", flush=True)  # Print dots to indicate processing
                time.sleep(0.5)
            print()
            # Generate and display the password
            print(f"New Password: {password_generator(user)}")
            sys.exit("Thank you for using our service")

        else:
            # Invalid input prompt
            print("Please input a valid prompt.")
            tries -= 1  # Decrement the number of tries
    print("Ran out of tries, Try again later :)")

def title():
    # Create and display the title using Figlet
    figlet = Figlet(font="slant")
    rendered = figlet.renderText("Password Generator")
    print(rendered)

def menu():
    # Create and display the menu using tabulate
    data = {"OPTIONS": ["Generate with Prompt", "Complete random", "Exit"],
            "KEYS": ["G", "R", "E"]}
    print(tabulate(data, headers="keys", tablefmt="double_grid"))

def password_generator(user, length=None):
    # Generate password based on user input
    if user == "g":
        prompt_length = length
        if prompt_length <= 0:
            return "Please Input a valid length"
        else:
            # Generate password with specified length
            return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    elif user == "r":
        # Generate password with random length between 8 and 12
        number = random.randint(8, 12)
        return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(number))

if __name__ == "__main__":
    main()
