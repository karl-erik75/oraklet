import random



def lot():
    ett = random.randint (1,9)
    två = random.randint (1,9)
    tre = random.randint (1,9)
    fyr = random.randint (1,9)
    fem = random.randint (1,9)
    sex = random.randint (1,9)
    prize = 0
    print (ett)
    print (två)
    print (tre)
    print (fyr)
    print (fem)
    print (sex)

    loteri = (input("gisa dom 6 sifrona till loteriet! "))
    #------------------------

    if int(loteri[0]) == (ett):
        print ("ja")
        prize = prize * 5 + 1000

    else:
        print ("no")

    #------------------------

    if int(loteri[1]) == (två):
        print ("ja")
        prize = prize * 5 + 1000
    else:
        print("no")

    #------------------------

    if int(loteri[2]) == (tre):
        print ("ja")
        prize = prize * 5 + 1000
    else:
        print("no")

    #------------------------

    if int(loteri[3]) == (fyr):
        print ("ja")
        prize = prize * 5  + 1000
    else:
        print("no")

    #------------------------

    if int(loteri[4]) == (fem):
        print ("ja")
        prize = prize * 5 + 1000
    else:
        print("no")

    #------------------------

    if int(loteri[5]) == (sex):
        print ("ja")
        pprize = prize * 5 + 1000
    else:
        print("no")

    #------------------------
    if int(loteri[5]) == (sex) and int(loteri[4]) == (fem) and int(loteri[2]) == (tre) and int(loteri[1]) == (två) and int(loteri[0]) == (ett) and int(loteri[3]) == (fyr):
                        print ("JACPOT!")
                        prize = 50000000

lot()
    print ("du van", prize,"!")

