import random


def guess_the_number():
    secret_number = random.randint(1, 100)

    attempts = 0
    guessed = False

    print("Welcome to the Guess the Number Game!")

    while not guessed:
        guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("You are Dumb!")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congrats! You guessed the number {secret_number} in {attempts} attempts.")
            guessed = True


guess_the_number()
input()