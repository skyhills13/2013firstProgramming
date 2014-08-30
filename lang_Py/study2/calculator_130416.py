def input_by_user() :
	
	inputFromUser = raw_input("input the expression you want to calculate:")
	#print inputFromUser

	expression_string = ' '

	for i in inputFromUser:
		if not i is ' ':
			expression_string += i

	return expression_string #string
	#print type(expression)

def parsing_expression(expression_string) :




'''
def parsing_expression(expression_string) :
	
	expression_list =[]

	for i in expression_string :
		temp_int = ''
		for j in operator :
			if i is j :
				expression_list +-int(temp_int)
				temp_int = ''
				expression_list += str(i)
		for j in range(10):
			if i is j :
				temp_int += i

	if len(temp_int) > 0 :
		expression_list.append(int(temp_int))

	print expression_list

	 

def infix_to_postfix(expression_list) :

	for i in expression_list :
		if type(i) is int :
			postfix.append(i)
		elif i is ')' :
			while True :
				if operator_stack[-1] is '(' :
					del operator_stack[-1]
					break
				else :
					postfix.append(i)
					del operator_stack[-1]
	else : 	

'''

#def calculate() :



expression_string = input_by_user()
parsing_expression(expression_string)