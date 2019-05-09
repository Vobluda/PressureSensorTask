import random as r
import time as t
counter = 0

def sensorInput():
    x = r.randint(0,10)
    if (x >= 7):
        y = r.randint(5,200)
        return(y)
    else:
        z = r.randint(0,4)
        return(z)

while (1==1):
    input = sensorInput()
    if (input >= 5):
        print("Input is equal to: %s and thus it passes" % (input,))
        counter = counter + 1
        print(counter)
        t.sleep(1)
    else:
        print("Input is equal to: %s and thus it fails" % (input,))
        print(counter)
        t.sleep(1)
    
