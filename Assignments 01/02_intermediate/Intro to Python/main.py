"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.
"""

# Dictionary storing gravity multipliers for each planet
GRAVITY_FACTORS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def mars_weight():
    """Prompts user for Earth weight and calculates weight on Mars."""
    earth_weight = float(input("Enter a weight on Earth: "))
    mars_weight = round(earth_weight * GRAVITY_FACTORS["Mars"], 2)
    print(f"The equivalent weight on Mars: {mars_weight}")

def planetary_weight():
    """Prompts user for Earth weight and calculates weight on any planet."""
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")

    if planet in GRAVITY_FACTORS:
        weight_on_planet = round(earth_weight * GRAVITY_FACTORS[planet], 2)
        print(f"The equivalent weight on {planet}: {weight_on_planet}")
    else:
        print("Invalid planet name. Please enter a valid planet.")

def main():
    """Main function to allow user to choose between Mars or any planet."""
    print("Choose an option:")
    print("1. Calculate weight on Mars")
    print("2. Calculate weight on any planet")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        mars_weight()
    elif choice == "2":
        planetary_weight()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
