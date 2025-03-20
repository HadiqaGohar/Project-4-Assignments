def add_many_numbers(numbers: list[int]) -> int:
    
    return sum(numbers)  

def main():
    numbers = [1, 2, 3, 4, 5]  
    sum_of_numbers = add_many_numbers(numbers)  # Calculate sum
    print(f"Sum of numbers: {sum_of_numbers}")  # Output sum

if __name__ == '__main__':
    main()
