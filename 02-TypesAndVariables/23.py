height = float(input("Enter your height in metres: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = round(weight/height**2,2)

print("Your BMI index: ", bmi)

if bmi <= 18.4: 
    print("Underweight")
elif bmi <= 24.9:
    print("Normal")
elif bmi <=39.9:
    print("Overweight")
else:
    print("Obese")