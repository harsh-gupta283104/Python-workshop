"""# Limit=int(input("Enter the Last Number:-  "))
# a, b, c=0,1,0
# print(a,end=",")
# for i in range(1,Limit+1):
#     a, b=b,c 
#     c=a+b
#     print(c, end=",")

# limit=1000
# fibonacci_sequence=[0,1]

# while True:
#     next_number=fibonacci_sequence[-1] + fibonacci_sequence[-2]
#     if next_number > limit:
#         break
#     fibonacci_sequence += [next_number] #combine lists using'+='

# print("Fibonacci sequence: ")
# print(fibonacci_sequence)

# start=10
# end=50
# prime_nuber=[]

# for num in range(start, end+1):
#     if num>1:
#         for i in range(2,int(num**0.5) +5):
#             if (num % i):
#                 break
#             else:
#                 prime_nuber.append(num)
# print(f"Prime numbers between {start} and {end}:")
# print(prime_nuber)"""

num_1= int(input("Enter the first limit:- "))
num_2= int(input("Enter the last limit:- "))

flag=0
for i in range(num_1,num_2):
    for j in range(2,i//2):
        if i/j==0:
            flag=flag+1
            if (flag==0):
                print(i,end=" ")
            else:
                flag=0