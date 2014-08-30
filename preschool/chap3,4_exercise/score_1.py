scores = []
result_f = open ("results2.txt") 
best_score = 0
for line in result_f:
	(name, score) = line.split()
	scores.append(float(score))
result_f.close()
scores.sort(reverse=True)
print(scores[0])
print(scores[1])
print(scores[2])