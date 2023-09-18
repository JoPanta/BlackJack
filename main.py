import random
import art
from clear import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play():
    global should_continue
    global user_cards
    global pc_cards
    global user_score
    global pc_score
    global round
    round = 1
    should_continue = True
    user_cards = random.choices(cards, k=2)
    pc_cards = random.choices(cards, k=2)
    user_score = sum(user_cards)
    pc_score = sum(pc_cards)
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == "y":
        clear()
        print(art.logo)
    if play == "n":
        should_continue = False
        clear()


def show_cards():
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {pc_cards[0]}")


play()
while should_continue:
    if round == 1 and user_score == 21 and pc_score < 21:
        show_cards()
        print("You win with a Blackjack 😎")
        should_continue = False
        play()
    elif pc_score == 21:
        show_cards()
        print("You lose, opponent has Blackjack 😱")
        should_continue = False
        play()
    elif user_score > 21:
        if 11 in user_cards:
            ace = user_cards.index(11)
            user_cards[ace] = 1
            user_score = sum(user_cards)
        else:
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print(
                f"Computer's final hand: {pc_cards}, final score: {pc_score}")
            print("You went over. You lose 😭")
            should_continue = False
            play()

    show_cards()
    if should_continue == True:
        another_card = input(
            "Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "n":
            while pc_score < 17:
                pc_cards.append(random.choice(cards))
                pc_score = sum(pc_cards)
                if 11 in pc_cards:
                    ace = pc_cards.index(11)
                    pc_cards[ace] = 1
                    pc_score = sum(pc_cards)
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print(
                f"Computer's final hand: {pc_cards}, final score: {pc_score}")
            if pc_score > 21 and 11 not in pc_cards:
                print("Opponent went over. YOU WIN 😁")
                play()
            elif pc_score > user_score:
                print("YOU LOSE 😤")
                play()
            elif pc_score < user_score:
                print("YOU WIN 🥳")
                play()
            elif pc_score == user_score:
                print("Draw 🙃")
                play()

        else:
            user_cards.append(random.choice(cards))
            user_score = sum(user_cards)
            round += 1
