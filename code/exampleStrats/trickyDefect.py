def strategy(history, memory):
	# 1:C, 0:D
	opponent_history = str(history[1]).strip("[").strip("]").split()
	for i in range(len(opponent_history)): opponent_history[i] = int(opponent_history[i])
	if opponent_history.count(1) > 0 and str(history[1]).strip("[").strip("]").split() == ["0"] * 3:

		print(opponent_history)
	# print(history[1])
		return 1,None
	return 0,False
