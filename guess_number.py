from random import *

tries = 8
magic_number = randint(1,101)
print(magic_number)

name = input("\t\t\t\tWelcome to our 'Guess the number game'\nWhat is your name: ")
print(f"""Well {name} I've thought of a number between 1 and 100 and you only have eight tries to guess it. 
What number do you think it is?\n""")

while tries > 0:
    player_guess = int(input("\nWhat is your guess: "))
    if player_guess < 1 or player_guess > 100 :
        tries -= 1
        print("You have chosen a number that is out of play")
    elif player_guess < magic_number:
        tries -= 1 
        print(f"Sorry Wrong answer : {player_guess} is less than the magic number")
    elif player_guess > magic_number:
        tries -= 1 
        print(f"Sorry Wrong answer : {player_guess} is greater than the magic number")
    else:
        tries -= 1
        print(f"Congrats you have guessed the magic number '{player_guess}' in {8 - tries} attempt(s)")
        break
    print(f"You have {tries} more tries")
else:
    print(f"Sorry you have run out of tries. The magic number was {magic_number}")