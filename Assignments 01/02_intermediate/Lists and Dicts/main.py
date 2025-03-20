def access_element(lst, index):
    """Returns the element at a given index, handling out-of-range cases."""
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    """Modifies an element at a given index with a new value."""
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    """Returns a sliced portion of the list with improved index validation."""
    if 0 <= start < len(lst) and 0 <= end <= len(lst):
        return lst[start:end]
    else:
        return "Invalid indices."

def index_game():
    """Interactive index-based game for lists."""
    lst = [1, 2, 3, 4, 5]  # Example list

    while True:
        print("\nCurrent list:", lst)
        print("Choose an operation: access, modify, slice, exit")
        operation = input("Enter operation: ").lower()

        if operation == "access":
            try:
                index = int(input("Enter index to access: "))
                print("Result:", access_element(lst, index))
            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif operation == "modify":
            try:
                index = int(input("Enter index to modify: "))
                new_value = input("Enter new value: ")
                print("Updated List:", modify_element(lst, index, new_value))
            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif operation == "slice":
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                print("Sliced List:", slice_list(lst, start, end))
            except ValueError:
                print("Invalid input. Please enter integers.")

        elif operation == "exit":
            print("Exiting the game. Goodbye!")
            break

        else:
            print("Invalid operation. Please try again.")

if __name__ == '__main__':
    index_game()
