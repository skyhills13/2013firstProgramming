'''def makesort(dict,list,num):
	for i in list:
		for j in range(1,num+1):
			if pow(10,j-1) <i and i <pow(10, j) :
				if pow(10, j-1) in dict :
					dict[pow(10,j-1)].append(i)
				else :
					dict[pow(10,j-1)] = [i]
'''

string = "abcdefghi"
spdk = string.split('e',3)[1]
print spdk

spdf = string.rsplit('e',3)[1]
print spdf