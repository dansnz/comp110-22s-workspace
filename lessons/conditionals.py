"""Working with (If-Else) conditional statements."""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
    print("BAOW!!!")
else:
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("you guessed too high!")
    else:
        print("You guessed too low!")

print("Game over.")