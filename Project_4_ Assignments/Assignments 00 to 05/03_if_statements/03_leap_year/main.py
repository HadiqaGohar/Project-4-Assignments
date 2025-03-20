# def main():
#     # Get the year to check from the user
#     year = int(input('Please input a year: '))

#     if year % 4 == 0:  # Checking whether the provided year is evenly divisibly by 4
#         if year % 100 == 0:  # Checking whether the provided year is evenly divisibly by 100
#             if year % 400 == 0:  # Checking whether the provided year is evenly divisibly by 400
#                 print("That's a leap year!")
#             else:  # (Not divisible by 400)
#                 print("That's not a leap year.")
#         else:  # (Not divisible by 100)
#             print("That's a leap year!")
#     else:  # (Not divisible by 4)
#         print("That's not a leap year.")


# # There is no need to edit code beyond this point

# if __name__ == '__main__':
#     main()



def main():
    # Get the year to check from the user
    year = int(input("Please input a year: "))

    # Check if the year is a leap year based on the given conditions
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

# Call the main function
if __name__ == '__main__':
    main()
