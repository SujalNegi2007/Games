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
    win = False
    a = user_guess()
    guess_used = [False, False, False, False]
    code_used = [False, False, False, False]
    c = 0
    d = 0
    for i in range(4):
        if a[i] == b[i]:
            c += 1
            guess_used[i] = True
            code_used[i] = True
    if c == 4:
        win = True
    for i in range(4):
        if not guess_used[i]:
            for j in range(4):
                if not code_used[j] and a[i] == b[j]:
                    d +=1
                    code_used[j] = True
                    break
                    
                    
    summary = (["Exact : ",c],["Partial : ",d])
    print(summary)
    return win
#-----------------------------------------------------------------------
def back_menu(lives,b,first_name):
    fixed_code = code(b)
    for i in range(lives):
        win = check_guess(fixed_code)
        if win:
            print("You Win!")
            History[first_name][0][1] += 1
            break
    else:
        print("You lose!")
        History[first_name][1][1] += 1
    return
def window():
    print("\n+-------------------------------------------+\n| To Play Easy Mastermind       : Enter [1] |\n| To Play Medium Mastermind     : Enter [2] |\n| To Play Hard Mastermind       : Enter [3] |\n| To View History               : Enter [4] |\n| To Clear History              : Enter [5] |\n| To Exit The Mastermind        : Enter [6] |\n+-------------------------------------------+\n")
    return
def front_menu(first_name):
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
def main():
    while True:
        full_name = input("Enter Your Name: ").capitalize().strip()
        name = full_name.split(" ")
        first_name = name[0]
        if first_name not in History:
            History[first_name] = [["Won", 0], ["Loss",0]]
            print("Welcome to the Mastermind!")
            front_menu(first_name)
        else:
            print(f"Welcome Back {first_name} to the Mastermind!")
            front_menu(first_name)
    return
main()
