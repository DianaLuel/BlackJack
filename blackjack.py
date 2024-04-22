import random

cards= [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """It deals new card"""
    new_card = random.choice(cards)
    return new_card

def calculate_score(cards):
    
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, oppenent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over, You lose"
    elif computer_score >21:
        return "Opponent went over, You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    user_cards=[]
    computer_cards=[]
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    ##########check#########
    #print(user_cards, computer_cards)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        ##########check#########
        #print(user_score, computer_score)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal=input("Do you want to draw another card? Type 'Y' or 'N': ").upper()
            if user_should_deal == "Y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
        ##########check#########
        #print(is_game_over)

    while computer_score !=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
        #####check#####
        #print(computer_cards, computer_score)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you wanna play a game of BlackJack? Type 'Y' or 'N': ").upper() == "Y":
    play_game()

##we can clear it by from replit import clear and clear()
