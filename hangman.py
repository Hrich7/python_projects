import nltk # we have to "pip install nltk" to be able to use this natural langual toolkit library
import random
import string

# Download the words corpus and brown corpora
nltk.download('words')
nltk.download('brown')

# Get a list of English words
#from nltk.corpus import words

# Load the words corpus and the Brown corpus
word_list = nltk.corpus.words.words()
brown_words = nltk.corpus.brown.words()

# Set to store common words 
common_word_set = set(word.lower() for word in brown_words)

def generate_random_common_word():
    common_word = random.choice(word_list)
    while common_word.lower() not in common_word_set:
        common_word = random.choice(word_list)
    return common_word

def guess_letter():
    while True:
        letter = input("Guess a letter: ").lower()
        if letter in string.ascii_lowercase:
            return letter
        else:
            print(f"You have Enter '{letter}' which is not a letter\n")
        
def check_letter_in_word(letter, secret_word):
    letter_indices = [index for index, value in enumerate(secret_word) if letter == value]
    return letter_indices

def show_board(letter,letter_indices, hidden_word):
    hidden_list = list(hidden_word)
    for i in letter_indices:
        hidden_list[i] = letter
    return "".join(hidden_list)

def check_win(hidden_word, secret_word):
    if hidden_word == secret_word:
        return True
    else:
        return False

def main():
    tries = 6
    secret_word = generate_random_common_word()
    hidden_word = "-" * len(secret_word)
    incorrect_letters = []

    print(f"{'=' * 60}")
    player_name = input("Hello! Welcome to our hangman game. \nWhat is your name: ".upper())
    print(f"Well {player_name}, you have 6 tries to get the correct word".upper())
    print(f"{'=' * 60}")
    print(f"\t\tThe secret word has {len(secret_word)} letters\n")
   
    while tries > 0:
        print(f"{'=' * 30}")
        print(f"{hidden_word}\n")
        print(f"Incorrect Letters: {incorrect_letters}")
        print(f"Tries: {tries}")

        letter = guess_letter()
        letter_indices = check_letter_in_word(letter, secret_word)
    
        if len(letter_indices) > 0:
            hidden_word = show_board(letter,letter_indices, hidden_word)
            print(f"We have found {len(letter_indices)} '{letter}' in the secret word")
            
        else:
            incorrect_letters.append(letter)
            print(f"Sorry there is no '{letter}' in the secret word")
            tries -= 1

        if check_win(hidden_word, secret_word):
            print(f"""
                  \tCongrats! You have found the secret word: {secret_word}""")
            return 0
        
    print(f"{'=' * 60}")
    print(f"Sorry you have run out of tries. The secret word was:{secret_word} ")

if __name__ == "__main__":
    main()