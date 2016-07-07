from random import randint
trials=10000
totalflips=0

for trial in range(0,trials):
    flips=0
    if randint(0,1)==0:
        flips+=1
        if randint(0,1)==1:
            flips+=1
        else:
            flips+=1
            while randint(0,1)==0:
                flips+=1
            flips+=1
    else:
        flips+=1
        if randint(0,1)==0:
            flips+=1
        else:
            flips+=1
            while randint(0,1)==1:
                flips+=1
            flips+=1
                
    totalflips=totalflips+flips
    
        
print("The total flips is {} out of 10000 trials and average is {}".format(totalflips,totalflips/trials))
        
        
