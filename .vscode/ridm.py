import random


def gambling(return_prize, du,bank2,x):
    prize = 100
    if return_prize != 0:
        prize = return_prize
    print ("priset liger på", (prize))


    fråga = input("vil du riska att alt för att få dubelt? ") 


    if fråga == "nej":
        print ("du van", prize)
        bank_func(prize,bank2,x)

    elif fråga == "ja":
        opp = random.randint(1, 10)
        du = random.randint(1, x)
        

        if (opp > du):
            print ("you lost")
            prize = 100

        elif (opp < du):
            print ("you win")
            prize = (prize * 2)
            print (prize)


        gambling(prize,du,bank2,x)


def bank_func(prize,bank2,x):
    
    bank = 0
    bank2 = (prize + bank)

    print ("du har", bank2)
    igen = input ("vill du riska mera pengar? ")

    if igen == "ja":
        gambling(0,du,bank2,x)

    elif igen == "nej":
        store(du,bank2,x)


def store(du,bank2,x):

    luck = input ("vil du sköpa mera tur för 300???")   


    if luck == "ja":
        if bank2 > 300:
            x * 1000000000000000
            gambling(0,du,bank2,x)

        elif bank2 < 300:
            print ("brokie")
            gambling(0,du,bank2,x)

    elif luck == "nej":
            print ("okej")
            gambling(0,du,bank2,x)

x = 10
bank2 = 0
du = random.randint(1, 10)
gambling(0, du, bank2,x)

