import art
import os
import random
import time

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards_copy = cards[:]

bets = ["$10", "$20", "$50", "$100"]

user_account = {"10":5, 
                "20":5, 
                "50":5, 
                "100":5}

user_card_list = []
com_card_list = []

user_score = 0
com_score = 0
new_com_score = 0
initial = 0
final = 0
profit = 0
com_outcome = 0
com = []

def welcome():
  print(art.greet)
  time.sleep(3)
  os.system('cls')

def reset_card():
   global cards_copy
   cards_copy = cards.copy()

def com_card():
  global com_score
  global com_card_list
  for n in range(0,2):
    num = random.randint(0, len(cards_copy)-1)
    card = cards_copy[num]
    # card = int(input("Enter com card : "))
    com_score += card
    if card == 11:
       if com_score > 21:
          com_score -= card
          card = 1
          com_score += card
          card = 11
    cards_copy.remove(card)
    com_card_list.append(card)
  return com_card_list

def user_card():
  global user_score
  global user_card_list
  for n in range(0,2):
    num = random.randint(0, len(cards_copy)-1)
    card = cards_copy[num]
    # card = int(input("Enter user card : "))
    user_score += card
    if card == 11:
       if user_score > 21:
          user_score -= card
          card = 1
          user_score += card
          card = 11
    cards_copy.remove(card)
    user_card_list.append(card)
  return user_card_list

def initial_balance():
  global initial
  for key,value in user_account.items():
    initial += int(key) * value
  return initial

def final_balance():
  global final
  for key, value in user_account.items():
    final += int(key) * value
  return final

def profit_balance():
  global profit
  profit = final_balance() - initial
  if final > initial:
      return "profit"
  else:
      return "lose"

def wins(userBet):
  deck = user_account[userBet]
  user_account[userBet] = deck+1
  return user_account

def loses(userBet):
  deck = user_account[userBet]
  user_account[userBet] = deck-1
  # return user_account

def is_deck(userBet):
  if userBet not in user_account:
    return "NO BET AMOUNT FOUND!"
  elif user_account[userBet] > 0:
    return True
  else:
    return False
  
def com_score_checker(userbet):
   if com_score > 21:
      wins(userbet)
      return "wins"
   elif com_score == 21:
      loses(userbet)
      return "lost"
   elif com_score < 16:
      com_second_outcome = comHit(userBet=userbet)
      # score_checker(com_second_outcome, user_bet)
      return com_second_outcome
   else:
      if user_score < 16:
         print("you have to HIT!")
         betting(userbet)
      else:
        compare_result = score_compare(com_score)
        if compare_result=="pass":
            loses(userbet)
            return "lost"
        elif compare_result=="fail":
            wins(userbet)
            return "wins"
        else:
            return "draw"

def score_checker(score,user_bet):
    global com_outcome
    if score > 21:
        loses(user_bet)
        return "lost"
    elif score == 21:
        wins(user_bet)
        return "21"
    elif score < 16:  
        print(f"computer : {com_card_list[0]} = {com_card_list[0]}")
        print(f"User : {user_card_list} = {user_score}")
        betting(user_bet)
    else:
      outcome = com_score_checker(user_bet)
      return outcome
        
def score_compare(comscore):
    final_result = comscore - user_score
    if final_result > 0:
        return "pass"
    elif final_result < 0:
        return "fail"
    else:
        return "draw"

def hit(userBet):
    global user_score
    num = random.randint(0, len(cards_copy)-1)
    card = cards_copy[num]
    # card = int(input("Enter a card : "))
    user_score += card
    if card == 11:
       if user_score > 21:
          user_score -= card
          card = 1
          user_score += card
          card = 11
    cards_copy.remove(card)
    user_card_list.append(card)
    outcome = score_checker(user_score, userBet)
    return outcome

def comHit(userBet):
    global com_score
    num = random.randint(0, len(cards_copy)-1)
    card = cards_copy[num]
    # card = int(input("Enter com card : "))
    com_score += card
    if card == 11:
       if com_score > 21:
          com_score -= card
          card = 1
          com_score += card
          card = 11
    cards_copy.remove(card)
    com_card_list.append(card)
    outcome = com_score_checker( userBet)
    return outcome

