import random
import os

os.system('cls')

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/      

---------------------------------------------------------------
"""


def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  score = 0
  for card in cards:
    score += card
  return score
    

def calculate_end(user_score, computer_score):
  if user_score == computer_score:
    return "It's a draw!"
  elif user_score == 21:
    return "Blackjack! You won!"
  elif user_score > 21 and computer_score > 21:
    return "You both went over. It's a draw!"
  elif user_score > 21:
    return "You went over. You lose!"
  elif computer_score > 21:
    return "Opponent went over. You won!"
  elif computer_score == 21:
    return "Blackjack! Computer won!"
  elif user_score > computer_score:
    return "You won!"
  else:
    return "You lose!"

def play_game():
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    while user_score > 19 or computer_score > 19:
      user_cards = []
      computer_cards = []
      for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
      
      

  while not is_game_over:
    print(logo)
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"      Your cards:       {user_cards}\n\n      Current score:    {user_score}\n")
    print(f"\n      Computer cards:   {computer_cards}\n\n      Current score:    {computer_score}\n\n---------------------------------------------------------------\n")

    if user_score > 21 or computer_score > 21 or user_score == 21 or computer_score == 21:
      is_game_over = True
    else:
      user_should_deal = input("      Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
        
        if computer_score < 17:
          computer_cards.append(deal_card())  

        os.system('cls')
      else:
        is_game_over = True
        os.system('cls')

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
  while computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  os.system('cls')
  print(logo)
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  print(f"      Your cards:       {user_cards}\n\n      Current score:    {user_score}\n")
  print(f"\n      Computer cards:   {computer_cards}\n\n      Current score:    {computer_score}\n\n---------------------------------------------------------------\n")
  print((f"      {calculate_end(user_score, computer_score)}"))

# Start:
play_game()
