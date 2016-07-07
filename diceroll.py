from random import randint

totalroll=0

for n in range(1,10001):
    roll = randint(1,6)
    totalroll = totalroll + roll
    
print("The average of all roll is: {}".format(totalroll/10000))
