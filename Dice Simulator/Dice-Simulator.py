import random
print("======= Welcome to Dice Simpulator ========")
print("=====             Start               =====")
click = "y"
while(click == "y"):
    dice = random.randint(1, 6)
    if dice == 1:
        print("---------")
        print("|        |")
        print("|   0    |")
        print("|        |")
        print("---------")
    elif dice == 2:
        print("---------")
        print("|        |")
        print("| 0   0  |")
        print("|        |")
        print("---------")
    elif dice == 3:
        print("---------")
        print("|   0    |")
        print("|   0    |")
        print("|   0    |")
        print("---------")
    elif dice == 4:
        print("---------")
        print("| 0   0  |")
        print("|        |")
        print("| 0   0  |")
        print("---------")
    elif dice == 5:
        print("---------")
        print("| 0    0 |")
        print("|   0    |")
        print("| 0    0 |")
        print("---------")
    elif dice == 6:
        print("---------")
        print("| 0    0 |")
        print("| 0    0 |")
        print("| 0    0 |")
        print("---------")

    click = input("Press y to roll again ")
print("========         End       =========")