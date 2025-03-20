def main():
    # Prompt user for temperature in Fahrenheit
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert to Celsius
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    # Display the result
    print(f"Temperature: {degrees_fahrenheit:.1f}F = {degrees_celsius:.6f}C")

# Call Function
if __name__ == '__main__':
    main()
