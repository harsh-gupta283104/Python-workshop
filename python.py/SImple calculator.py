
list=[]
while True:
    print("="*5,"Enhanced Simple Calculator","="*5)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication" )
    print("5. Display all the operations")
    print("6. Quit")
    operati_on=input("Enter your choice:- ")
    if (operati_on == "1"):
        print("hello")
        num_1=int(input("Enter first number:- "))
        num_2=int(input("Enter second number:- "))
        add=num_1+num_2
        list.append(add)
    elif operati_on=='2':
        num_1=int(input("Enter first number:- "))
        num_2=int(input("Enter second number:- "))
        sub=num_1-num_2
        list.append(sub)
    elif operati_on=='3':
        num_1=int(input("Enter first number:- "))
        num_2=int(input("Enter second number:- "))
        div=num_1/num_2
        list.append(div)
    elif operati_on=='4':
        num_1=int(input("Enter first number:- "))
        num_2=int(input("Enter second number:- "))
        mult=num_1*num_2
        list.append(mult)
    elif operati_on=='5':
        print(list)
    elif operati_on==6:
        break