import random


def main():
    # Gets user's guess.
    userGuess = str(input("Enter a three digit number: "))

    # Generate a random three digit number.
    ranNumber = str(random.randrange(100, 1000))

    print("The lotery number is " + ranNumber)

    # If the user's guess and generated number are the same they win 10k!
    if userGuess == ranNumber:
        print("You have won $10,000!")
    else:
        # Checks that all numbers in the users guess are in the random number,
        if all((userGuess[0] in ranNumber, userGuess[1] in ranNumber, userGuess[2] in ranNumber)):
            print("You have won $3,000!")

        # At least one number matched.
        elif any((userGuess[0] in ranNumber, userGuess[1] in ranNumber, userGuess[2] in ranNumber)):
            print("You have won $1,000!")

        # Nothing matched, they get nothing.
        else:
            print("You Lose!")


main()
