import random
secretNumber = random.randint(1, 25)
print("I am thinking of a number between 1 and 25.")

for guessesTaken in range(1, 7):
    print("Errate die Zahl!")
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break

if guess == secretNumber:
    print("Good job! You guessed the number in " + str(guessesTaken) + " guesses.")
