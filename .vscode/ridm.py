import random
x = 10

def gambling(return_prize,bank2):
    # print("\033c", end="")



    prize = 100
    if return_prize != 0:
        prize = return_prize
    print ("priset liger på", (prize))

    
    fråga = input("vil du riska att alt för att få dubelt? ") 
    


    if fråga == "nej":
        print ("du van", prize)
        bank_func(prize,bank2,bank05)

    else:
        opp = random.randint(1, 10)
        du = random.randint(1, x)
       #print("din tur är", (x))

 


        if (opp > du):
            print ("du  förlora")
            prize = 100

        elif (opp < du):
            print ("du van")
            prize = (prize * 2)
            print (prize)
        

        gambling(prize,bank2)


def bank_func(prize,bank2,bank05):
    
    bank = prize

    bank05 = bank2

    bank2 = (bank05 + bank)

    print ("du har", bank2)
    igen = input ("vill du riska mera pengar? ")

    if igen == "ja":
        gambling(0,bank2)

    elif igen == "nej":
        store(bank2, bank05)


def store(bank2, bank05):
    
    global x
    luck = input ("vil du sköpa mera tur för 300???")   


    if luck == "ja":
        if bank2 > 300:
            x = x * 1,3
            bank2 = bank2 - 300
            gambling(0,bank2)

        elif bank2 < 300:
            print ("brokie")
            gambling(0,bank2)

    elif luck == "nej":
            print ("okej")
            gambling(0,bank2)

bank2 = 0
bank05 = 0
bank2 = 0
du = random.randint(1, 10)
gambling(0,bank2)

