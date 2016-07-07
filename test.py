while True:
    try:
        integer=int(input("Please enter an integer: "))
        print("The integer you enter is {}".format(integer))
        break
    except ValueError:
        print("Please try again")
