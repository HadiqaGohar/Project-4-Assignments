def main():
    """
    Asks the user how many of each fruit they want to buy and calculates the total cost.
    """
    # Dictionary containing fruits and their prices
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }
    
    total_cost = 0  # Variable to keep track of total cost

    # Loop through each fruit and prompt the user for quantity
    for fruit_name, price in fruits.items():
        while True:
            try:
                amount_bought = int(input(f"How many ({fruit_name}) do you want to buy?: ").strip())
                if amount_bought < 0:
                    print("Please enter a valid non-negative number.")
                    continue
                total_cost += price * amount_bought
                break  # Exit loop if input is valid
            except ValueError:
                print("Invalid input! Please enter a number.")

    # Display total cost formatted to 2 decimal places
    print(f"Your total is ${total_cost:.2f}")

# Run the program
if __name__ == '__main__':
    main()
