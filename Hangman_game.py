#Hangman Game
import random
Options = [
    "ABOUT", "ALERT", "BEACH", "BRAIN", "CHAIN", 
    "DREAM", "ERROR", "FORCE", "GIANT", "HOTEL", 
    "JUDGE", "LIGHT", "MUSIC", "OCEAN", "QUIET"
]
print("Welcome to the Hangman Game")
Your_Overall_Score = 0
#_______________________________________________________________________

while True:
    Menu = int(input("\nTo Play The Game        : Enter *1*\nTo Exit The Game        : Enter *2*\nTo Check Your Score     : Enter *3*\n"))
    if Menu not in [1,2,3]:
        print("Invalid Option!")
    
#_______________________________________________________________________
    elif Menu == 1:
        Win = False
        Lives = 6
        Word = random.choice(Options)
        Word_list = []
        for i in range(5):
            Word_list.append(Word[i])
        List = ["_", "_", "_", "_", "_"]
        while True:
            print("\nGuess the word below")
            print(f"{List}\nNote: You have {Lives} lives")
            Guess = input(f"Enter the Letter: ").capitalize()
            if "_" not in List:
                Win = True
                break
            elif Lives == 0:
                Win = False
                break
            elif Guess in List:
                print("Already Guessed!")
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
                Lives -= 1
                print(f"\n{Guess} is not present in the Word.")
                print(f"\nNote: You have {Lives} lives")
                if Lives == 0:
                    Win = False
                    break
        if Win:
            print(f"You Win! You still have {Lives} lives left!")
            if Lives >=4:
                Your_Overall_Score += 2
            else:
                Your_Overall_Score += 1
        else:
            print(f"You Lose! You have {Lives} lives left!")
            print("".join(Word_list))
#_______________________________________________________________________
    elif Menu == 2:
        break
    elif Menu == 3:
        print(f"Total score: {Your_Overall_Score}")
