import random

d=random.randint(0,2)
print(d)
y = int(input("Choose Rock, Paper or Scissor!\n Enter 1 for Rock :\n Enter 2 for Paper :\n Enter 3 for Scissor : "))
if y < 1 or y > 3:
    print("Wrong Pick!!\n Please enter 1, 2 or 3")
    exit()
else:
    if(y==d):
        print("It is a DRAW!!")
    elif((y==1 and d==3) or (y==2 and d==1) or (y==3 and d==2)):
        print("Anhad, You WON!!")
    else:
        print("Anhad, You LOSE!!")
