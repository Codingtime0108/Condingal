height= float(input("Enter your height:"))
weight= float(input("Enter your weight:"))

bmi= weight/(height/100)**2

if bmi<=18.5:
    print("You are underweight!")
elif bmi<=24.9:
    print("You are healthy")
elif bmi<=29.9:
    print("You are over weight!")
elif bmi<=34.9:
    print("You are severly overweight!")
elif bmi<=39.9:
    print("You are obese!!!")
else:
    print("You are severly obese!!!!")