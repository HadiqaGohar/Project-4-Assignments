# def main():
#     # Prompt user for a number and convert to float
#     num = float(input("Type a number to see its square: "))

#     print(f"{num} squared is {num ** 2}")

# if __name__ == '__main__':
#     main()

from termcolor import colored

def Square():
    print(colored(" \n\t\t\t 🔢 ******* Welcome to the Square Calculator! ******* \n ", "magenta"))
    while True:
        try:
            num = float(input(colored("🔢 Type a number to see its square: ", "cyan")))
            print(colored(f"✅ {num} squared is {num ** 2}", "green"))
            print(colored(" \n\t\t\t 🔢 ******* Code End! ******* \n ", "magenta"))
            break
        except ValueError:
            print(colored("❌ Please enter a valid number", "red"))

if __name__ == '__main__':
    Square()
