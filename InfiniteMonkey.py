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
        newstring = ""
        tries += 1
        for i in range(28):
            if generated[i] == goal[i]:
                newstring += generated[i]
            else:
                newstring += random.choice("abcdefghijklmnopqrstuvwxyz ")
        generated = newstring
        closeness = Score(generated)
        print("Best string generated so far: ", generated)
        print("Accuracy: ", closeness, '\n')
    print("This program took %d iterations to complete!" % tries)
    
Call()
        