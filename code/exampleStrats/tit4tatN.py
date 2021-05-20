def strategy(history, memory):
	if not memory:
		memory = 0
	choice = 1
	if (history.shape[1] >= 1 and history[1,-1] == 0) or memory > 2: # Choose to defect if and only if the opponent just defected.
		memory += 1  # marks that the other prisoner has defected last turn
		choice = 0  # Defects to show them a leson!

	return choice, memory
