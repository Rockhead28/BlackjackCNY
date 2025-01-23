#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import copy
import streamlit as st

def create_deck(num_decks):
    base_cards = {
        "A": 11, "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "J": 10, "Q": 10, "K": 10
    }
    return [copy.deepcopy(base_cards) for _ in range(4 * num_decks)]

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
    st.title("Blackjack Probability Calculator")
    st.markdown("Calculate your odds of not bursting on the next card!")
    st.markdown("To play, choose the number of decks. Then input the card that you have draw")
    with st.sidebar:
        num_decks = st.number_input("Number of decks:", min_value=1, value=1)
        deck_played = create_deck(num_decks)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Player Hand")
        player_hand = []
        
        for i in range(5):
            card = st.text_input(f"Enter card {i+1} (A, 2-10, J, Q, K):", key=f"card_{i}")
            if card:
                card = card.upper()
                for deck_dict in deck_played:
                    if card in deck_dict:
                        value = deck_dict.pop(card)
                        
                        # Dynamic Ace handling
                        if value == 11 and sum(player_hand) + 11 > 21:
                            value = 1
                        
                        # Change all Aces to 1 point after second card
                        if len(player_hand) >= 2:
                            for d in deck_played:
                                if "A" in d:
                                    d["A"] = 1
                        
                        player_hand.append(value)
                        break

    with col2:
        st.subheader("Analysis")
        if player_hand:
            st.write(f"Player hand: {player_hand}")
            st.write(f"Total sum of cards: {sum(player_hand)}")

            # Calculate not burst percentage
            percentage = calculate_not_burst_percentage(player_hand, deck_played)
            st.markdown(f"### Probability of Not Bursting on Next Card")
            st.markdown(f"## {percentage:.2f}%", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

