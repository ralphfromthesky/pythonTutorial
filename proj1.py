import random as ran

def roll():
    min_value = 1
    max_value = 6
    roll = ran.randint(min_value, max_value)
    
    return roll

value = roll()

while True:
    player = input('pls enter number of players(2 - 4): ')
    if player.isdigit():
        player = int(player)
        if 2 <= player <= 4:
            break
        else:
            print('player must be between 2 - 4')
    else:
        print('invalid, try again')
        
max_score = 50
player_score = [0 for i in range(player)]   
    
while max(player_score) < max_score:
    for playerX in range(player):
        print('player', playerX + 1, 'turn has just started')
        current_score =0
        
        while True:
            should_rolll = input('do you like to roll (y)?: ')
            if should_rolll.lower() != 'y':
                break
                
            value = roll()
            if value == 1:
                print(f'you rolled {value} turn done!')
                current_score = 0
                break
            else: 
                current_score += value
                print('you rolled a: ', value)
            print('your score is: ', current_score)
        
        player_score[playerX] += current_score
        print('your total score is: ', player_score[playerX])
        