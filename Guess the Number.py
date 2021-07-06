import random

number=random.randint(0,100)
guesses=1
print("You have only 10 chances to win , Guess the number between 0 to 100....best of luck")
while guesses<=10:
    io = int(input("Guess any number:-"))

    if io>number:
        print("\nGuess LESSER number")

    elif io<number:
        print("\nGuess GREATER number")

    else:
        print("you won the game...")
        print("You took ",guesses,"number of guesses to win")
        break
    print("\t\t\t\t\t\tLeft no. of guesses:-",10-guesses)
    guesses+=1

if guesses>10: print("Game over")