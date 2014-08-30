print("play ball")
print("total_s = 0")
print("total_b = 0")
from random import randint
ran1 = randint(0,9)
ran2 = randint(0,9)

input1=13
while input1 != ran1 :
	input1 = input("guess the first number:")
	if input1 == ran1 :
		print("total_s = 1")
		print("total_b = 0")	
	else:
		if input1 == ran2 :
			print("total_s=0")
			print("total_b=1")
		else:
			if input1 !=ran2 :
				print("out")
input2 =13
while input2 !=ran2 :
	input2 = input("guess the second number:")
	if input2 == ran2 :
		print("total_s = 2")
		print("total_b = 0")
		print("gg")
	else:
		if input2 == ran1 : 
			print("total_s =1")
			print("total_b =1")
		else:
			if input2 != ran1 :
				print("out")



