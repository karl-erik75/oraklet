import random
x = 10
y = 300

def gambling(return_prize,bank2):
    # print("\033c", end="")
    prize = 100
    if return_prize != 0:
        prize = return_prize
    print ("priset liger på", (prize))

    
    fråga = input("vil du riska alt för att få dubelt? ") 
    


    if fråga == "nej":
        print ("du van", prize)
        bank_func(prize,bank2)

    else:
        opp = random.randint(1, 10)
        du = random.randint(1, x)
        print(x)

 


        if (opp > du):
            print ("you lost")
            prize = 100

        elif (opp < du):
            print ("you win")
            prize = (prize * 2)
            print (prize)


        gambling(prize,bank2)


def bank_func(prize,bank2):
    
    bank = 0
    bank2 = (prize + bank + bank2)

    print ("du har", bank2)
    igen = input ("vill du riska mera pengar? ")

    if igen == "ja":
        gambling(0,bank2)

    elif igen == "nej":
        store(bank2)


def store(bank2):
    global x
    global y

    luck = input("vil du sköpa mera tur för " + str(y))
    

    
    if luck == "ja":
        if bank2 > y:
            x = x * 1.3
            bank2 = bank2 - y
            y = y + 50
            gambling(0,bank2)

        elif bank2 < y:
            print ("brokie")
            gambling(0,bank2)

    elif luck == "nej":
            print ("okej")
            gambling(0,bank2)


bank2 = 0
du = random.randint(1, 10)
gambling(0,bank2)

