import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    for _ in range(N_NUMBERS):  # Loop 10 times
        print(random.randint(MIN_VALUE, MAX_VALUE))  # Generate and print a random number

if __name__ == '__main__':
    main()
