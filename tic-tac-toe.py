'''
Next steps: 
1. Figure out how to stop the game when someone won.
2. Figure out how to stop the game if the board is full.
'''

print("Welcome to tic-tac-toe.")

board = [["", "", ""], ["", "", ""], ["", "", ""]]
turn = 1

user_input = input("Type whatever (but not exit please) to start the game: ")

def show():
	print(board[0])
	print(board[1])
	print(board[2])

def move_player_1(u_input, b, t):
	change = u_input.split(".")
	if b[int(change[0]) - 1][int(change[1]) - 1] == "":
		b[int(change[0]) - 1][int(change[1]) - 1] = "X"
		show()
		t += 1
	else:
		print("You can't play that case.")
	return b, t

def move_player_2(u_input, b, t):
	change = u_input.split(".")
	if b[int(change[0]) - 1][int(change[1]) - 1] == "":
		b[int(change[0]) - 1][int(change[1]) - 1] = "O"
		show()
		t += 1
	else:
		print("You can't play that case.")
	return b, t

while "exit" not in user_input:
	if turn % 2 != 0:
		user_input = input("Your turn to play, Player 1: ")
		board, turn = move_player_1(user_input, board, turn)
	else:
		user_input = input("Your turn to play, Player 2: ")
		board, turn = move_player_2(user_input, board, turn)
