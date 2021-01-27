def prefixToInfix(prefix):
	stack = []
	# read prefix in reverse order
	i = len(prefix) - 1
	while i >= 0:
		if not isOperator(prefix[i]):
			# symbol is operand
			stack.append(prefix[i])
			i -= 1
			print(stack)
		else:
			# symbol is operator
			str = (f"({stack.pop() + prefix[i] + stack.pop()})")
			stack.append(str)
			i -= 1
			print(stack)
	
	return stack[0][1:-1]

def isOperator(c):
	return c in '+-*/^()'


# Driver code
if __name__=="__main__":
	str = input('\nWrite your prefix expression here: ') #"*-A/BC-/AKL"
	print('\nHere is step by step transformation of your expression into infix notation: \n')
	print(f'\n{prefixToInfix(str)}\n')
