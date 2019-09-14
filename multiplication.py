print("Welcome to Muliplication World")

a=eval(input('enter no of blocks: '))
b=eval(input('enter no of lines: '))
c=eval(input('enter where to start: '))
for i in range(c, a+1):
	for j in range(c, b+1):
		print(i, '*', j, '=', i*j)
	print()