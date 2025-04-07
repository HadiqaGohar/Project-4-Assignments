# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
    
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid  # Target found
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1  # Target not found

# # Example usage
# arr = [1, 3, 5, 7, 9, 11, 13, 15]
# target = 7
# result = binary_search(arr, target)

# if result != -1:
#     print(f"Element {target} found at index {result}")
# else:
#     print(f"Element {target} not found")



def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found

# Prompt user for input
target = int(input("Please enter a number to search for: "))

# Generate a list of numbers based on the range from 1 to the target number
arr = list(range(1, target + 1))

result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
    print(f"Binary representation of {target}: {bin(target)[2:]}")
    print(f"Binary representation of index {result}: {bin(result)[2:]}")
else:
    print(f"Element {target} not found.")
