import random
prize = 100
loop = True


while (loop) == True:
    print ("priset liger på", (prize))


    fråga = input("vil du riska att alt för att få dubelt? ") 


    if fråga == "nej":
        print ("du van", prize)
        loop = False



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


while (loop) == False:
    bank = 0
    bank2 = (prize + bank)
    print ("du har", bank2)
    igen = input ("vil du riska mera pengar? ")

    if igen == "ja":
        loop = True
