#!/usr/bin/env python
# coding: utf-8

# In[2]:


#write a blackjack game
#input 2 user. 1 dealer, 1 player
#start with player, then followed by dealer
#if player have card score below 21, have option to draw another card or can opt to stop. Up to a maximum of 5 cards
#winner must have higher score than the other user, and must be below 21 points. No minimum score
#Aces start with 11 points. 3rd card onwards Aces will automatically convert to 1 points.
#J,Q,K is 10
import time
import random

def game():
    start = input("Welcome to Ivan's Blackjack!. Hit [Enter] to Start Playing:")

    cards = {
        "Aces": 11,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
        "Six": 6,
        "Seven": 7,
        "Eight": 8,
        "Nine": 9,
        "Ten": 10,
        "Jack": 10,
        "Queen": 10,
        "King": 10
        }

    player_hand = []
    dealer_hand = []

    #dealer card. represented with letter d in front
    #might not need this category
    dcard1 = random.choice (list(cards))
    dcard1v = cards.get(dcard1)
    dcard2 = random.choice (list(cards))
    dcard2v = cards.get(dcard2)


    #add card number into dealer_hand
    dealer_hand.append (dcard1v)
    dealer_hand.append (dcard2v)

    #player card
    #cards.get >> .get is used to obtain the values of the key in dictionary.
    #card with v is the integar value that was converted. Previous method of .get and .append to list ends up being a string. Or maybe I was wrong somewhere earlier. Error msg is TypeError: 'int' object is not iterable.
    card1 = random.choice (list(cards))
    card1v = cards.get(card1)
    card2 = random.choice (list(cards))
    card2v = cards.get(card2)


    #add card number into player_hand
    player_hand.append (card1v)
    player_hand.append (card2v)

    #to account double Aces dealing on first hand
    if len(player_hand) == 2 and sum(player_hand) == 22:
        player_hand [0] = 10

    if len(dealer_hand) == 2 and sum(dealer_hand) == 22:
        dealer_hand [0] = 10

    #short list variables
    input_question = ("Would you still like to Play or Pass?")

    print (f"Your first two card is {card1} and {card2}. Total card number is {sum(player_hand)}")

    #p is to control number of cards player can draw
    p = 0

    #player turn
    while p<3:
        if sum(player_hand) == 21:
            print ("Congrats! You have a blackjack!")
            break
        elif sum(player_hand) > 21:
            print ("You've burst!")
            break
        elif sum(player_hand) <21:
            input_ans = input (input_question).lower()
            if input_ans == "pass":
                print (f"Your total card number is {sum(player_hand)}")
                break
            elif input_ans == "play":
                cardvalue = random.choice (list(cards))
                player_hand.append (cards [cardvalue])
                #convert Aces to 1
                if sum(player_hand) > 21:
                    for playeraces in range (len(player_hand)):
                        if player_hand [playeraces] == 11:
                            player_hand [playeraces] = 1
                p+=1
                print (player_hand)
                print (f"Your next card is {cardvalue}. Total card number is {sum(player_hand)}")
                continue
            else:
                print ("Your input is not valid. Please type Play or Pass")
        else:
            print ("You've burst!")
            break

    #insert time delay
    time.sleep(1)
    #draw dealer hand
    print (f"Dealer first two card is {dcard1} and {dcard2}")


    #dealer card count. change Aces from 11 to 1 if more than 2 cards
    dcc = 2


    #r is to control number of cards dealer can draw
    #only limit to 3 as dealer already have 2 cards
    r = 0
    while r<3 and sum(dealer_hand) <18:
      draw_card_value = random.choice (list(cards))
      dealer_hand.append (cards [draw_card_value])
      if sum(dealer_hand) > 21:
          for dealeraces in range (len(dealer_hand)):
              if dealer_hand [dealeraces] == 11:
                  dealer_hand [dealeraces] = 1
      #introduce time delay
      time.sleep(1)
      print (f"Dealer's next card is number is {draw_card_value}")
      r+=1
      dcc+=1
      #if dcc >= 3:
        #cards ["Aces"] = 1
    time.sleep(1)
    print (f"Dealer's total card number is {sum(dealer_hand)}")

    print (dealer_hand)
    time.sleep(1)
    #final calculation comparison of both hands
    if (sum(player_hand) <= 21) and (sum(player_hand) > sum(dealer_hand)):
        print ("Player Win!")
    elif (sum(player_hand) <= 21) and (sum(dealer_hand) > 21):
        print ("Player Win!")
    elif (sum(player_hand) == 21) and (sum(dealer_hand) == 21):
        print ("Player Win!")
    elif (sum(player_hand) < 21) and (sum(player_hand) == sum(dealer_hand)):
        print ("It's a Draw!")
    elif (sum(player_hand) > 21) and (sum(dealer_hand) > 21):
        print ("Dealer also burst! It's a Draw!")
    elif (sum(dealer_hand) <= 21) and (sum(player_hand) <= sum(dealer_hand)):
        print ("Dealer Win!")
    else:
        print ("Dealer Win!")

game()
while True:
    time.sleep(1)
    restart = input ("Restart? Type 'Y' or 'N'").lower()
    if restart == "y":
        game()
    elif restart == "n":
        print ("Thank you for playing. See you again!")
        break
    else:
        print ("Your input is not valid. Please type 'Y' or 'N'")

