def main():
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))

    # Perform division and get remainder
    quotient = dividend // divisor  # Integer division
    remainder = dividend % divisor  # Modulus operation3

    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == '__main__':
    main()
