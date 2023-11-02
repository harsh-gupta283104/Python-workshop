#This is a programme to find the bmi
a=int(input("Enter your weight: "))
b=int(input("Enter your height (in M):  "))

bmi=a/(b**2)

if bmi< 18.5:
    print("The Bmi is uder wieght: ",bmi)
elif bmi< 25:
    print("The Bmi is normal: ",bmi)

elif bmi> 30:
    print("The Bmi is overweight: ",bmi)
else:
    print("You have enter something wrong.")
