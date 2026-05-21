#Number Guessing Game
import random
print("Welcome To The Number Guessing Game")
Full_Name = input("Enter Your Full Name: ").strip()
Full_Name = " ".join(w.capitalize() for w in Full_Name.split(" "))
Name = Full_Name.split(" ")
Surname = Name[-1]
Name = Name[0]
Scores = {"Easy_Wins": 0, "Medium_Wins": 0, "Hard_Wins": 0, "Total_Score": 0, "Easy_Lose": 0, "Medium_Lose": 0, "Hard_Lose": 0, "Best_attempts_of_Easy_difficulty" : 10,  "Best_attempts_of_Medium_difficulty" : 7, "Best_attempts_of_Hard_difficulty" : 5}

while True:
    Win = False
    try:
        Main_Menu = int(input("\n+------------------------------------+\n| For Easy Mode(50)      : Enter *1* |\n| For Medium Mode(100)   : Enter *2* |\n| For Hard Mode(200)     : Enter *3* |\n| To Exit The Game       : Enter *4* |\n| To check the score     : Enter *5* |\n+------------------------------------+\n"))
        if Main_Menu == 1:
            Computer_guess = random.randint(1,50)
            Odd_Even = Computer_guess % 2
            if Odd_Even == 1:
                Number = "Odd"
            else:
                Number = "Even"
            turns = 1
            for i in range(10):
                Guess_left = 10 - turns
                Player_guess = int(input("\nEnter a number b/w 1 to 50: "))
                if Player_guess < 1 or Player_guess > 50:
                    print("Number b/w 1 to 50 only!")
                elif Player_guess == Computer_guess:
                    Win = True
                    break
                elif turns == 5:
                    print(f"The Number is {Number}")
                    if Player_guess < Computer_guess:
                        print(f"Try a larger number than {Player_guess}. No. of Guess left: {Guess_left}")
                    elif Player_guess > Computer_guess:
                        print(f"Try a smaller number than {Player_guess}. No. of Guess left: {Guess_left}")
                elif Player_guess < Computer_guess:
                    print(f"Try a larger number than {Player_guess}. No. of Guess left: {Guess_left}")
                elif Player_guess > Computer_guess:
                    print(f"Try a smaller number than {Player_guess}. No. of Guess left: {Guess_left}")
                else:
                    print("Only Numbers are allowed!")
                turns += 1
            if Win:
                print(f"Your Win {Name}! No. of Guess Used: {turns}")
                Scores["Easy_Wins"] += 1
                Scores["Total_Score"] += 1
                if turns <= Scores["Best_attempts_of_Easy_difficulty"]:
                    Scores["Best_attempts_of_Easy_difficulty"] = turns
            else:
                print(f"You lose {Name}! All Guess Used!")
                print(f"The Number was {Computer_guess}")
                Scores["Total_Score"] -= 1
                Scores["Easy_Lose"] += 1

#-----------------------------------------------------------------------
        elif Main_Menu == 2:
            Computer_guess = random.randint(1,100)
            Odd_Even = Computer_guess % 2
            if Odd_Even == 1:
                Number = "Odd"
            else:
                Number = "Even"
            turns = 1
            for i in range(7):
                Guess_left = 7 - turns
                Player_guess = int(input("\nEnter a number b/w 1 to 100: "))
                if Player_guess < 1 or Player_guess > 100:
                    print("Number b/w 1 to 100 only!")
                elif Player_guess == Computer_guess:
                    Win = True
                    break
                elif turns == 4:
                    print(f"The Number is {Number}")
                    if Player_guess < Computer_guess:
                        print(f"Try a larger number than {Player_guess}. No. of Guess left: {Guess_left}")
                    elif Player_guess > Computer_guess:
                        print(f"Try a smaller number than {Player_guess}. No. of Guess left: {Guess_left}")
                elif Player_guess < Computer_guess:
                    print(f"Try a larger number than {Player_guess}. No. of Guess left: {Guess_left}")
                elif Player_guess > Computer_guess:
                    print(f"Try a smaller number than {Player_guess}. No. of Guess left: {Guess_left}")
                else:
                    print("Only Numbers are allowed!")
                turns += 1
            if Win:
                print(f"Your Win {Name}! No. of Guess Used: {turns}")
                Scores["Medium_Wins"] += 2
                Scores["Total_Score"] += 2
                if turns <= Scores["Best_attempts_of_Medium_difficulty"]:
                    Scores["Best_attempts_of_Medium_difficulty"] = turns
            else:
                print(f"You lose {Name}! All Guess Used!")
                print(f"The Number was {Computer_guess}")
                Scores["Total_Score"] -= 2
                Scores["Medium_Lose"] += 1
    
    #-----------------------------------------------------------------------
        elif Main_Menu == 3:
            Computer_guess = random.randint(1,200)
            Odd_Even = Computer_guess % 2
            if Odd_Even == 1:
                Number = "Odd"
            else:
                Number = "Even"
            turns = 1
            for i in range(5):
                Guess_left = 5 - turns
                Player_guess = int(input("\nEnter a number b/w 1 to 200: "))
                if Player_guess < 1 or Player_guess > 200:
                    print("Number b/w 1 to 200 only!")
                elif Player_guess == Computer_guess:
                    Win = True
                    break
                elif turns == 3:
                    print(f"The Number is {Number}")
                    if Player_guess < Computer_guess:
                        print(f"Try a larger number than {Player_guess}. No. of Guess left: {Guess_left}")
                    elif Player_guess > Computer_guess:
                        print(f"Try a smaller number than {Player_guess}. No. of Guess left: {Guess_left}")
                elif Player_guess < Computer_guess:
                    print(f"Try a larger number than {Player_guess}. No. of Guess left: {Guess_left}")
                elif Player_guess > Computer_guess:
                    print(f"Try a smaller number than {Player_guess}. No. of Guess left: {Guess_left}")
                else:
                    print("Only Numbers are allowed!")
                turns += 1
            if Win:
                print(f"Your Win {Name}! No. of Guess Used: {turns}")
                Scores["Hard_Wins"] += 3
                Scores["Total_Score"] += 3
                if turns <= Scores["Best_attempts_of_Hard_difficulty"]:
                    Scores["Best_attempts_of_Hard_difficulty"] = turns
            else:
                print(f"You lose {Name}! All Guess Used!")
                print(f"The Number was {Computer_guess}")
                Scores["Total_Score"] -= 3
                Scores["Hard_Lose"] += 1
    
    #-----------------------------------------------------------------------
        elif Main_Menu == 4:
            print("Thank you for playing the game!")
            break
    
        elif Main_Menu == 5:
            for num, score in Scores.items():
                print(f"{num} : {score}")
    except:
        print("Enter Only Valid Input")
