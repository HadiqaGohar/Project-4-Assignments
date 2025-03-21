
import streamlit as st

# Set page title
st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="wide")

# Sidebar for the image
st.sidebar.markdown('<h1 class="title">BMI Calculator</h1>', unsafe_allow_html=True)
st.sidebar.image("dumbbell.png", use_container_width=True)

# Main content area (Centering the process)
st.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    .description {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<h1 class="title">BMI Calculator</h1>', unsafe_allow_html=True)
st.markdown('<p class="description">Enter your weight (in kg) and height (in feet) to calculate your BMI.</p>', unsafe_allow_html=True)

# Layout to center input fields and buttons
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    # Input fields in the center of the page
    weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1)
    height_feet = st.number_input("Enter your height (feet)", min_value=0.0, step=0.1)

    # Function to calculate BMI
    def calculate_bmi(weight, height_feet):
        # Convert height to meters
        height_in_meters = height_feet * 0.3048
        bmi = weight / (height_in_meters ** 2)
        return bmi

    # Calculate button
    if st.button("Calculate BMI"):
        if weight > 0 and height_feet >= 0:
            bmi = calculate_bmi(weight, height_feet)
            st.write(f"Your BMI is: {bmi:.2f}")
            
            # Category based on BMI
            if bmi < 18.5:
                st.write("Category: Underweight")
            elif 18.5 <= bmi < 24.9:
                st.write("Category: Normal weight")
            elif 25 <= bmi < 29.9:
                st.write("Category: Overweight")
            else:
                st.write("Category: Obese")
        else:
            st.error("Please enter valid inputs.")
