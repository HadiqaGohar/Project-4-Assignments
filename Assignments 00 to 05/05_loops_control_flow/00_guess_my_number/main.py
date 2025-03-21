import random

def main():
    secret_number = random.randint(1, 99)
    guess_count = 0  # Track the number of guesses
    
    print("I am thinking of a number between 1 and 99...")

    while True:
        try:
            guess = int(input("Enter a guess: "))
            guess_count += 1  # Increment guess count

            if guess < secret_number:
                print("Your guess is too low. Try a higher number.")
            elif guess > secret_number:
                print("Your guess is too high. Try a lower number.")
            else:
                print(f"🎉 Congrats! The number was {secret_number}. You guessed it in {guess_count} attempts!")
                break  # Exit loop when guessed correctly
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == '__main__':
    main()