def stand(userBet):
    global com_score
    print(f"computer : {com_card_list} = {com_score}")
    print(f"User : {user_card_list} = {user_score}")
    com_score_outcome = com_score_checker(userBet)
    return com_score_outcome


def stop_the_game():
    money = profit_balance()
    if money == "profit":
        print(f"You've earned a profit of : {profit}")
    else:
        print(f"You've lose from the initial amount : {profit}")


def gaming():
    global user_score
    global final
    global com_score
    global new_com_score
    global user_card_list
    global com_card_list
    global initial
    print(f"\nYour Bank Balance : ${initial_balance()}\n")
    print("This is the deck of amount you have.")
    for key, value in user_account.items():
      print(f"{key} : {value}")
    print(f"\n{bets}")
    userBet = input("How much do you bet ?\n")

    if not is_deck(userBet) or isinstance(is_deck(userBet),str):
      print(f"Choose a different bet other than ${userBet}")
      initial = 0
      gaming()
    else:
      print(f"User : ${userBet}\n")
      if len(cards_copy)<len(cards):
         reset_card()
      com = com_card()
      print(f"computer : {com[0]} = {com[0]}")
      print(f"User : {user_card()} = {user_score}")
      if user_score == 21:
          wins(userBet)
          print("BLACKJACK!!")
          choice = input("Do you want to continue ? Type 'yes' or 'no' : ").lower()
          if choice == "yes":
            
            user_card_list = []
            com_card_list = []
            user_score = 0
            com_score = 0
            new_com_score = 0
            initial = 0
            final = 0
            com = []
            gaming()
          else:
            stop_the_game()
      elif user_score > 21:
          loses(userBet)
          print("User Lost!!")
          choice = input("Do you want to continue ? Type 'yes' or 'no' : ").lower()
          if choice == "yes":
            user_card_list = []
            com_card_list = []
            user_score = 0
            com_score = 0
            new_com_score = 0
            initial = 0
            final = 0
            com = []
            gaming()
          else:
            stop_the_game()
      betting(userBet)  


def betting(userBet):
    global com_card_list
    global com_score
    global user_score
    global user_card_list
    choice = input("'Hit' or 'Stand' : ").lower()
    choices = {"hit":hit, "stand":stand}
    choiceFunction = choices[choice]
    # new_card_list = choiceFunction()
    result = choiceFunction(userBet)
    # result = score_checker(user_score,userBet)

    if result == "passed":
        print(f"\ncomputer : {com_card_list} = {com_score}")
        print(f"User : {user_card_list} = {user_score}")
        comHit()
    elif result == "lost":
        print(f"\ncomputer : {com_card_list} = {com_score}")
        print(f"User : {user_card_list} = {user_score}")
        print("User LOST!!!")
    elif result == "21":
        print(f"\ncomputer : {com_card_list} = {com_score}")
        print(f"User : {user_card_list} = {user_score}")
        print("")
        print("BLACKJACK")
    elif result == "draw":
        print(f"\ncomputer : {com_card_list} = {com_score}")
        print(f"User : {user_card_list} = {user_score}")
        print("")
        print("The Game is Drawn!")
    elif result == "wins":
        print(f"\ncomputer : {com_card_list} = {com_score}")
        print(f"User : {user_card_list} = {user_score}")
        print("")
        print("USER WINS!")
        

    choice = input("Do you want to continue ? Type 'yes' or 'no' : ").lower()
    if choice == "yes":
        global initial
        global final
        global com
        global new_com_score
        user_card_list = []
        com_card_list = []
        user_score = 0
        com_score = 0
        new_com_score = 0
        initial = 0
        final = 0
        com = []
        gaming()
    else:
        stop_the_game()


age = int(input("What is your age ?: "))
if age < 18:
    print("Go and Study kid!")
else:
    print(welcome())
    print(art.logo)
    isPlay = input("Type 'Play' to start the game : ").lower()
    if isPlay != "play":
        print("You're disqualified!")
    else:
        gaming()
        print("Good Bye!!")
