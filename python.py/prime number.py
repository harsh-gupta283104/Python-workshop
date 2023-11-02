start=int(input("Enter the start number:-  "))
end=int(input("Enter the last number:-  "))
print("Prime number between",start,"and",end, "are:")

for num in range(start,end+1):

    if num>1:
# all number is greater than 1
# prime numbers are defined as posetive integer greater than 1
        for i in range(2,num):
            if (num%i)==0:
# if statement check if the current number num is divisible by i
# (i.e., num modulo i is zero).
# if this condition is true, then
                break

        else:

            print(num)