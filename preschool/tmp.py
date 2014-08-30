import random

def getRandomValues():
	indexValues = []
	for i in range(0,10):
		indexValues.append(i)
	random.shuffle(indexValues)
	return[indexValues[0], indexValues[1], indexValues[2]]

def Inputfromuser():
	rawInputValues=raw_input("input three numbers:(ex:1,2,3)")
	InputValues=rawInputValues.split(",")
	for each in InputValues:
		

#generate random numbers
ans = getRandomValues()
print ans

#input from users
user = Inputfromuser()

#compare
