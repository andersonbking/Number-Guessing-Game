import random

answer = random.randint(1, 10)
guess = None

while guess != answer:
    guess = int(input("Guess a number 1 - 10: "))
    if guess == answer:
        print("You guessed correctly!")
    else:
        print("Incorrect, try again.")
