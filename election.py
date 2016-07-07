from random import random

total_a_win=0
total_b_win=0


for n in range(1,10001):
    a_win=0
    b_win=0
    if random() < .87:
        a_win+=1
    else:
        b_win+=1
    if random() < .65:
        a_win+=1
    else:
        b_win+=1
    if random() < .17:
        a_win+=1
    else:
        b_win+=1

    if a_win > b_win:
        total_a_win+=1
    else:
        total_b_win+=1
        
print("Probability A wins election:", total_a_win / 10000)
print("Probability B wins election:", total_b_win / 10000)
