# List=[1,2,52,82,1,5,6,3,1,2,4]
# a=0
# for num in List:
#     for num2 in List:
#         if num == num2:
#             a+=1
#     print(f"The elemetn {num} occurs {a} times in the list.")
#     a=0

# list=[]
# no=int(input("Enter the no. of element that you want:- "))
# for entries in range(no):
#     element=int(input("Enter the element:- "))
#     list.append(element)
#     a=list[-1:-no]
# print(a)

myTuple=("apple", "banana", "cherry", "apple", "guava")
print(myTuple)

myTuple1=("apple", "banana", "cherry", "apple", "guava")
print(myTuple1)
print(len(myTuple1))
print(type(myTuple1))

tuple1=("apple", "banana", "cherry",)
tuple2=(1, 2, 3, 4, 5, 6)
tuple3=(True, False, False)
print(tuple1, tuple2, tuple3)