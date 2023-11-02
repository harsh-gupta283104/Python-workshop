str = input("Enter password")
count1=0
count2=0
count3=0
count4=0
for i in range(0,len(str)):
    ch = str[i]
    if(ch>='0' and ch<='9'):
        count1=count1+1
    elif(ch>='a' and ch<'z' or ch>='A' and ch<='Z'):
        count2=count2+1
    elif(ch == ' '):
        count4 = count4+1
    else:
        count3=count3+1
print(f"Number of digits{count1}, no of alphabet {count2},no of special character {count3}, no of spaces{count4}")