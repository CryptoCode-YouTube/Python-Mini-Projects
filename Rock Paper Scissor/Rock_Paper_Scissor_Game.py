#!/usr/bin/python3

import random
import sys
import time

#stone = 1
#paper = 2
#scissor = 3 

computer_score = 0
human_score = 0

target_score = 100
#score = 0
print('Rock Paper Scissor     ')
print('\nGame Instructios:')
print('''		Play against the computer and try to win.
		 Win 100 points to beat the computer

		 Press q to Quit''')

while True:

	#Human Side
	human = input('\nYour Choice (r,p,s) ')
	if human == 'r':
		print('Your Choice = Rock')
		human_val = 1
	elif human == 'p':
		print('Your Choice = Paper')
		human_val =2
	elif human == 's':
		print('Your Choice = Scissor')
		human_val = 3
	elif human == 'q' or 'Q':
		print('Quiting the game')
		time.sleep(1)
		sys.exit()
	else:
		print('Only r,p,s No other keys should be pressed!, Try again')
		continue

	#Computer Side
	computer_val = random.randint(1,3)
	if computer_val == 1: 
		print('Computer\'s Choice = Rock')
	elif computer_val == 2: 
		print('Computer\'s Choice = Paper')
	else: 
		print('Computer\'s Choice = Scissor')

	

	#Main Logic
	

	if computer_val == human_val:
		print('It\'s a tie')

	elif computer_val == 1 and human_val == 2:#
		print('You win')
		human_score += 10
		print('Your Score =',human_score)
		print('Computer Score =',computer_score)

	elif computer_val == 1 and human_val == 3:
		print('Computer win')
		computer_score += 10
		print('Your Score =',human_score)
		print('Computer Score =',computer_score)

	elif computer_val == 2 and human_val == 1:
		print('Computer win')
		computer_score += 10
		print('Your Score =',human_score)
		print('Computer Score =',computer_score)

	elif computer_val == 2 and human_val == 3:
		print('You win')
		human_score += 10
		print('Your Score =',human_score)
		print('Computer Score =',computer_score)

	elif computer_val == 3 and human_val == 1:
		print('You win')
		human_score += 10
		print('Your Score =',human_score)
		print('Computer Score =',computer_score)

	elif computer_val == 3 and human_val == 2:
		print('Computer win')
		computer_score += 10
		print('Your Score =',human_score)
		print('Computer Score =',computer_score)

	else:
		pass

	#Score Calculation

	if computer_score == target_score or human_score == target_score:
		break

# Final Evaluation
if human_score == 100:
	print('\nYou beat the computer!')
else:
	print('\nYou Lost, Comuter wins!')
