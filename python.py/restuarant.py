# If you are using OR in programme then the condition for the OR:- If any one condition is correct of any statement the result will be that but u r using and then every condition should be right
print("Welcome to resturant")
print("How can I help you.")
one="Burger"
two="Chowmein"
three="Momos"
four="Coffe with Biscuit"
five="Chicken"
six="Special Non-veg"
type_of_food=str(input("First of tell me are you veg or non-veg (in v and n and all):")).lower()
amount_of_customer=float(input("What is your amout limit that you afford: "))
time_of_customer=float(input("How much time you can spend here (in minute): "))
# The mistake is here in if statement
if type_of_food=="v" and amount_of_customer<= 100 and time_of_customer<=20:
    print("Menu relevant for you as follow:-",one,two,)
elif type_of_food=="v" and amount_of_customer>100 and time_of_customer>20:
    print("The menu relevant for you as follows:- ",three,four)
elif type_of_food=="n" and amount_of_customer>300 and time_of_customer>60:
    print("The menu suitable for you as follows:", five, six,)
elif type_of_food=="all" and amount_of_customer>300 and time_of_customer>60:
    print("The menu suitable for you as follows:", one, two, three, four,five, six,)
else :
    print("You have entered any wrong value")