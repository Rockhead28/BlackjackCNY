#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import copy

def create_deck(num_decks):
    base_cards = {
        "A": 11, "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "J": 10, "Q": 10, "K": 10
    }
    deck = [copy.deepcopy(base_cards) for _ in range(4 * num_decks)]
    return deck

def calculate_not_burst_percentage(player_hand, deck_played):
    points_left = 21 - sum(player_hand)
    count_perc = 0
    number_card_left = 0

    for deck_dict in deck_played:
        for card_name, card_value in deck_dict.items():
            if card_value <= points_left:
                count_perc += 1
            number_card_left += 1

    return (count_perc / number_card_left * 100) if number_card_left > 0 else 0

def main():
    st.title("Blackjack Card Analysis")

    # Deck configuration
    num_decks = st.number_input("Number of decks being played:", min_value=1, value=1)
    deck_played = create_deck(num_decks)

    # Player hand input
    player_hand = []
    for i in range(5):
        card = st.text_input(f"Enter card {i+1} (A, 2-10, J, Q, K):", key=f"card_{i}")
        if card:
            card = card.upper()
            for deck_dict in deck_played:
                if card in deck_dict:
                    value = deck_dict.pop(card)
                    player_hand.append(value)
                    break

    # Handle double Aces scenario
    if len(player_hand) == 2 and sum(player_hand) == 22:
        player_hand[0] = 1

    # Display results
    if player_hand:
        st.write(f"Player hand: {player_hand}")
        st.write(f"Total sum of cards: {sum(player_hand)}")

        # Calculate not burst percentage
        percentage = calculate_not_burst_percentage(player_hand, deck_played)
        st.write(f"Percentage of not bursting with next card: {percentage:.2f}%")

if __name__ == "__main__":
    main()

