import random

class findingMine :
	value = None
	status = None #'open' 'close' 'flag' 'questionmark'

#1.make mines
#2.fill other cells
#3.input from users - open: (mine: game over, 1...n),flag

#mine = -1


#create empty map

mine_map = []
for i in range(10) :
	mine_map.append([])
	for j in range(10) :
		mine_map[i].append(findingMine())


#create mines

mine_list = range(100)
random.shuffle(mine_list)
for i in range(25):
	row = mine_list[i]/10
	column = mine_list[i]%10
	mine_map[row][column].value = str('*')


#print out the map 

mine_map_string = ''
for i in mine_map :
	for j in i :
		mine_map_string += str(j.value) + '         '
	mine_map_string += '\n'

#fill other cells


