import random
from hangman_art import logo, stages
from hangman_words import wordlist
import os

def generate_random_common_word():
    return random.choice(wordlist)


def main():
    chosen_word = generate_random_common_word()
    word_length = len(chosen_word)
    correct_guesses = []
    incorrect_guesses = []
    end_of_game = False
    lives = 6

    display = []
    for _ in range(word_length):
        display += '_'

    print(lives)
    while not end_of_game:
        os.system('clear')
        print(logo)
        print(f"{chosen_word}\n")
        print(f"Incorrect Letters: {list(set(incorrect_guesses))}")
        print(f"Lives: {lives}")
        #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}\n")
        print(stages[lives])

        guess = input("Guess a letter: ").lower()
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
                correct_guesses += guess

          #Check if user is wrong.
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            incorrect_guesses.append(guess)
            if lives == 0:
                end_of_game = True
                os.system('clear')
                print("You lose.")

        #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            os.system('clear')
            print("You win.")

        print(stages[lives])

if __name__ == "__main__":
    main()


