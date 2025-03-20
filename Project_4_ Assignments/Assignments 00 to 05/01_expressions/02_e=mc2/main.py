C = 299792458  # Speed of light in meters per second (m/s)

def main():
    
    mass_in_kg = float(input("Enter kilos of mass: "))

    # Calculate energy using Einstein's equation
    energy_in_joules = mass_in_kg * (C ** 2)

    # Result
    print("\ne = m * C^2...")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")
    print(f"{energy_in_joules:.6e} joules of energy!")  

if __name__ == '__main__':
    main()
