# -*- coding: UTF-8 -*-
 
import random
 
def getRandomValues():
    indexValues = []
    for i in range(1,10):
        indexValues.append(i)
    random.shuffle(indexValues)
 
    return [indexValues[0], indexValues[1], indexValues[2]]
 
 
def getInputValues():
    inputValues = raw_input(u"3개의 숫자를 입력하세요?(예 2,3,4)")
    intInputValues = []
    for each in inputValues.split(","):
        intInputValues.append(int(each))
    return intInputValues
 
def isSameValue(randomValue, inputValue):
    if (randomValue == inputValue):
        return True
    else:
        return False
 
def isSameIndex(randomIndex, inputIndex):
    if (randomIndex == inputIndex):
        return True
    else:
        return False
 
def evaluate(index, inputValue):
    for m in range(3):
        randomValue = randomValues[m]
        if isSameValue(randomValue, inputValue):
            if isSameIndex(m, index):
                return 2
            else:
                return 1
 
 
randomValues = getRandomValues()
 
 
for i in range(10):
    inputValues = getInputValues()
 
    ball = 0
    strike = 0
    for index in range(3):
        result = evaluate(index, inputValues[index])
        if (result == 1):
            ball += 1
        elif (result == 2):
            strike += 1
 
    print(inputValues)
    print("%d strike, %d ball" %(strike, ball))
    if strike == 3:
        print(u"RandomValues : %d니가 이겼다.")
        break