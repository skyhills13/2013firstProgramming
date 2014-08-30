from random import randint
answer=randint(1,9)


guess=3 # number in "guess" part should not be the same number with the number in "answer" part
while guess != answer:
	guess = input ("Guess the number:")

	if guess == answer:
		print("U Win!!")
	else:
		if guess>answer:
			print("Too high")
		else:
			print("Too low")
print("gg")