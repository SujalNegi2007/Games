# Snake And Ladder
import random
print("Welcome To Snakes & Ladders")

while True:
    try:
        menu = int(input("\n+--------------------------+\n| To Start Game: Enter [1] |\n| To Exit Menu : Enter [2] |\n+--------------------------+\n"))
#--------------------------------------------------------------------------------
        if menu == 1:
            player = {"player1", "player2"}
            bot1 = player.pop()
            bot2 = player.pop()
            position = {"player1" : 0, "player2" : 0}
            win_bot1 = False
            win_bot2 = False
            snake_ladder = {random.randint(1,90) : random.randint(1,90), random.randint(1,90) : random.randint(1,90), random.randint(1,90) : random.randint(1,90), random.randint(1,90) : random.randint(1,90), random.randint(1,90) : random.randint(1,90), random.randint(1,90) : random.randint(1,90), random.randint(1,90) : random.randint(1,100), random.randint(1,100) : random.randint(1,100), random.randint(1,90) : random.randint(1,90), random.randint(1,90) : random.randint(1,90), random.randint(1,90) : random.randint(1,90)}
#--------------------------------------------------------------------------------
            while True:
                dice = random.randint(1,6)
                print(f"It is {bot1} turn")
                input(f"Enter to roll the dice {bot1}: ").capitalize().strip()
                if position[bot1] <= 100 and position[bot1] + dice <= 100 :
                    position[bot1] += dice
                    if position[bot1] == 100:
                        win_bot1 = True
                        break
                elif position[bot1] + dice > 100:
                    print(f"{bot1} can't move as dice needs to be {100 - position[bot1] } or less to move.")
                print(f"{bot1} got {dice}. {bot1} moves {dice} boxes. Position of {bot1} is {position[bot1]}\n")
                if position[bot1] in snake_ladder.keys():
                        if position[bot1] > snake_ladder[position[bot1]]:
                            print(f"{bot1} got bitten by the snake and has been moved to {snake_ladder[position[bot1]]} for treatment!")
                        elif position[bot1] < snake_ladder[position[bot1]]:
                            print(f"{bot1} hired a taxi and is now at {snake_ladder[position[bot1]]}!")
                        elif position[bot1] == snake_ladder[position[bot1]]:
                            print(f"{bot1} is taking a stroll!")
                        position[bot1] = snake_ladder[position[bot1]]
#--------------------------------------------------------------------------------
                dice = random.randint(1,6)
                print(f"It is {bot2} turn")
                input(f"Enter to roll the dice {bot2}: ").capitalize().strip()
                if position[bot2] <= 100 and position[bot2] + dice <= 100 :
                    position[bot2] += dice
                    if position[bot2] == 100:
                        win_bot2 = True
                        break
                elif position[bot2] + dice > 100:
                    print(f"{bot2} can't move as dice needs to be {100 - position[bot2] } or less to move.")
                print(f"{bot2} got {dice}. {bot2} moves {dice} boxes. Position of {bot2} is {position[bot2]}\n")
                if position[bot2] in snake_ladder.keys():
                        if position[bot2] > snake_ladder[position[bot2]]:
                            print(f"{bot2} got bitten by the snake and has been moved to {snake_ladder[position[bot2]]} for treatment!")
                        elif position[bot2] < snake_ladder[position[bot2]]:
                            print(f"{bot2} hired a taxi and is now at {snake_ladder[position[bot2]]}!")
                        elif position[bot2] == snake_ladder[position[bot2]]:
                            print(f"{bot2} is taking a stroll!")
                        position[bot2] = snake_ladder[position[bot2]]
#--------------------------------------------------------------------------------
            if win_bot1:
                print(f"{bot1} Won the match!")
            elif win_bot2:
                print(f"{bot2} Won the match!")
            else:
                print("Someting Gone Wrong!")
#--------------------------------------------------------------------------------
        elif menu == 2:
            break
        else:
            print(f"Enter Valid Input Instead of {menu}!")
    except:
        print("Enter Valid Input!")
