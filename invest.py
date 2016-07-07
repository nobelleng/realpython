def invest(amount, rate, time):
    print("\nPrincipal amount: {}".format(amount))
    print("Annual rate of return: {}\n".format(rate))   
    for year in range(1, time+1):
        interest=amount*rate      
        amount=amount+interest
        print ("Year {0} : ${1}".format(str(year), str(amount)))


invest (100, .05, 8)
invest (2000, .025, 5)
