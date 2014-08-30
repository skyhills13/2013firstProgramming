# Example
numDic = {}

numRange = 20

# loop 2 ~ 20
for i in range(2, numRange + 1) :
	
	for j in range(2, i + 1) :
		if i % j == 0 :
			# If This Number is Not Prime Number
			if j in numDic :
				numDic[j].append(i)
			# If This Number is Prime Number
			else :
				numDic[j] = [i]

			# If You Want Get all Multiple Number of each Prime Number,
			# Delete or Input '#' This Code
			break


# Print Result !
print numDic
