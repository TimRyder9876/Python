# exercise 5_24 card shuffling and dealing

import random

#initialize cards
card_list = ['Ace','King','Queen','Jack','Ten','Nine','Eight','Seven','Six','Five','Four','Three','Two']
suit_list = ['Spades','Hearts','Diamonds','Clubs']

def initialize_cards(cards, suits):
    combinations = []
    for i in range(len(suits)):
        suit_combinations = []
        #print(suit_list[i])
        for c in range(len(cards)):
            #print(cards[c])
            suit_combinations += [(cards[c],suits[i])]
        combinations += suit_combinations
    return combinations

results = []      
results = initialize_cards(card_list, suit_list)

#shuffle deck
random.shuffle(results)

#loop through each index on the deck
for i in range(len(results)):
    # fetch the combined card and suit into a combined string

    s= results[i][0] + ' of ' + results[i][1]
    
    # print the card with field width of 17 spaces
    print('{:<17}\t'.format(s), end = '')

    #every fourth card do a line break
    if (i + 1) % 4 == 0:
        print()


