from math import ceil, floor

#temperatura#
x=float(input())
if -0.5 <= x < 0:
	print('-0')
else:
	decimalka=x - floor(x)
	if decimalka >= 0.5:
		print(ceil(x))
	else:
		print(floor(x))
