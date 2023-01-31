import random
def GameWin(computer,You):
    if computer==You:
        return None
    elif computer=="s":
        if You=="w":
            return False
        elif You=="g":
            return True
    elif computer=="w":
        if You=="g":
            return False
        elif You=="s":
            return True
    elif computer=="g":
        if You=="w":
            return True
        elif You=="s":
            return False        

computer=input("Computer Turn: Snake(s) Water(w) Gun(g)?")
randNo=random.randint(1,3)
if randNo==1:
    computer="s"
elif randNo==2:
    computer="w"
elif randNo==3:
    computer="g"
You=input("Your Turn: Snake(s) Water(w) Gun(g)?")
print(f"Computer chose {computer}")
print(f"You chose {You}")
a=GameWin(computer,You)
if a==None:
    print("Tie")
elif a:
    print("You win")
else:
    print("You lose")
