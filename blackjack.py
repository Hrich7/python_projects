import os
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def cards_total(cards):
    return sum(cards)

def computer_draw(computer_cards):
    computer_total = cards_total(computer_cards)
    while computer_total < 17:
        computer_cards.append(deal_card())
        if computer_total > 21 and 11 in computer_cards:
            computer_cards= ace_to_one(computer_cards)
        computer_total = cards_total(computer_cards)
    return computer_cards

def ace_to_one(user_cards):
    ind = user_cards.index(11)
    user_cards[ind] = 1
    return user_cards


play = True
while play:
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_game == 'y':
        clear_screen()
        print(logo)

        player_cards = [deal_card() for _ in range(2)]
        computer_cards = [deal_card() for _ in range(2)]

        player_total = cards_total(player_cards)
        computer_total = cards_total(computer_cards)

        print(f"\t\tYour cards: {player_cards}, current score: {(player_total)}")
        print(f"\t\tComputer's first card: {computer_cards[0]}")
        
        if player_total == 21 or computer_total == 21:
            if computer_total == 21:
                print(f"\t\tYour final hand: {player_cards}, final score: {player_total}")
                print(f"\t\tComputer's final hand: {computer_cards}, final score: {computer_total}")
                print("Lose, opponent has Blackjack 😱")
                break
                #or set the while loop to false
            elif player_total == 21:
                print(f"\t\tYour final hand: {player_cards}, final score: {player_total}")
                print(f"\t\tComputer's final hand: {computer_cards}, final score: {computer_total}")
                print("You win. You have a blackjack 😱")
                break
                #or set the while loop to false
        
        else:
            while player_total < 22:
                draw = input("\nType 'y' to get another card, type 'n' to pass: ")
                if draw == 'y':
                    player_cards.append(deal_card())
                    if player_total > 21 and 11 in player_cards:
                        player_cards = ace_to_one(player_cards)
                    player_total = cards_total(player_cards)
                    print(f"\t\tYour cards: {player_cards}, current score: {player_total}")
                    print(f"\t\tComputer's first card: {computer_cards[0]}")

                else:
                    computer_cards = computer_draw(computer_cards)
                    computer_total = cards_total(computer_cards)
                    if computer_total > 21:
                        print(f"\t\tYour final hand: {player_cards}, final score: {player_total}")
                        print(f"\t\tComputer's final hand: {computer_cards}, final score: {computer_total}")
                        print("Opponent went over. You win 😃")
                    else:
                        if player_total > computer_total:
                            print(f"\t\tYour final hand: {player_cards}, final score: {player_total}")
                            print(f"\t\tComputer's final hand: {computer_cards}, final score: {computer_total}")
                            print("You win 😃")
                        elif player_total < computer_total:
                            print(f"\t\tYour final hand: {player_cards}, final score: {player_total}")
                            print(f"\t\tComputer's final hand: {computer_cards}, final score: {computer_total}")
                            print("You lose 😤")
                        else:
                            print(f"\t\tYour final hand: {player_cards}, final score: {player_total}")
                            print(f"\t\tComputer's final hand: {computer_cards}, final score: {computer_total}")
                            print("Draw 🙃")
                    break
            else:
                print(f"\t\tYour final hand: {player_cards}, final score: {player_total}")
                print(f"\t\tComputer's final hand: {computer_cards}, final score: {computer_total}")
                print("You went over. You lose 😭")
    else:
        play = False
   



