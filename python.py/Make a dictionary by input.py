User_dict={}

num_pair=int(input("Enter te number of key-value pairs you want to add:- "))
for x in range(num_pair):
    key=input("Enter the key:- ")
    Value=input("Enter the Vlaue:- ")
    User_dict[key]=Value
print("Result of the dictonary:- ",User_dict)