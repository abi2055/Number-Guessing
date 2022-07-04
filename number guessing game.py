import random

def guess_user():
    secret_number = random.randint(1,10)
    guess = 0
    while guess != secret_number:
        guess = int(input("Guess a number from 1 to 10: "))
        if guess > 10 or guess < 1:
            print("Your guess was out of range! Please guess again!")
        elif guess < secret_number:
            print("Try Again! Guess was too Low")
        elif guess > secret_number:
            print("Try Again! Guess was too High")

    print(f"You Guessed Correct! The number was {secret_number}")

def guess_comp():
    low = 1
    high = 10
    user_feedback = ""
    while user_feedback != "correct":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = high
        user_feedback = input(f"Is {guess} too high, too low or correct: ").lower()
        if user_feedback == "high":
            print("My guess was too high!")
            high = guess - 1
        elif user_feedback == "low":
            print("My guess was too low!")
            low = guess + 1
        elif user_feedback != "correct":
            print("I cannot understand your feedback!")

    print(f"I guessed correct! Your number was {guess}")

decision = ""
while decision != "quit":
    print("""
Options:
1 --> You Guess the Computer's Number
2 --> Computer Guesses Your Number 
3 --> Quit
    """)
    decision = int(input("What Would You Like to Do (Options 1,2 or 3)? "))
    if decision == 1:
        guess_comp()
    elif decision == 2:
        guess_user()
    elif decision == 3:
        print("You quit! Please Play Again Soon!")
        break
    else:
        print("Invalid Option! Please Try Again!")
