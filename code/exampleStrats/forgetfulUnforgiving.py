# import random
# import numpy as np

def strategy(history, memory):

	if not memory:
		# LENGTH_OF_GAME = [int(200-40*np.log(random.random())) for i in range(100)]
		# total_guesses = 0
		# for guess in LENGTH_OF_GAME:
		# 	total_guesses += guess
		# guess = total_guesses / 100
		guess = 240
		memory = [1, 1]
	else:
		guess = memory[2]
	turn = memory[1]
	choice = 1  # 1:C, 0:D
	# print(memory)
	if history.shape[1] >= 1 and history[1,-1] == 0 or memory[0] > 3: # Choose to defect if and only if the opponent just defected.
		choice = 0
		memory[0] += 1

	if turn >= guess+60:
		choice = 0

	if memory[0] % 10 == 0:  # 5
		choice = 1
		memory[0] += 1

	return choice, [memory[0], turn+1, guess]


#2.723252137519957  | 10
#2.7245011305028903 | 20
#2.72745482151492   | 30
#2.728347344155846  | 50
#2.730378083992911  | 300
#2.732313098913462  | N/A

#with guessing
#2.7172946271143745
#2.71539567341284

#without guessing
#2.721954827946978
