import random
while True:
    a = int(input("Enter your choice:\n1=> Rock\n2=> Paper\n3=> Scissors\n4=>Exit Game "))
    b = random.randint(1, 3)
    if a == 1:
        if b == 1:
            print("Draw")
            continue
        elif b == 2:
            print("You Lose")
            continue
        else:
            print("You Win")
            continue
    elif a == 2:
        if b == 1:
            print("You Win")
            continue
        elif b == 2:
            print("Draw")
            continue
        else:
            print("You Lose")
            continue
    elif a == 3:
        if b == 1:
            print("You Lose")
            continue
        elif b == 2:
            print("You Win")
            continue
        else:
            print("Draw")
            continue
    else:
        break
