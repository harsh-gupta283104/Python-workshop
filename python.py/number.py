a=float(input("Enter any fix number "))
b=float(input("Enter any another fix number "))
if a==0 or b==0 or a<1 or b<1:
    print("The number is invalid ")
elif a>b:
    print(f"{a},is greater than ,{b}")
elif a<b:
    print(f"{b},is greater than ,{a}")