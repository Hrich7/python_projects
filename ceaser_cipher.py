import string, os


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

def caesar(start_text, shift_amount, cipher_direction):
    end_text = []
    shift_amount %= 26
    alphabet = list(string.ascii_lowercase)
    if cipher_direction.lower() == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            end_text.append(alphabet[(alphabet.index(char) + \
          shift_amount) % 26])
        else:
            end_text.append(char)
    print(f"The {cipher_direction}d text is:  {''.join(end_text)}")



def main():
    go_again = True

    while go_again:
        os.system('clear')
        print(logo)
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

        play_again = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
        if play_again == 'yes' or play_again == 'y':
            go_again = True
        elif play_again == 'no' or play_again == 'n':
            print('Goodbye')
            go_again = False



if __name__ == '__main__':
    main()