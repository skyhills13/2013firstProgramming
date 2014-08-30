scores = []
result_f = open ("results2.txt") 
for line in result_f:
	(name, score) = line.split()
	scores.append(float(score))
result_f.close()
scores.sort(reverse=True)

index = 0
for sorted_scores in scores:
	if index < 3:
		print(sorted_scores)
	index = index +1

