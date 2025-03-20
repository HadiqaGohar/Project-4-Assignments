def double_numbers(numbers: list[int]) -> list[int]:
 
    return [num * 2 for num in numbers]  # List comprehension for efficiency

def main():
    numbers = [1, 2, 3, 4] 
    doubled_numbers = double_numbers(numbers)  # Get the doubled list
    print(doubled_numbers)  # Result


if __name__ == '__main__':
    main()
