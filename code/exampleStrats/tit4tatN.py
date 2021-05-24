def strategy(history, memory):
	if not memory:
		memory = [0, 1]
	turn = memory[1]
	choice = 1
	if (history.shape[1] >= 1 and history[1,-1] == 0) or memory[0] > 2: # Choose to defect if and only if the opponent just defected.
		memory[0] += 1  # marks that the other prisoner has defected last turn
		choice = 0  # Defects to show them a leson!
	# if turn >= 350:
	# 	choice = 0

	return choice, [memory[0], turn+1]

#2.7892078685696844
#2.7872606589508475
