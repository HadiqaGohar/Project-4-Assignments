def get_user_numbers():
    """
    Prompts the user to input numbers and stores them in a list.
    Stops when the user enters a blank line.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        
        # Stop input when a blank line is entered
        if user_input == "":
            break
        
        # Convert input to an integer and add it to the list
        user_numbers.append(int(user_input))
    
    return user_numbers

def count_numbers(num_list):
    """
    Counts the occurrences of each number in the list using a dictionary.
    """
    num_dict = {}
    for num in num_list:
        num_dict[num] = num_dict.get(num, 0) + 1  # Increment count using .get()
    
    return num_dict

def print_counts(num_dict):
    """
    Prints out the frequency of each number in the dictionary.
    """
    for num, count in sorted(num_dict.items()):  # Sorting for a cleaner output
        print(f"{num} appears {count} times.")

def main():
    """
    Main function to get user input, count occurrences, and display results.
    """
    user_numbers = get_user_numbers()
    num_dict = count_numbers(user_numbers)
    print_counts(num_dict)

# Boilerplate code to run the program
if __name__ == '__main__':
    main()
