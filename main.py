import random

ladder ={4:56, 22:72, 41:95}
snake ={48:6, 94:50, 75:10}
pos1 = 0

def move(pos):
    dice=random.randint(1,6)
    if dice == 1:
        print(f"Dice:{dice} \u2680")
    elif dice == 2:
        print(f"Dice:{dice} \u2681")
    elif dice == 3:
        print(f"Dice:{dice} \u2682")
    elif dice == 4:
        print(f"Dice:{dice} \u2683")
    elif dice == 5:
        print(f"Dice:{dice} \u2684")
    else:
        print(f"Dice:{dice} \u2685")
    temp_pos = pos
    pos = pos + dice
    if pos in snake:
       print("Bitten by snake \U0001F40D")
       pos = snake[pos]
       print(f"Position:{pos}")
    elif pos in ladder:
        print("Climbed by ladder #")
        pos = ladder[pos]
        print(f"Position:{pos}")
    elif pos > 100:
        print("Invalid move try again. \u274C")
        pos = temp_pos
        print(f"Position:{pos}")
    else:
        print(f"Position:{pos}")
    print("\n")
    return pos

while True:
    A = input("Press \"ENTER\" to throw dice ")
    pos1 = move(pos1)
    if pos1 == 100:
        print("Congratulations you WON! \U0001F3C6")
        break