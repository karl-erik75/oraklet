import random


def gambling(return_prize):
    prize = 100
    if return_prize != 0:
        prize = return_prize
    print ("priset liger på", (prize))


    fråga = input("vil du riska att alt för att få dubelt? ") 


    if fråga == "nej":
        print ("du van", prize)
        bank_func(prize)



    elif fråga == "ja":
        opp = random.randint(1, 10)
        du = random.randint(1, 10)

        if (opp > du):
            print ("you lost")
            prize = 100

        elif (opp < du):
            print ("you win")
            prize = (prize * 2)
            print (prize)

        gambling(prize)


def bank_func(prize):
    
    bank = 0
    bank2 = (prize + bank)

    print ("du har", bank2)
    igen = input ("vill du riska mera pengar? ")

    if igen == "ja":
        gambling(0)

    elif igen == "nej":
        store(bank2)


def store(bank2):

    luck = input ("vil du sköpa mera tur för 300???")   

    if luck == "ja":
        gambling(0)

gambling(0)

