list=[]
a=0
b=0
no_of_elements=int(input("Enter the no. of the element in list that you want:-  "))
for entries in range(no_of_elements):
    element=input("Enter the element of the list:- ")
    number=list.append(element)
print(list)

even_numbers=[a+=a if x%2==0 else b+=b for x in list]
print(even_numbers)

