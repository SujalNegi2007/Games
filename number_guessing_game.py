#Number Guessing Game
#__________________________________________________________________________
import random
scores = {"Easy_Wins": 0, "Medium_Wins": 0, "Hard_Wins": 0, "Total_Score": 0, "Easy_Lose": 0, "Medium_Lose": 0, "Hard_Lose": 0, "Best_attempts_of_Easy_difficulty" : 10,  "Best_attempts_of_Medium_difficulty" : 7, "Best_attempts_of_Hard_difficulty" : 5}
#__________________________________________________________________________
def name_func():
    full_name = input("Enter Your Full Name: ").capitalize().strip()
    name = full_name.split(" ")
    surname = name[-1]
    first_name = name[0]
    return first_name
#__________________________________________________________________________
def window():
    return ("\n+------------------------------------+\n| For Easy Mode(50)      : Enter *1* |\n| For Medium Mode(100)   : Enter *2* |\n| For Hard Mode(200)     : Enter *3* |\n| To Exit The Game       : Enter *4* |\n| To check the score     : Enter *5* |\n+------------------------------------+\n")
#__________________________________________________________________________
def front_menu(a,name,b):
    computer_guess = random.randint(1,b)
    condition = ["Easy" if a == 10 else "Medium" if a == 7 else "Hard" if a == 5 else "Invalid Input"]
    win = False
    number = ["Odd" if computer_guess%2 == 1 else "Even"]
    turns = 1
    for i in range(a):
        guess_left = a - turns
        player_guess = int(input(f"\nEnter a number b/w 1 to {b}: "))
        c = ["It's getting hot..." if 0 <= player_guess - computer_guess <= 10 else "It's getting warm..." if 11 <= player_guess - computer_guess <= 20 else "It's getting cold..." ]
        if player_guess < 1 or player_guess > b:
            print(f"Number b/w 1 to {b} only!")
        elif player_guess == computer_guess:
            win = True
            break
        elif turns == a//2:
            print(f"The Number is {number[0]}")
            if player_guess < computer_guess:
                print(f"Try a larger number than {player_guess}. No. of Guess left: {guess_left}. {c[0]}")
            elif player_guess > computer_guess:
                print(f"Try a smaller number than {player_guess}. No. of Guess left: {guess_left}. {c[0]}")
        elif player_guess < computer_guess:
            print(f"Try a larger number than {player_guess}. No. of Guess left: {guess_left}. {c[0]}")
        elif player_guess > computer_guess:
            print(f"Try a smaller number than {player_guess}. No. of Guess left: {guess_left}. {c[0]}")
        else:
            print("Only Numbers are allowed!")
        turns += 1
    if win:
        print(f"Your win! {name}! No. of Guess Used: {turns}")
        scores[f"{condition[0]}_Wins"] += 1
        scores["Total_Score"] += 1
        if turns <= scores[f"Best_attempts_of_{condition[0]}_difficulty"]:
            scores[f"Best_attempts_of_{condition[0]}_difficulty"] = turns
    else:
        print(f"You Lose! {name}! All Guess Used!")
        print(f"The Number was {computer_guess}")
        scores["Total_Score"] -= 1
        scores[f"{condition[0]}_Lose"] += 1
#______________________________________________________________________
while True:
    print("Welcome To The Number Guessing Game")
    first_name = name_func()
    while True:
        print(window())
        Main_Menu = int(input())
        if Main_Menu == 1:
            front_menu(10,first_name,50)
        elif Main_Menu == 2:
            front_menu(7,first_name,100)
        elif Main_Menu == 3:
            front_menu(5,first_name,200)
        elif Main_Menu == 4:
            print("Thank you for playing the game!")
            break
        elif Main_Menu == 5:
            for num, score in scores.items():
                print(f"{num} : {score}")
        else:
            print("Invalid Input!")
