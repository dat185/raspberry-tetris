
from utility.managment_light import ManagmentLight
import time
import random
import json

def findArray(array,value):
    for valueTemp in array:
        if (valueTemp == value):
            return True
    return False

map = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

effect = ManagmentLight()
effect.setMap(map)

isStart = False
isButton_right = False
isButton_left = False
continueLine = True
position = 0
positionLast = 0
saveLight = []

for num in map:
    effect.lightOff(num)

effect.lightOnLineEffect(1,20,1,1,0.05)
timeStartDelay = time.time()

while True:
     button_left = effect.getValueButton(2)
     button_right = effect.getValueButton(3)

     if (button_right == False and isButton_right == False and findArray(saveLight,position+1) == False):
        position += 1
        isButton_right = True
     elif (button_left == False and isButton_left == False and findArray(saveLight,position-1) == False):
        position -= 1
        isButton_left = True

     if (button_right == True and continueLine == True):
        isButton_right = False
     if (button_left == True and continueLine == True):
        isButton_left = False


     timeEndDelay = time.time()
     if ((timeEndDelay - timeStartDelay) >= 1):
        timeStartDelay = time.time()
        continueLine = True
     else:
        continueLine = False

     if (continueLine == True):
         print (json.dumps(saveLight))
         if (isStart == False):
            numRandom = random.randint(1,5)
            if (findArray(saveLight,numRandom) == False):
                position = numRandom
                positionLast = position
                effect.lightOn(position)
                isStart = True
            else:
                for num in map:
                    effect.lightOff(num)
                effect.lightOnLineEffect(1,20,1,2.1,0.1)
                saveLight = []
         else:
            if (findArray(saveLight,position) == False and findArray(saveLight,position+5) == False):
                positionLast = position
                position += 5
            else:
                saveLight.append(position)
                isStart = False

         if ((position + 5) > 20):
            isStart = False
            if (findArray(saveLight,position) == False):
                saveLight.append(position)


     if (positionLast != position):
         effect.lightOff(positionLast)
         effect.lightOn(position)
         positionLast = position
