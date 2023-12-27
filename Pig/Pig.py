import random

def roll():
    roll = random.randint(1,6)
    return roll

while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")

    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)] # intializing list with 0

while max(player_scores) < max_score:
    for player_index in range (players):
        print(f'Player {player_index + 1} turn has just started!')
        print(f'\nYour total score is:{player_scores[player_index]}\n')
        current_score = 0
        while True:
            should_roll = input("Would you like to roll(y)?: ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You have rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print(f'You rolled a: {value}')
            print(f'Your score is: {current_score}')

        player_scores[player_index] += current_score
        print(f'Your total score is: {player_scores[player_index]}')

max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print(f'Player number {winning_index+1} is the winner with a score of: {max_score}')