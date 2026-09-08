import random
x = 10
y = 300

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
    

    
    if luck == "ja":
        if bank2 > y:
            x = x + 1
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

