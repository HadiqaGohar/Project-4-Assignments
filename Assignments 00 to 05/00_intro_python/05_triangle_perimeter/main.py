# def main():
#     # Get the lengths of the three sides
#     side1 = float(input("What is the length of side 1? "))
#     side2 = float(input("What is the length of side 2? "))
#     side3 = float(input("What is the length of side 3? "))

#     # Calculate the perimeter
#     perimeter = side1 + side2 + side3

#     # Print the result using f-string for better readability
#     print(f"The perimeter of the triangle is {perimeter}")


# # This provided line is required at the end of the Python file to call the main() function.
# if __name__ == '__main__':
#     main()

from termcolor import colored

def TrianglePerimeter():
    while True:
       try:
           side1 = float(input("What is the length of side 1? "))
           break
       except ValueError:
           print(colored("Please enter a valid number", "red"))
    while True:
       try:
           side2 = float(input("What is the length of side 2? "))
           break
       except ValueError:
           print(colored("Please enter a valid number", "red"))
    while True:
       try:
           side3 = float(input("What is the length of side 3? "))
           break
       except ValueError:
           print(colored("Please enter a valid number", "red"))
    perimeter = side1 + side2 + side3
    print(colored(f"The perimeter of the triangle is {perimeter}", "magenta"))

if __name__ == '__main__':
    TrianglePerimeter()     
