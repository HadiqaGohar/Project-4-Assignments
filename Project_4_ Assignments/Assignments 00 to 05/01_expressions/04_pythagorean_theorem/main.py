import math  

def main():
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse using Pythagorean theorem
    bc = math.sqrt(ab**2 + ac**2)

    print(f"The length of BC (the hypotenuse) is: {bc:.2f}")

if __name__ == '__main__':
    main()
