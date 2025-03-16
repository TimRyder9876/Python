# fig04_02.py
"""Simulating the dice game Craps."""
import random

def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple

wins = {}
losses = {}
rolls_totals = {}
x = 100000

for i in range(x):
    die_values = roll_dice()  # first roll
    roll_counter = 1
    # determine game status and point, based on first roll
    sum_of_dice = sum(die_values)

    if sum_of_dice in (7, 11):  # win
        game_status = 'WON'
    elif sum_of_dice in (2, 3, 12):  # lose
        game_status = 'LOST'
    else:  # remember point
        game_status = 'CONTINUE'
        my_point = sum_of_dice

    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        roll_counter += 1
        sum_of_dice = sum(die_values)

        if sum_of_dice == my_point:  # win by making point
            game_status = 'WON'
        elif sum_of_dice == 7:  # lose by rolling 7
            game_status = 'LOST'

    # display "wins" or "loses" message
    if game_status == 'WON':
        if roll_counter in wins:
            wins[roll_counter] += 1
        else:
            wins[roll_counter] = 1

        if roll_counter in rolls_totals:
            rolls_totals[roll_counter] += 1
        else:
            rolls_totals[roll_counter] = 1



    else:
        #print('Player loses', roll_counter)
        if roll_counter in losses:
            losses[roll_counter] += 1
        else:
            losses[roll_counter] = 1
            
        if roll_counter in rolls_totals:
            rolls_totals[roll_counter] += 1
        else:
            rolls_totals[roll_counter] = 1


total_wins= 0
total_losses = 0

for rolls, count in sorted(wins.items()):
    #print(f'Rolls: {rolls}  Wins: {count}')
    total_wins += count

for rolls, count in sorted(losses.items()):
    #print(f'Rolls: {rolls}  Losses: {count}')    
    total_losses += count

print(f'Percentage of wins: {total_wins/x*100:.2f}% ' )
print(f'Percentage of losses: {total_losses/x*100:.2f}% ' )
print('Percentage of wins/losses based on total number of rolls')

print('\n')
print(f'{"% Resolved":>24}{"Cumulative %":>20}')
print(f'{"Rolls"}{"on this roll":>19}{"of games resolved":>20}')
total_count = 0
for roll_number, count in sorted(rolls_totals.items()):
    total_count += count
    print(f'{roll_number:<11}{count/x*100:>12,.2f}%{total_count/x*100:>19,.2f}%')
#print(rolls.items())