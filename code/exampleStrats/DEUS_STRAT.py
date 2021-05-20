def strategy(history, memory):
	choice = 0  # 1=C, 0=D
	if not memory:
		memory = 0
	if memory % 3 == 0:
		choice = 1
	return choice, memory + 1
