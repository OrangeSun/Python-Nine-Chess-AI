import Nine_Robot

'''
Introduction by OrangeSun:

[List]Board: The Chess Board. Player record as 1, Robot record as 2
[Function]Game: [Click_Button] → [Game_Function] → [Robot_run] → [Return States]
[Function]GameOver: Clear the Chess Board
[Function]Win: Judge Win or Lose, Return a Boolean and a number 0(null) or 1(Player) or 2(Robot)
'''

Board = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def game(player):
	# if invalid event #
	if Board[player-1] != 0:
		return '!!!Error : Invalid Event', -1

	# else, change the board #
	Board[player-1] = 1

	# if win or lose, return #
	wins, win_n = win()
	if wins:
		ed = game_over(win_n)
		return ed, -1

	# Robot run #
	y = Nine_Robot.robot_main(Board)
	if Board[y] != 0:
		print('Robot’s Choice is Error !', y)
	print(y)
	Board[y] = 2
	# if win or lose, return #
	wins, win_n = win()
	if wins:
		ed = game_over(win_n)
		return ed, y+1
	return '--- Continue ---', y+1


# if game over, this function will run #
def game_over(n):
	# Clear the Board
	for i in range(9):
		Board[i] = 0

	# Return States
	if n == 1:
		return '--- You Winner ---'
	elif n == 2:
		return '--- You Loser ---'
	elif n == 0:
		return '--- Bad Game ---'
	else:
		return '!!! judge error !!!'


def win():
	# Win or Lose or Continue
	if (Board[0] == Board[1] == Board[2]) or (Board[0] == Board[3] == Board[6]) or (Board[0] == Board[4] == Board[8]):
		if Board[0] != 0:
			return True, Board[0]

	if (Board[6] == Board[4] == Board[2]) or (Board[6] == Board[7] == Board[8]):
		if Board[6] != 0:
			return True, Board[6]

	if (Board[5] == Board[4] == Board[3]) or (Board[5] == Board[2] == Board[8]):
		if Board[5] != 0:
			return True, Board[5]

	if Board[1] == Board[4] == Board[7]:
		if Board[1] != 0:
			return True, Board[1]

	for i in range(9):
		if Board[i] == 0:
			return False, 0
	return True, 0
