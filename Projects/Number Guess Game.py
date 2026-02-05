import random

print("""----------------------------
Welcome to Number Guess Game!
----------------------------
""")
print("""Your task is the guess the number that computer keeps. Enjoy!""")


def main():
    dif = difficulty()
    num = random_number_generator(dif)
    guesser(dif, num, 0)


def difficulty():
    dif = input("""How hard you would like to play ? (1, 2, 3)
    1. Easy (1 - 50)
    2. Medium (1 - 100)
    3. Hard (1 - 500)
    """)

    if dif in ["1", "2", "3"]:
        return dif
    else:
        print("Please enter valid data")
        return difficulty()


def random_number_generator(dif):
    match dif:
        case "1":
            return random.randint(1, 50)
        case "2":
            return random.randint(1, 100)
        case "3":
            return random.randint(1, 500)


def guesser(dif, num, att):
    limits = {"1": 50, "2": 100, "3": 500}
    limit = limits[dif]

    try:
        guess = int(input(f"Please enter your guess (1-{limit}): "))
        if 0 < guess <= limit:
            return game(num, guess, att, dif)
        else:
            print(f"Please enter a value between 1 and {limit}.")
            return guesser(dif, num, att)
    except ValueError:
        print("Please enter valid data")
        return guesser(dif, num, att)


def game(num, guess, att, dif):
    att += 1
    if guess < num:
        print("Higher!")
        return guesser(dif, num, att)
    elif guess > num:
        print("Lower!")
        return guesser(dif, num, att)
    else:
        print(f"Congratulations!\nYou've guessed the number within {att} attempts!")
        again()


def again():
    new = input("\nWould you like to play again ? (y/n): ").lower()
    if new == "y":
        print("Sure, good luck!")
        main()
    elif new == "n":
        print("Well, have a nice day!")
    else:
        print("Please enter valid data")
        again()


if __name__ == "__main__":
    main()