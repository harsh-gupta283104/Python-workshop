start=int(input("Enter the first number:- "))
end=int(input("Enter the last number:- "))
print(f"Even number detween {start} and {end}: ")
for num in range(start,end+1):
    if num%2==0:
        print(num, end=" ")

print(f"/n0dd number between{start} and {end}:")
for num in range(start,end+1):
    if num%2!=0:
        print(num,end=" ")