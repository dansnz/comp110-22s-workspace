"""Exercise 03 - Structured Wordle."""

__author__ = "730411941"


def main() -> None:
    """The entry point of the program and main game loop."""
    secret: str = "codes"
    i: int = 1
    while i < 7:
        print(f"=== Turn {i}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {i}/6 turns!")
            quit()
        else:
            i += 1
    print("X/6 - Sorry, try again tomorrow!")
        
        
def input_guess(expected_length: int) -> str:
    """Designed to prompt the user for a guess that meets expected length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def contains_char(string: str, character: str) -> bool:
    """Designed to know if the character is in the string."""
    assert len(character) == 1
    in_string: bool = False
    index: int = 0
    while not(in_string) and index < len(string):
        if character == string[index]:
            in_string = True
        else:
            index += 1
    if in_string is True:
        return True
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """Designed to concatenate a str of emojis."""
    assert len(guess) == len(secret)
    emojis: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            emojis += GREEN_BOX
        else:
            if contains_char(secret, guess[i]) is True:
                emojis += YELLOW_BOX
            else:
                emojis += WHITE_BOX
        i += 1
    return emojis


if __name__ == "__main__":
    main()