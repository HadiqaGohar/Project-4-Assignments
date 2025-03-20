def main():
    curr_value = int(input("Enter a number: "))  # Get user input and convert to integer

    while curr_value < 100:  # Loop until the value reaches or exceeds 100
        curr_value *= 2  # Double the current value
        print(curr_value)  # Print the updated value

if __name__ == '__main__':
    main()
