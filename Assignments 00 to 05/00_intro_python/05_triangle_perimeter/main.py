def main():
    # Get the lengths of the three sides
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Calculate the perimeter
    perimeter = side1 + side2 + side3

    # Print the result using f-string for better readability
    print(f"The perimeter of the triangle is {perimeter}")


# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
