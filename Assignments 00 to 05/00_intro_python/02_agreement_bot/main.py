# def main():
#     favorite_animal = input("What's your favorite animal? ")
#     print(f"My favorite animal is also {favorite_animal}!")


# if __name__ == '__main__':
#     main()

from termcolor import colored

def Favorite_Animal():

    print(colored("\n\t\t\t +-+-+ 🐾 FAVORITE ANIMAL +-+-+ \n", "light_magenta"))

    while True:
        favorite_animal = input(colored("🐾 What's your favorite animal? ", "light_cyan"))
        if favorite_animal.isalpha():  # Check if input contains only letters
            break
        else:
            print(colored("❌ Only letters are allowed! Please enter a valid animal name.", "red"))

    print(colored(f"🎉 Your favorite animal is also {favorite_animal}! 🐾", "yellow"))
    print(colored("\n\t\t\t +-+-+ End of the Program +-+-+ \n", "light_magenta"))

if __name__ == '__main__':
    Favorite_Animal()

