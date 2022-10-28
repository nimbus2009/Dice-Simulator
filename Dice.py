import random
import time as t

diceRoll=input("Press 'Y' to roll a die. Press 'N' to exit.")

while(diceRoll=='Y' or diceRoll=='y'):
    diceNum=random.randint(1,6)

    print('Rolling.....')
    t.sleep(1)

    print(' ')

    if(diceNum==1):

        print("[       ]")
        print("[   0   ]")
        print("[       ]")

        print(' ')
        print('A 1 was rolled!')
    elif(diceNum==2):
        print("[     0 ]")
        print("[       ]")
        print("[ 0     ]")

        print(' ')
        print('A 2 was rolled!')
    elif(diceNum==3):
        print("[ 0     ]")
        print("[   0   ]")
        print("[     0 ]")

        print(' ')
        print('A 3 was rolled!')
    elif(diceNum==4):
        print("[ 0   0 ]")
        print("[       ]")
        print("[ 0   0 ]")

        print(' ')
        print('A 4 was rolled!')
    elif(diceNum==5):
        print("[ 0   0 ]")
        print("[   0   ]")
        print("[ 0   0 ]")

        print(' ')
        print('A 5 was rolled!')
    elif(diceNum==6):
        print("[ 0   0 ]")
        print("[ 0   0 ]")
        print("[ 0   0 ]")

        print(' ')
        print('A 6 was rolled!')

    print(' ')

    diceRoll2=input("Press 'Y' to roll a die. Press 'N' to exit.")
    if(diceRoll2=='Y'or diceRoll2=='y'):
        diceRoll='Y'
    elif(diceRoll2=='N' or diceRoll2=='n'):
        break
