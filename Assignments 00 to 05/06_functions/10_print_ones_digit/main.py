def print_ones_digit(num: int):
    """
    Prints the ones digit of the given number.
    """
    print("The ones digit is", abs(num) % 10)  # abs() ensures it works for negative numbers too

def main():
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print_ones_digit(num)

if __name__ == '__main__':
    main()
