def count_even(lst):
    """
    Prints the number of even numbers in the list.
    
    >>> count_even([1, 2, 3, 4])
    2
    >>> count_even([1, 3, 5, 7])
    0
    """
    even_count = sum(1 for num in lst if num % 2 == 0)  # Count evens using list comprehension
    print(even_count)

def get_list_of_ints():
    """
    Reads integers from the user until they press enter and returns the list.
    """
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            lst.append(int(user_input))  # Convert input to integer and append
        except ValueError:
            print("Invalid input. Please enter an integer.")  # Handle non-integer inputs

    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)

# Ensure the main function runs when the script is executed
if __name__ == '__main__':
    main()
