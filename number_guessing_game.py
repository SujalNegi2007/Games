#Number Guessing Game
import random
print("Welcome To The Number Guessing Game")
Full_Name = input("Enter Your Full Name: ").strip()
Full_Name = " ".join(w.capitalize() for w in Full_Name.split(" "))
Name = Full_Name.split(" ")
Surname = Name[-1]
Name = Name[0]
Your_Overall_Score = 0
while True:
    Win = False
    Main_Menu = int(input("\nFor Easy Mode(50)      : Enter *1*\nFor Medium Mode(100)   : Enter *2*\nFor Hard Mode(200)     : Enter *3*\nTo Exit The Game       : Enter *4*\nTo check the score     : Enter *5*\n"))
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
            Your_Overall_Score += 1
        else:
            print(f"You lose {Name}! All Guess Used!")
            print(f"The Number was {Computer_guess}")

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
            Your_Overall_Score += 2
        else:
            print(f"You lose {Name}! All Guess Used!")
            print(f"The Number was {Computer_guess}")

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
            Your_Overall_Score += 3
        else:
            print(f"You lose {Name}! All Guess Used!")
            print(f"The Number was {Computer_guess}")

#-----------------------------------------------------------------------
    elif Main_Menu == 4:
        print("Thank you for playing the game!")
        break

    elif Main_Menu == 5:
        print(f"{Full_Name} total score is {Your_Overall_Score}!")
