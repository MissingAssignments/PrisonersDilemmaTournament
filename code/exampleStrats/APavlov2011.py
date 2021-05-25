# def strategy(history, memory):
# 	# 1:C, 0:D
# 	discovered = False

# 	if not memory:
# 		memory = 0
# 	if history.shape[1] < 6:
# 		if history[1,-1:] == [0]:
# 			return 0, memory+1
# 		return 1, memory+1
# 	if history.shape[1] % 6 == 0:  # history.shape[1] is the turn #
# 		opponent_history = str(history[1,-6:]).strip("[").strip("]").split()
# 		# print(opponent_history)
# 		# print(["1"]*6)
# 		if opponent_history == ["1"]*6:
# 			print("Opponent is always cooperative!")
# 			discovered = True
# 			if history[1,-1:] == [0]:
# 				return 0, memory+1
# 		if opponent_history == ["0"]*6:
# 			print("Opponent is allways defective!")
# 			discovered = True
# 			return 0, memory+1
# 		if opponent_history == ["0", "1", "0", "1", "0", "1"]:
# 			print("Opponent is suspicious tit for tat!")
# 			discovered = True
# 			if history.shape[1] % 6 in [0, 1]:
# 				return 1, memory+1
# 			if history[1,-1:] == [1]:
# 				return 0, memory+1
# 		if opponent_history == ["0", "0", "1", "0", "0", "1"]:
# 			print("Opponent is pavlovd!")
# 			discovered = True
# 			if history.shape[1] % 6 == 0:
# 				return 0, memory+1
# 		if not discovered:
# 			print("Opponent is random!")
# 			return 0, memory+1
# 	return 1, memory+1

def opponent_history(history, n=-6):
	op_hist = str(history[1,n:]).strip("[").strip("]").split()
	for i in range(len(op_hist)): op_hist[i] = int(op_hist[i])
	return op_hist

# def strategy(history, memory):
# 	if not memory:
# 		memory = 0
# 	if history.shape[1] < 6:
# 		# print([0, memory+1] if history[1,-1:] == [0] else [1, memory+1])
# 		return [0, memory+1] if history[1,-1:] == [0] else [1, memory+1]
# 	if history.shape[1] % 6 == 0:
# 		if opponent_history(history,-6) == [1, 1, 1, 1, 1, 1]:
# 			# print([0, memory+1] if history[1,-1:] == [0] else [1, memory+1])
# 			return [0, memory+1] if history[1,-1:] == [0] else [1, memory+1]
# 		if opponent_history(history,-6).count(0) >= 4:
# 			# print([0, memory+1])
# 			return [0, memory+1]
# 		if opponent_history(history,-6).count(0) == 3:
# 			# print([0, memory+1] if opponent_history(history,-2) == [0, 0] else [1, memory+1])
# 			return [0, memory+1] if opponent_history(history,-2) == [0, 0] else [1, memory+1]
# 		# print([0, memory+1])
# 		return [0, memory+1]

# 	# print([0, memory+1])
# 	return [0, memory+1]

def strategy(history, memory):
		"""Actual strategy definition that determines player's action."""
		# TFT for six rounds
		opponent_class = memory
		if history.shape[1] < 6:
			return [0,opponent_class] if history[1,-1:] == [0] else [1,opponent_class]
		if history.shape[1] % 6 == 0:
			# print("Every 6th")
			# Classify opponent
			if opponent_history(history,-6) == [1] * 6:
				opponent_class = "Cooperative"
			if opponent_history(history,-6).count(0) >= 4:
				opponent_class = "ALLD"
			if opponent_history(history,-6).count(0) == 3:
				opponent_class = "STFT"
			if not opponent_class:
				opponent_class = "Random"
		# Play according to classification
		if opponent_class in ["Random", "ALLD"]:
			# print("Random/ALLD")
			return [0,opponent_class]
		if opponent_class == "STFT":
			# TFTT
			# print("STFT")
			return [0,opponent_class] if opponent_history(history,-2) == [0, 0] else [1,opponent_class]
		if opponent_class == "Cooperative":
			# TFT
			# print("Cooperative")
			return [0,opponent_class] if history[1,-1:] == [0] else [1,opponent_class]
		# print("nothing")
		# return 1,opponent_class
