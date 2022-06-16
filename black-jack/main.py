import random
import os
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards = cards*4

def giveCard(hand,rep):
    for card in range(rep):
        oneCard=random.choice(cards)
        cards.remove(oneCard)
        hand.append(oneCard)
    return hand

def whoIsWinner(player,dealer):
    player=abs(21-player)
    dealer=abs(21-dealer)
    print(player,dealer)
    if dealer > player:
        print("Player Win!!!🥳")
    else:
        print("Dealer Win!!!😢")

def sumScore(player):
    if 11 in player and sum(player) > 21:
        player.remove(11)
        player.append(1)
    return sum(player)

def main():
    print(art.logo)
    player_hand=[]
    dealer_hand=[]
    for x in range(2):
        giveCard(dealer_hand,1)
        giveCard(player_hand,1)
    print(f"Dealer have: {dealer_hand[0]}")
    print(f"Player have: {player_hand}")
    endGame=False
    while not endGame:
        answer=input("Would you get an extra card?(Yes or no) ").lower()
        if answer=='no':
            endGame=True
            
            player_score=sumScore(player_hand)
            dealer_score=sumScore(dealer_hand)
            print(f"Dealer have: {dealer_hand}")
            print(f"Player have: {player_hand}")
            whoIsWinner(player_score,dealer_score)
        else:
            os.system('cls')
            giveCard(player_hand,1)
            print(art.logo)
            print(f"Dealer have: {dealer_hand[0]}")
            print(f"Player have: {player_hand}")

main()
