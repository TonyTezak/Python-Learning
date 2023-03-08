htInch = input("enter your height in inches \n")
wtLbs = input("enter your weight in pounds \n")

htMeter = float(htInch) / 39.37007874
# print(htMeter)
wtKg = float(wtLbs) * 0.45359237
# print(wtKg)

# 🚨 Don't change the code below 👇
#height = input("enter your height in m: ")
#weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = int(wtKg) / float(htMeter) ** 2
BMI_as_Int = int(BMI)
print(BMI_as_Int)

if BMI < 18:
    print(f"Your BMI is {BMI_as_Int}, you are underweight.")
elif BMI <= 25:
    print(f"Your BMI is {BMI_as_Int}, you have a normal weight.")
elif BMI <= 30:
    print(f"Your BMI is {BMI_as_Int}, you are slightly overweight.")
elif BMI <= 35:
    print(f"Your BMI is {BMI_as_Int}, you are obese.")
else:
    print(f"Your BMI is {BMI_as_Int}, you are clinically obese.")