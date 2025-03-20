def main():
    lst = []  # Initialize an empty list to store user inputs

    val = input("Enter a value: ")  # Get the first input from the user
    while val:  # Continue looping until the user presses Enter without typing anything
        lst.append(val)  # Add the input value to the list
        val = input("Enter a value: ")  # Ask for the next input

    print("Here's the list:", lst)  

if __name__ == '__main__':
    main()
