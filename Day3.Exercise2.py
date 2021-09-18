height = float(input("enter your height in m: "))

weight = float(input("enter your weight in kg: "))

old_number = weight / height ** 2 

number = (round(old_number))

if number < 18.5:
  print(f"Your BMI is {number}, you are underweight.")
elif number < 25:
    print(f"Your BMI is {number}, you have a normal weight.")
elif number < 30:
    print(f"Your BMI is {number}, you are slightly overweight.")
elif number < 35:
    print(f"Your BMI is {number}, you are obese.")
else:
  print(f"Your BMI is {number}, you are clinically obese.")
