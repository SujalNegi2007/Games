#Mastermind
import random
History = {}
def code(b):
    a = []
    for i in range(4):
        a.append(random.randint(1,b))
    return a
def user_guess():
    a = []
    b = input("\nEnter The Four Digit Code Seperated By [,]: ")
    if len(b) != 7:
        print("Invalid Input!")
        b = input("\nEnter The Four Digit Code Seperated By [,]: ")
    c = b.split(",")
    for i in range(4):
        a.append(int(c[i]))
    return a
def check_guess(b):
    a = user_guess()
    c = 0
    d = 0
    for i in range(4):
        if a[i] == b[i]:
            c += 1
    for i in range(4):
        if a[i] in b and a[i] != b[i]:
            d +=1
    summary = (["Exact : ",c],["Partial : ",d])
    print(summary)
    return
def back_menu(lives,b,first_name):
    guess = code(b)
    print("\nGame is starting...\nRandom Code is Generated.\n")
    for i in range(lives):
        check_guess(guess)
        if guess == user_guess():
            print("You Win!")
            History[first_name][0][1] +=1
            break
        print("You Lose!")
        History[first_name][1][1] +=1
    return
def window():
    print("\n+-------------------------------------------+\n| To Play Easy Mastermind       : Enter [1] |\n| To Play Medium Mastermind     : Enter [2] |\n| To Play Hard Mastermind       : Enter [3] |\n| To View History               : Enter [4] |\n| To Clear History              : Enter [5] |\n| To Exit The Mastermind        : Enter [6] |\n+-------------------------------------------+\n")
    return
def main():
    while True:
        full_name = input("Enter Your Name: ").capitalize().strip()
        name = full_name.split(" ")
        first_name = name[0]
        if first_name not in History:
            History[first_name] = [["Won", 0], ["Loss",0]]
            print("Welcome to the Mastermind!")
            while True:
                window()
                menu = int(input(f"{first_name}'s' reply: "))
                if menu == 1:
                    back_menu(12,4,first_name)
                elif menu == 2:
                    back_menu(10,6,first_name)
                elif menu == 3:
                    back_menu(8,8,first_name)
                elif menu == 4:
                    for key, value in dict.items(History):
                        print(f"{key} => {value}")
                elif menu == 5:
                    if first_name in History:
                        History.pop(first_name,None)
                        History[first_name] = [["Won", 0], ["Loss",0]]
                    else:
                        print(f"{first_name} is not in database.")
                elif menu == 6:
                    print("Exiting...\n")
                    break
        else:
            print(f"Welcome Back {first_name} to the Mastermind!")
            while True:
                window()
                menu = int(input(f"{first_name}'s' reply: "))
                if menu == 1:
                    back_menu(12,4,first_name)
                elif menu == 2:
                    back_menu(10,6,first_name)
                elif menu == 3:
                    back_menu(8,8,first_name)
                elif menu == 4:
                    for key, value in dict.items(History):
                        print(f"{key} => {value}")
                elif menu == 5:
                    if first_name in History:
                        History.pop(first_name,None)
                        History[first_name] = [["Won", 0], ["Loss",0]]
                    else:
                        print(f"{first_name} is not in database.")
                elif menu == 6:
                    print("Exiting...\n")
                    break
    return
main()
