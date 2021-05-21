def strategy(history, memory):
	if not memory:
		memory = 1
	choice = 1
	if (history.shape[1] >= 1 and history[1,-1] == 0): # Choose to defect if and only if the opponent just defected.
		choice = 0
	if memory == 0:
		choice = 0
		memory = 1
	return choice, memory
