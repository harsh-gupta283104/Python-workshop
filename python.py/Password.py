while True:
    i=input("enter password: ")
    if len(i)<12:
        print("please! enter password of more than 12 char")
    else:
        a=b=c=e=f=0
        for j in i:
            if j.isdigit():
                a+=1
            elif j.isalpha():
                if j.isupper():
                    b+=1
                if j.islower():
                    c+=1
            elif j.isspace():
                e+=1
            elif (j in "!@#$%^&*"):
                f+=1
        
        if (a==0 or b==0 or c==0 or e!=0 or f==0):
            print("please! enter strong pass")
        else:
            print("password confirmed")
            break