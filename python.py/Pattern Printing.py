# num=int(input("Enter the limit of hte pattern:-  "))
# for i in range(1,num+1):
#     print(i*"*")

# string=input("Enter a letter:- ")
# if (string==string[::-1]):
#     print("The string is a plindrome")
# else:
#     print("The string is not palindrome")

# list=[]

# number=int(input("Enter the number of the list:- "))

# for enteries in range(number):
#     element=int(input("Enter the element:- "))
#     list.append(element)
# print(list)
# for i in list:
#     if i%2==0:

user_input=input("Enter numbers separated by spaces:- ")
number=list(map(int, user_input.split()))
even_odd_checker=list(map(lambda x: "Even" if x%2==0 else "Odd",number))
print("Result:",even_odd_checker)
