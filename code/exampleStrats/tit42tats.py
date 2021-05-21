def strategy(history, memory):
    choice = 1
    if history.shape[1] >= 2 and history[1,-1] == 0 and history[1,-2] == 0: # Choose to defect if and only if the opponent just defected.
        choice = 0
    # print(choice)
    return choice, None
