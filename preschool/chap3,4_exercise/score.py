scores = []
result_f = open ("results2.txt") 
best_score = 0
for line in result_f:
	(name, score) = line.split()
	if best_score<float(score):
		best_score=float(score)
result_f.close()
print(best_score)