# OLD CODE

# def main():
#     print("This program adds two numbers.")
    
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))

#     total = num1 + num2

#     print(f"The total is {total}.")

# if __name__ == '__main__':
#     main()

# ---------------------TRY NEW CODE------------------------

from termcolor import colored


def sum():
    print(colored("\n\t\t\t +-+-+ Sum of two numbers +-+-+ \n", "light_magenta"))

    while True:
        try:
            value1 = int(input(colored("Enter the first number: ", "light_cyan")))
            break
        except ValueError:
            print(colored("❌ Invalid input! Please enter a valid number.", "red"))

    while True:
        try:
            value2 = int(input(colored("Enter the second number: ", "light_cyan")))
            break
        except ValueError:
            print(colored("❌ Invalid input! Please enter a valid number.", "red"))

    total_value = value1 + value2
    print(colored(f"The total value is {total_value}.", "yellow"))
    print(colored("\n\t\t\t +-+-+ End of the program +-+-+ \n", "light_magenta"))

if __name__ == '__main__':
  sum()

   #  Why didn’t I use (if __name__ == '__sum__':) here ? 🤔  
   #  I avoided using __sum__ because it is not a built-in variable in Python. Instead, Python uses __name__ == '__main__' to determine whether a script is being run directly or imported as a module.

   #  What is the use of __name__ == '__main__' in Python? 🤔
   #  The __name__ == '__main__' is used to execute some code only if the file was run directly, and not imported. This is useful when you want to run some code only if the file was run directly, and not imported.
