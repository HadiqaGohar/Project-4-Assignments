def print_multiple(message: str, repeats: int):
    """
    Prints the message a given number of times.
    """
    for _ in range(repeats):  # Using `_` instead of `i` since it's unused
        print(message)

def main():
    message = input("Please type a message: ")
    
    while True:
        try:
            repeats = int(input("Enter a number of times to repeat your message: "))
            if repeats < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print_multiple(message, repeats)

if __name__ == '__main__':
    main()
