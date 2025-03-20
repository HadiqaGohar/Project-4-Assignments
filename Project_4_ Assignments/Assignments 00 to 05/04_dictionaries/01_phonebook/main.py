def read_phone_numbers():
    """
    Collects user input to store names and phone numbers in a dictionary.
    Stops when the user enters a blank name.
    Returns the phonebook dictionary.
    """
    phonebook = {}  # Initialize an empty phonebook

    while True:
        name = input("Name: ").strip()
        if name == "":
            break
        number = input("Number: ").strip()
        phonebook[name] = number  # Store name-number pair

    return phonebook

def print_phonebook(phonebook):
    """
    Prints all entries in the phonebook.
    """
    if not phonebook:
        print("Phonebook is empty.")
        return

    print("\nPhonebook Entries:")
    for name, number in phonebook.items():
        print(f"{name} -> {number}")

def lookup_numbers(phonebook):
    """
    Allows the user to search for phone numbers by entering a name.
    Stops when a blank input is given.
    """
    while True:
        name = input("Enter name to lookup: ").strip()
        if name == "":
            break
        print(phonebook.get(name, f"{name} is not in the phonebook"))

def main():
    """
    Runs the phonebook program: collects contacts, prints them, and allows lookups.
    """
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

# Run the program
if __name__ == '__main__':
    main()
