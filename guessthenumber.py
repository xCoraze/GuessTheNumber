import random
secretNumber = random.randint(1, 25)
print("Ich denke an eine Zahl zwischen 1 und 25.")

for guessesTaken in range(1, 7):
    print("Errate die Zahl!")
    guess = int(input())

    if guess < secretNumber:
        print('Diese Zahl ist zu niedrig.')
    elif guess > secretNumber:
        print("Diese Zahl ist zu hoch.")
    else:
        break

if guess == secretNumber:
    print("Du liegst richtig! Du hast die Zahl in " + str(guessesTaken) + " Versuchen erraten.")