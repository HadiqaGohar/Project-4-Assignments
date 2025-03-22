

# def main():
#     # Prompt user for temperature in Fahrenheit
#     degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
#     # Convert to Celsius
#     degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

#     # Display the result
#     print(f"Temperature: {degrees_fahrenheit:.1f}F = {degrees_celsius:.6f}C")

# # Call Function
# if __name__ == '__main__':
#     main()

from termcolor import colored

def temperature_converter():

    print(colored("\n\t\t\t +-+-+ 🔥 Temperature Converter  +-+-+ \n", "light_magenta"))

    while True:
        try:
            # Prompt user for temperature in Fahrenheit with color
            degrees_fahrenheit = float(input(colored("Enter temperature in Fahrenheit: ", "light_cyan")))
            
            # Convert to Celsius
            degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0
            
            # Display the result with color formatting
            print(colored(f"Temperature: {degrees_fahrenheit:.1f}F = {degrees_celsius:.6f}C", "green"))
            print(colored("\n\t\t\t +-+-+ End of the Program +-+-+ \n", "light_magenta"))
            break  # Exit loop after successful conversion
        
        except ValueError:
            print(colored("❌ Invalid input! Please enter a valid number.", "red"))

if __name__ == "__main__":
    temperature_converter()
