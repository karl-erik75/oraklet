import random
x = 10
y = 300

def lot():
    ett = random.randint (1,9)
    två = random.randint (1,9)
    tre = random.randint (1,9)
    fyr = random.randint (1,9)
    fem = random.randint (1,9)
    sex = random.randint (1,9)
    prize12 = 0

    loteri = (input("gisa dom 6 sifrona till loteriet! "))
    #------------------------

    if int(loteri[0]) == (ett):
        print ("ja")
        prize12 = prize12 * 5 + 1000

    else:
        print ("no")

    #------------------------

    if int(loteri[1]) == (två):
        print ("ja")
        prize12 = prize12 * 5 + 1000
    else:
        print("no")

    #------------------------

    if int(loteri[2]) == (tre):
        print ("ja")
        prize12 = prize12 * 5 + 1000
    else:
        print("no")

    #------------------------

    if int(loteri[3]) == (fyr):
        print ("ja")
        prize12 = prize12 * 5  + 1000
    else:
        print("no")

    #------------------------

    if int(loteri[4]) == (fem):
        print ("ja")
        prize12 = prize12 * 5 + 1000
    else:
        print("no")

    #------------------------

    if int(loteri[5]) == (sex):
        print ("ja")
        prize12 = prize12 * 5 + 1000
    else:
        print("no")

    #------------------------


    if int(loteri[5]) == (sex) and int(loteri[4]) == (fem) and int(loteri[2]) == (tre) and int(loteri[1]) == (två) and int(loteri[0]) == (ett) and int(loteri[3]) == (fyr):
                        print ("JACPOT!")
                        prize12 = 50000000
    print ("du van", (prize12))
    sköp = input ("vill du sköpa en till? ")
    prize = prize12

    if sköp == "nej":
        bank_func(prize,bank2)

    else:
        bank_func(prize,bank2)
        



    

def gambling(return_prize,bank2):
    prize = 100
    if return_prize != 0:
        prize = return_prize
    # print("\033c", end="")

    
    fråga = input("priset liger på " + str(prize) + " vil du riska alt för att få dubelt? ") 
    


    if fråga == "nej":
        bank_func(prize,bank2)

    else:
        opp = random.randint(1, 10)
        du = random.randint(1, x)
        # print(x)

        if (opp > du):
            print ("du förlorade")
            prize = 100

        elif (opp < du):
            print ("du van!")
            prize = (prize * 2)


        gambling(prize,bank2)


def bank_func(prize,bank2):
    print("\033c", end="")

    bank = 0
    bank2 = (prize + bank + bank2)
    print ("du van", prize)
    print ("du har", bank2)
    igen = input ("vill du riska mera pengar? ")

    if igen == "nej":
        store(bank2)

    else:
        gambling(0,bank2)


def store(bank2):
    global x
    global y
    print("\033c", end="")
    print ("du har", bank2,"kr")
    luck = input("vil du sköpa mera tur för " + str(y) )
    lots = input("eller vil du sköpa en lot?")

    if lots == "nej":
        print ("okej...")
        gambling(0,bank2)

    else:
         lot()





    if luck == "nej":
        print ("okej")
        gambling(0,bank2)



    
    else:
        if bank2 > y:
            x = x + 1
            bank2 = bank2 - y
            y = y + 50
            store(bank2)
            

        elif bank2 < y:
            print ("brokie")
            gambling(0,bank2)

    



bank2 = 0
du = random.randint(1, 10)
gambling(0,bank2)

