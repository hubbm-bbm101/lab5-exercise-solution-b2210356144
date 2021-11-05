import random
number = random.randint(0, 100)
loop = 1
while loop == 1:
    guess  = int(input("Guess a number between 0 and 100 :"))
    if guess > number:
        print("Decrease your number")
    elif guess < number:
        print("increase your number")
    else:
        print("This is correct number")
        loop = 0



