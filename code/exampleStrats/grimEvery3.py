# def strategy(history, memory):
# 	choice = 0  # 1=C, 0=D
# 	if not memory:
# 		memory = 0
# 	if memory % 6 == 0:
# 		choice = 1
# 	return choice, memory + 1


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
		if not memory[1] % 3 == 0: # 3
			return 0, (True, memory[1]+1)
	return 1, (False, memory[1]+1)

'''
SCORE HISTORY:
2.414
2.389
2.424
2.404
2.406
2.407
2.408
'''
