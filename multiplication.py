print("Welcome to a Flexible Multiplication Table")

a=eval(input('Enter No of Blocks for Your Desired Multiplication: '))
b=eval(input('Enter No of Lines for Your Desired Multiplication: '))
c=eval(input('Enter Where You want Your Desired Multiplication to Start: '))
for i in range(c, a+1):
	for j in range(c, b+1):
		print(i, '*', j, '=', i*j)
	print()