# Summary about the program:- You are tasked with creating a Python program that calculates the monthly 
# payment for an education loan based on the principal amount, annual interest 
# rate, and the loan term (in years) provided by the user.

p=float(input("Enter the principle loan amount(in Dollar($)):- "))
r=float(input("Enter the rate of interest(in pecentage):- "))
n=int(input("Enter the Loan term in year:-  "))
r=(r/12)/100
n=(n*12)
m= (p*r*((1+r)**n))/(((1+r)**n)-1)
print(f"This your monthly payment of you loan:- {m}")

