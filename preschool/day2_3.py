print("hello")

input_val=input("Guess the number:")

if input_val ==5:
	print("Win!")
else:
	if input_val<5:
		print("Too high")
	else:
		print("Too low")
print("Game over")
