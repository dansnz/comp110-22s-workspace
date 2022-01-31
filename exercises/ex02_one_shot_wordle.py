"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730411941"

secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")

while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
emojis: str = ""

while i < len(secret):
    if guess[i] == secret[i]:
        emojis += GREEN_BOX
    else:
        in_word: bool = False
        alt_indices: int = 0
        while not(in_word) and alt_indices < len(secret):
            if secret[alt_indices] == guess[i]:
                in_word = True
            else: 
                alt_indices += 1
        if in_word is True:
            emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX
    i += 1
print(emojis)


if len(guess) == len(secret):
    if guess != secret:
        print("Not quite. Play again soon!")
    else:
        print("Woo! You got it!")