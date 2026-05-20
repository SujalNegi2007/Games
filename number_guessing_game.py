import random
num = random.randint(1,100)
print("Welcome to the Number Guessing Game!")
i=1
while True:
    guess = int(input("Enter Your Guess: "))
    if guess == num:
        print(f"{guess} is the correct answer!")
        print(f"It took you {i} turns.")
        break
    elif guess < 1 or guess > 100:
        print("Try guessing b/w 1 to 100.")
    elif guess < num:
        print("Your Guess is low. Try entering higher number.")
    elif guess > num:
        print("Your Guess is high. Try entering lower number.")
    else:
        print("Only integers are allowed!")
    i += 1
print("Calculating Your Result.")
if i == 1:
    print("You are in 1%. Your luck is too good to be true.")
elif i<=4:
    print("Good One bro!")
elif i <= 7:
    print("Average!")
elif i <= 10:
    print("Try another day!")
else:
    print("You are banned from the game! And it's for your own good.")
