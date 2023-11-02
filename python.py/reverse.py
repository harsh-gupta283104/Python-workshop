# txt=input("Enter the number:- ")
# reverse= txt[::-1]
# print(reverse)

number=int(input("Enter the number:- "))
reversed_number=0

while number>0:
    
    digit= number%10
    
    #print(digit)
    
    reversed_number=(reversed_number * 10) + digit

    number=number//10

print(f"The reveersed numberis :{reversed_number}")