

secret_word = 'higafaf'
lenght = len(secret_word)
hidden_word = ''
lives = 6

letter = input("Enter letter:")
hidden_word = '-' * lenght
ind = [i for i, v in enumerate(secret_word) if letter == v]

hidden_list = list(hidden_word)
for i in ind:
    hidden_list[i] = letter

hidden_word = "".join(hidden_list)
print(hidden_word)

while lives > 0:
    pass







# Create an empty list to hold the letters the user have already chosen
letters_chosen = []

def check_win():
    letter = guess_letter()
    checked = check_letter(letter)
    while lives > 0:
        if checked == secret_word:
            print("You have guess the correct word")
            break
        else:
            pass

def guess_letter():
    while True:
        letter = input("Guess a letter: ").lower()
        if letter in string.ascii_lowercase:
            return letter
        
def check_letter(letter, secret_word):
    #secret_list = list(secret_word) # This will be different if the user found a correct letter in previous iteration
    letter_indices = [index for index, value in enumerate(secret_word) if letter == value]
    """if len(letter_indices) > 0:
        for i in letter_indices:
            secret_list[i] = letter
    return secret_list"""
    return letter_indices

def show_game_status(letter_indices):
    return "".join(list_of_letters)

