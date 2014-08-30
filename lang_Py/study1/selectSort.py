# Example
import random

numRange = 100

numList = []

# Initialize numList as different each number
for i in range(numRange) :

	numRandom = 0
	boolean = True

	while boolean :
		numRandom = random.randrange(1, 1000)

		# if numRandom Exist in numList, Try Again
		boolean = False
		for j in numList :
			if j == numRandom :
				boolean = True

	numList.append(numRandom)



# Print Before Sorting
print "Before Sorting"
print numList



# Sort
for i in range(len(numList)) :
	for j in range(i, len(numList)) :
		if numList[j] < numList[i] :
			temp = numList[j]
			numList[j] = numList[i]
			numList[i] = temp

# Print After Sorting
print
print "After Sorting"
print numList
