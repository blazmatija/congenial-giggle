from math import ceil, floor


x=float(input())
x=-1.5
if -0.5 <= x < 0:
	print('-0')
else:
	decimalka=x - floor(x)
	if decimalka >= 0.5:
		print(ceil(x))
	else:
		print(floor(x))