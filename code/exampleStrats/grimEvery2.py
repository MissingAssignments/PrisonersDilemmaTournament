def strategy(history, memory):
	wronged = False
	if not memory:
		memory = (False, 0)
	if memory[0] is not None and memory[0]: # Has memory that it was already wronged.
		wronged = True

	else: # Has not been wronged yet, historically.
		if history.shape[1] >= 1 and history[1,-1] == 0: # Just got wronged.
			wronged = True

	if wronged:
		if not memory[1] % 2 == 0: # 3
			return 0, (True, memory[0]+1)
	return 1, (False, memory[0]+1)
