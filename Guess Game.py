import random


def guess(x):
    random_number = random.randint(1, x)
    guess_number =0
    while guess_number != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
    if guess_number< random_number:
        print("The guess is too low")
    elif guess_number> random_number:
        print("The guess is too high")
    else:
        print(f"You have guessed the number correctly!")


def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess=low
        feedback=input(f'is {guess} too high(H),too low(L),correct(C)').lowercase
        if feedback=='h':
            high=guess-1
        if feedback=='l':
            low=guess+1

guess(100)

