#Hangman Game
import random
Options = [
    "ABOUT", "ALERT", "BEACH", "BRAIN", "CHAIN", 
    "DREAM", "ERROR", "FORCE", "GIANT", "HOTEL", 
    "JUDGE", "LIGHT", "MUSIC", "OCEAN", "QUIET",
    "APPLE", "BREAD", "BRUSH", "CHAIR", "CHEST",
    "CHORD", "CLICK", "CLOCK", "CLOUD", "DANCE",
    "DIARY", "DRINK", "FLUTE", "GRAPE", "HOUSE"
]
print("Welcome to the Hangman Game")
Scores = {"Wins": 0, "Losses": 0, "Total_Score": 0}
#_______________________________________________________________________

while True:
    try:
        Menu = int(input("\n+-------------------------------------+\n| To Play The Game        : Enter *1* |\n| To Exit The Game        : Enter *2* |\n| To Check Your Score     : Enter *3* |\n+-------------------------------------+\n"))
        if Menu not in [1,2,3]:
            print("Invalid Option!")
        
    #_______________________________________________________________________
        elif Menu == 1:
            Win = False
            Lives = 6
            Word = random.choice(Options)
            Word_list = []
            Guessed = set()
            for i in range(5):
                Word_list.append(Word[i])
            List = ["_", "_", "_", "_", "_"]
            while True:
                print("\nGuess the word below")
                if len(Guessed) > 0:
                    print(f"{List}\nNote: You have {Lives} lives\nYou have guessed {' '.join(Guessed)} till now")
                else:
                    print(f"{List}\nNote: You have {Lives} lives")
                Guess = input(f"Enter the Letter: ").capitalize()
                if "_" not in List:
                    Win = True
                    break
                elif Lives == 0:
                    Win = False
                    break
                elif Guess in List:
                    print(f"Already Guessed: {Guessed}")
                elif Guess in Word_list:
                    for i in range(5):
                        if Guess == Word_list[i]:
                            List[i] = Guess
                            print(f"{List}")
                    if "_" in List:
                        print(f"\nNote: You have {Lives} lives")
                    else:
                        Win = True
                        break
                elif Guess not in  Word_list:
                    if Guess not in Guessed:
                        Guessed.add(Guess)
                        Lives -= 1
                        print(f"\n{Guess} is not present in the Word.")
                        print(f"\nNote: You have {Lives} lives")
                        if Lives == 0:
                            Win = False
                            break
                    else:
                        print(f"Already Guessed {Guess}!")
            if Win:
                print(f"You Win! You still have {Lives} lives left!")
                if Lives >=4:
                    Scores["Total_Score"] += 2
                    Scores["Wins"] += 1
                else:
                    Scores["Total_Score"] += 1
                    Scores["Wins"] += 1
            else:
                print(f"You Lose! You have {Lives} lives left!")
                print(f'The Word Was {" ".join(Word_list)}')
                Scores["Losses"] += 1
    #_______________________________________________________________________
        elif Menu == 2:
            break
        elif Menu == 3:
            for key, value in Scores.items():
                print(f"{key} : {value}")
    except:
        print("Enter Only Valid Input!")
