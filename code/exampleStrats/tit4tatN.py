import random

def strategy(history, memory):
	if not memory:
		memory = 0
	choice = 1
	if (history.shape[1] >= 1 and history[1,-1] == 0):# or memory > 2: # Choose to defect if and only if the opponent just defected.
		memory += 1
		choice = 0
		# print(history[1,-1] == 0)
	false_count = 0
	for ans in history[1,-1]:
		if not ans:
			false_count += 1
	if false_count > 3:
		choice = 0
		# if (memory+1) % 3 == 0:  # 10 < 9 > 8
		# 	choice = 1
	return choice, memory

'''
SCORE HISTORY
2.578
2.563
2.502
2.571
2.532
2.590
'''