# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Function to determine BMI category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Input weight and height
print("Welcome to the BMI Calculator!")
weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Display the result
print(f"Your BMI is: {bmi:.2f}")
print(f"Based on your BMI, you are considered: {bmi_category(bmi)}")
