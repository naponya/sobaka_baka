import random
from colorama import Fore
from colorama import Style
from hangman_art import logo_black_jack
from hangman_art import happy_emoji
from hangman_art import sad_emoji
from hangman_art import cards_imgs
from hangman_art import logo_goodbye

cls = lambda: print('\n'*100)

true_false = [True, False, False]

cards_stable = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

img_player = []
img_computer = []


def take_card(hand, img_list):
    """Take a random card from the deck"""

    hand.append(random.choice(cards))
    cards.remove(hand[-1])
    img_list.append(cards_imgs[cards_stable.index(hand[-1])])


def hand_check(player):
    """Checks if player has too many cards in hand"""
    if calc_score(player) > 21:
        return True


def printing(hand, img_list):
    """Returns a string with all the cards in hand with images"""
    s = ""
    for i in range(len(hand)):
        s += str(hand[i])
        if i == (len(img_list)-1):
            s += img_list[i]
        else:
            s += img_list[i] + ", "
    return s


def add_cards(player, computer):
        """Cheks if ace in player's hand should be 1 or 11.
        Asks if player wants to take another card.
        Check player's hand not to exceed 21 points."""

        if 11 in player and calc_score(player) > 21:
            i = player.index(11)
            player[i] = 1
        
        print(f"\nYour cards: {printing(player, img_player)}; current score: {calc_score(player)}")
        print(f"Computer's first card: {computer[0]}{img_computer[0]}\n")
        
        if hand_check(player):
            return player, False
        
        card_decision = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        while card_decision != 'y' and card_decision != 'n':
            card_decision = input("Inappropriate symbol. Type 'y' to get another card, type 'n' to pass: ")
        
        if card_decision == 'y':
            take_card(player, img_player)            
            return player, True
        else:
            return player, False


def calc_score(hand):
    """Calculates total score in hand"""

    score = 0
    for i in hand:
        score += i
    return score


def win(player, computer):
    """Function to end game if player wins"""

    print(f"\nYour final hand: {printing(player, img_player)}; final score: {Fore.CYAN}{calc_score(player)}{Style.RESET_ALL}")
    print(f"Computer's final hand: {printing(computer, img_computer)}; final score: {Fore.CYAN}{calc_score(computer)}{Style.RESET_ALL}")
    print(f"You win {random.choice(happy_emoji)}")


def lose(player, computer):
    """Function to end game if player loses"""

    print(f"\nYour final hand: {printing(player, img_player)}; final score: {Fore.RED}{calc_score(player)}{Style.RESET_ALL}")
    print(f"Computer's final hand: {printing(computer, img_computer)}; final score: {Fore.RED}{calc_score(computer)}{Style.RESET_ALL}")
    print(f"You lose {random.choice(sad_emoji)}")


def win_black_jack(player, computer):
    """Function to end game if player wins with black jack"""

    print(f"\nYour final hand: {printing(player, img_player)}; final score: {Fore.CYAN}{calc_score(player)}{Style.RESET_ALL}")
    print(f"Computer's final hand: {printing(computer, img_computer)}; final score: {Fore.CYAN}{calc_score(computer)}{Style.RESET_ALL}")
    print("You have a Black Jack! 🤩")


def lose_black_jack(player, computer):
    """Function to end game if player loses to computer with black jack"""

    print(f"\nYour final hand: {printing(player, img_player)}; final score: {Fore.RED}{calc_score(player)}{Style.RESET_ALL}")
    print(f"Computer's final hand: {printing(computer, img_computer)}; final score: {Fore.RED}{calc_score(computer)}{Style.RESET_ALL}")
    print("Your opponent have a Black Jack! 💔")


def draw(player, computer):
    """Function to end game if player and computer have the same score"""

    print(f"\nYour final hand: {printing(player, img_player)}; final score: {calc_score(player)}")
    print(f"Computer's final hand: {printing(computer, img_computer)}; final score: {calc_score(computer)}")
    print("That's a draw! 🤷")


def play():
    """Starts the game"""

    cls()
    print(logo_black_jack)
    player = []
    computer = []

    take_card(player, img_player)
    take_card(player, img_player)

    take_card(computer, img_computer)
    take_card(computer, img_computer)
    
    if calc_score(player) == calc_score(computer) == 21:
        draw(player, computer)
        return
    elif calc_score(player) == 21:
        win_black_jack(player, computer)
        return
    elif calc_score(computer) == 21:
        lose_black_jack(player, computer)
        return

    taking = True
    while taking:
        player, taking = add_cards(player, computer)
    
    i = 2
    if calc_score(player) < 21:
        while i > 0:
            i -= 1
            if calc_score(computer) < 16:
                take_card(computer, img_computer)
            elif 16 <= calc_score(computer) <= 19:
                to_take_card = random.choice(true_false)
                if to_take_card:
                    take_card(computer, img_computer)
            else:
                i -= 2  
            if 11 in computer and calc_score(computer) > 21:
                i = computer.index(11)
                computer[i] = 1
                
    if calc_score(player) > 21:
        lose(player, computer)
    elif calc_score(player) == calc_score(computer) or (calc_score(computer) > 21 and calc_score(player) > 21):
        draw(player, computer)
    elif calc_score(player) == 21:
        win_black_jack(player, computer)
    elif calc_score(computer) == 21:
        lose_black_jack(player, computer)   
    elif calc_score(computer) > 21:
        win(player, computer)
    elif calc_score(player) < calc_score(computer):
        lose(player, computer)
    elif calc_score(player) > calc_score(computer):
        win(player, computer)


# -------------CLEAR SCREEN-------------
cls()

# -------------GAME START-------------
while True:
    decision = input("Do you want to play Black Jack? Type 'y' for yes or 'n' for no: ").lower()
    while decision != 'y' and decision != 'n':
        decision = input("Inappropriate symbol. Type 'y' to start game, type 'n' to exit: ")
    if decision == 'y':
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        play()
    else:
        print(logo_goodbye)
        break
