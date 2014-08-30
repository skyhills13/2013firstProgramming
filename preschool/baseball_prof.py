#!/usr/bin/python
import random

def genRandom():
	tmp = range(1,10)
#print tmp
	random.shuffle(tmp)
#print tmp
	result = [tmp[0],tmp[1],tmp[2]]
	return result

def fromuser(question):
	ques_r = raw_input(question)
	ques=[]
	for i in range(0,3): # 0, 1, 2
		number =  int(ques_r[i])
		ques.append (number)
	return ques

def check(sol, usr):
	s=0;
	b=0;
	for i in range(0,3):
		for j in range(0,3):
			if sol[i] == usr[j]:
				if i == j:
					s= s+1
				else:
					b= b+1
	return (s,b)


#generate random number
ans =  []
ans = genRandom()
print "sol", ans

b=0
s=0
num_try=0

while s!=3 and num_try < 10:
#input from user
	num_try +=1
	user_ans = []
	user_ans = fromuser("Input the number[ex:123]")
	print "user" , user_ans
	#compare
	(s,b) = check(ans,user_ans)

	#print result
	if(s==0 and b==0):
		print ("OUT")
	elif(s==3):
	 	print ("Home Run")
		print ("succeded by ", num_try, "try")
	else:
		print s, "S", b, "B"
if num_try >= 10:
	print "you lose"
#end

