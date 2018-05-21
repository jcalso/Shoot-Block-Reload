#First Game, does commands at random
from random import randint
print('This is shoot block reload, the classic childhood game')
print('There are only three commands in this game, "s", "r", and "b"')
print('Each reload allows you to shoot once, you can block enemy shots with b, if one player shoots the other while they reload, the player who shot, wins')
print('To start, type your first command below')
player_reloads = 0
computer_reloads = 0

player_input = input()

if player_input == 'r':
	player_reloads += 1

print('Enemy Reloads')
computer_reloads = computer_reloads+1

computer_input = 0
def end(p, c):
	if p == 's' and c == 2:
		return False
	elif(c == 1 and p == 'r'):
		return False
	else:
		return True


while end(player_input, computer_input):
	
	player_input = input()


	if player_input == 'r':
		player_reloads = player_reloads+1
	if player_input == 's' and player_reloads > 0:
		player_reloads -=1
	elif player_input == 's' and player_reloads == 0:
		player_input == 'r'
		print('Player shot a blank')

	
	if computer_reloads == 0:
		computer_input = randint(2,3)
	else:
		computer_input = randint(1,3)

	if(computer_input == 1):
		print("Enemy Shoots")
		computer_reloads -=1
	elif(computer_input == 2):
		print('Enemy Reloads')
		computer_reloads = computer_reloads+1
	else:
		print('Enemy Blocks')

if (player_input != 's' and computer_input != 2):
	print("Computer Wins!")
else: 
	print("Player Wins!")




