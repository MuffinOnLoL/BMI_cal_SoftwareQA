# src/bmi_calculator.py

def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be greater than 0.")
    return (weight * 703) / (height ** 2)

def main():
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    
    try:
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    if bmi < 18.5:
        print("You are underweight.")
    elif bmi > 18.5 and bmi <= 24.9:
        print("You are normal weight.")
    elif bmi > 24.9 and bmi <= 29.9:
        print("You are overweight.")
    elif bmi >= 30:
        print("You are obese.")

if __name__ == "__main__":
    main()