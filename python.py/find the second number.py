num_1=input("Enter the starting range:- ")
num_2=input("Enter the end range:- ")

for i in range(num_1,num_2):
    if i%5==0:
        a=i+2
        print(i, "-",a)

# list = []
# num_item = int(input("Enter the number of items :- "))
# for entries in range(num_item ):
#     number1  = int(input("Enter :- "))
#     list.append(number1)
# print(list)
# for i in list:
#     a=i+i
# print(a)