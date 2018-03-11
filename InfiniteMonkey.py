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
    best = 0
    tries = 0
    while closeness != 1:
        generated = RandString()
        closeness = Score(generated)
        tries += 1
        if closeness > best:
            best = closeness
            beststring = generated
        if tries % 100000 == 0:
            print("Best string generated so far every 100000 tries: ", beststring)
            print("Accuracy: ", best)
    return generated    
    
print(Call())
        