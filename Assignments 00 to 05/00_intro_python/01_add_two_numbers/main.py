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
