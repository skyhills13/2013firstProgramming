import random

def results():
	print "strike", strike
	print "ball", ball
	print "num_try", num_try

def getrandom():
	answers =[]
	for i in range(0,10):
		answers.append(i)
		random.shuffle(answers)
	return [answers[0],answers[1],answers[2]]

def userinput():
	inputvalues = raw_input("input three numbers[ex:1,2,3]:")
	input = inputvalues.split(",")
	inputs = []
	for i in input:
		inputs.append(int(i))
	return [inputs[0],inputs[1],inputs[2]]

def compare(strike, ball):
	for i in range(0,3):
		for j in range(0,3):
			if ans[i] == user [j]:
				if i == j:
					strike = strike + 1
				else:
					ball = ball + 1	
	results()	

#Should I return something here?


#while strike < 3:
#	num_try +=1
#	user = userinput()


#start
print ("=========")
print ("play ball")
print ("=========")
strike = 0
ball = 0
num_try = 0

result = results()
print result

#generate random value

ans = getrandom()
print ans


#input from user
user = userinput()
print user

#compare

compare(strike,ball)


#result

