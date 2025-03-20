import random

NUM_ROUNDS = 5  # Number of rounds in the game

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0  # Track user score

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")

        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is {user_number}")

        # Get user input and validate it
        while True:
            guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
            if guess in ["higher", "lower"]:
                break
            print("Please enter either 'higher' or 'lower'.")

        # Check if the user was correct
        if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1  # Increase score if correct
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {score}\n")  # Print updated score

    # Display final message based on performance
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == '__main__':
    main()
