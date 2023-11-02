import random
def guess_number():
    return random.randint(1, 100)
target_number= guess_number()
attempt=0

while True:
    User_guess= int(input("Guess the number:"))
    attempt+=1
    if User_guess==target_number:
        print("Congratulation! You passed the number ",attempt,"attempts")
        break
    elif User_guess<target_number:
        print("Try a higher Number.")
    else:
        print("Try a lower number.")
    