from random import randint


def find_min_max() -> list:
    """Find ths minimum and maximum values for the number to be between"""
    while True:
        try:
            min_max = [int(input("Please enter the min value: ")), int(input("Please enter max value: "))]
            if min_max[0] < min_max[1]:
                return min_max
            else:
                print("Make sure the min number is smaller than the max number.")
        except ValueError:
            print("Please enter numbers only.")


def find_guess_limit():
    """Finds if the user wants a guess limit, and sets it if they do"""
    while True:  # Finds if the user wants a guess limit
        guess_limit = input("Would you like to limit your guesses? (Y/N): ").lower()
        if (guess_limit == "y") or guess_limit == "n":
            if guess_limit == "n":
                return None
            while True:  # Gets what the user wants the guess limit to be
                try:
                    guess_limit = int(input("What would you like the guess limit to be: "))
                    if guess_limit > 0:
                        return guess_limit
                    else:
                        print("Make sure the number is greater than zero.")
                except ValueError:
                    print("Please enter only a number.")
        else:
            print("Please only enter Y or N.")


def setup():
    """Sets up the game parameters"""
    min_max = find_min_max()
    guess_limit = find_guess_limit()
    return min_max, guess_limit


def play_round(num: int) -> bool:
    """Goes through one guess by the player"""
    while True:
        try:
            guess = int(input("What do you guess?: "))
            if guess == num:
                print("You got it!")
                return True
            elif guess > num:
                print("The number is lower.")
                return False
            elif guess < num:
                print("The number is higher.")
                return False
        except ValueError:
            print("Please only enter a number.")


def reset() -> [bool]:
    """Checks if the player wants to quit, and if they don't, checks if they want to change the rules"""
    while True:  # Checks if the user wants to quit the game
        close = input("Would you like to exit the game? (Y/N): ").lower()
        if (close == "y") or (close == "n"):
            if close == "y":
                quit()
            else:
                break
        print("Please only enter Y or N.")
    while True:  # Checks if the user wants the rules to be changed
        rule_change = input("Would you like to change the rules? (Y/N): ").lower()
        if (rule_change == "y") or (rule_change == "n"):
            if rule_change == "y":
                return True
            else:
                return False
        print("Please only enter Y or N.")


min_max, guess_limit = setup()
while True:
    num = randint(min_max[0], min_max[1])
    if guess_limit is None:
        while True:
            if play_round(num):
                break
    else:
        for _ in range(guess_limit):
            won = play_round(num)
            if won:
                break
        if not won:
            print("Sorry, you ran out of guesses")
    if reset():
        min_max, guess_limit = setup()