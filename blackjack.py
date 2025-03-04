import random

# ASCII art logo for Blackjack
logo = [r'''   _________    _________
 |A        |  |10       |
 |    ♠    |  |    ♥    |
 |         |  |         |
 |    ♠    |  |    ♥    |
 |        A|  |       10|
  ‾‾‾‾‾‾‾‾‾    ‾‾‾‾‾‾‾‾‾

  B   L   A   C   K   J   A   C   K''']

# Function to deal a random card
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # 11 is Ace, 10s represent face cards
    return random.choice(cards)

# Function to calculate the score of a hand
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:  # Check for Blackjack
        return 0
    if 11 in cards and sum(cards) > 21:  # Convert Ace (11) to 1 if needed
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Function to compare scores and determine the winner
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer wins with a Blackjack!"
    elif user_score == 0:
        return "User wins with a Blackjack!"
    elif user_score > 21:
        return "Computer wins!"
    elif computer_score > 21:
        return "User wins!"
    else:
        return "Computer wins!" if computer_score > user_score else "User wins!"

# Function to handle the game logic
def play_game(is_first_game):
    if is_first_game:
        print(logo[0])  # Print logo only for the first game
    
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Dealing two cards to both user and computer at the start
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User's turn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        # Show user cards and the first card of the computer
        print(f"User cards: {user_cards}, User score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # If user has Blackjack or busts, the game ends
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choose = input("Type 'y' to pick the next card or 'n' to pass: ")
            if choose == 'y':
                user_cards.append(deal_card())  # Draw another card
            else:
                is_game_over = True  # End user's turn

    # Computer's turn (draw until 17 or more)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Show final hands and determine the winner
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Main game loop
first_game = True
while input("Do you want to play the game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    if not first_game:
        print("\n" * 5)  # Reduced blank lines for better readability
    play_game(first_game)
    first_game = False  # Logo will not print in subsequent games
