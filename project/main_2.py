def ten(x, *y):
	print(type(y), y)
	print(type(x), x)
	res = x* y
	return res
b = ten(10, 10)
print(b)
