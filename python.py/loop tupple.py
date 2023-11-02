this_tupple=("apple","Banana","Cherry")
i=0
while i< len(this_tupple):
    print(this_tupple[i])
    i+=1

this_tupple=("apple","banana","cherry")
for i in range(len(this_tupple)):
    print(this_tupple)

this_tupple=("apple",)


fruits=("apple","banana","cherry")
mytuple=fruits*2
print(mytuple)

this_tupple=(1,2,3,4,5,6,7,8,9,0)
x=this_tupple.index(8)
print(x)

fruit=("apple","banana","cherry")
(green, yellow, red)=fruits

print(green)
print(yellow)
print(red)

fruits=("apple","banana", "cherry", "pinapple", "cherry")
(green, *tropic , red)=fruits

print(green)
print(tropic)
print(red)



this_tupple=(1,2,3,4,5,6,7,8,9,0)
x=this_tupple.count(4)
print(x)