def strategy(history, memory):
	if not memory:
		memory = 1
	choice = 1
	# print(memory)
	if history.shape[1] >= 1 and history[1,-1] == 0 or memory > 5: # Choose to defect if and only if the opponent just defected.
		choice = 0
		memory += 1
	if memory % 10 == 0:
		choice = 1
		memory += 1

	return choice, memory

#2.737188591895948
#2.73348576038056