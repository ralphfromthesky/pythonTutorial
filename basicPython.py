# asd

##################################
lives = 3

while lives > 0:
    print('What\'s my name?')
    name = input()
    if name != 'ralph':
        lives -= 1
        print(f'Wrong guess! You have {lives} lives left.')
    else:
        print('You win!')
        break  # Exit the loop since the player has guessed correctly

if lives == 0:
    print('Game over! You have run out of lives.')
