import random
def RandString():
    string = ''
    for i in range(28):
        string += random.choice("abcdefghijklmnopqrstuvwxyz ")
    return string

def Score(generated):
    goal = "methinks it is like a weasel"
    score = 0
    for i in range(28):
        if goal[i] == generated[i]:
            score += 1
    return score/28

def Call():
    generated = RandString()
    closeness = Score(generated)
    tries = 0
    goal = "methinks it is like a weasel"
    while closeness != 1:
        tries += 1
        j = 0
        for i in range(28):
            if generated[i] != goal[i]:
                j = i
        generated = generated[0:j] + random.choice('abcdefghijklmnopqrstuvwxyz ') + generated[j+1:]
        closeness = Score(generated)
        print("Best string generated so far: ", generated)
        print("Accuracy: ", closeness, '\n')
    print("This program took %d iterations to complete!" % tries)
    
Call()
        