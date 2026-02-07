import random

secret = random.randint(1, 10)

print("I'm thinking of a number between 1 and 10.")

guess = int(input("Take a guess:    "))

if guess == secret:
    print("Nice! You guessed it")
else: 
    print("Nope! The number was", secret)

    