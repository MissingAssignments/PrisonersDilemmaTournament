def strategy(history, memory):
	if not memory:
		memory = 0
	choice = 1
	if (history.shape[1] >= 1 and history[1,-1] == 0): # Choose to defect if and only if the opponent just defected.
		choice = 0
	if memory % 25 == 0:  # 10 < 9 > 8
		choice = 1
	return choice, memory + 1

'''
SCORE HISTORY
2.578
2.563
2.502
2.571
2.532
2.590
'''