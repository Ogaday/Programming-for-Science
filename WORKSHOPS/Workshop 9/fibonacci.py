def fibonacci(n, d):
	d[n] = fibonacci[n]
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)
		
while True:
	x = raw_input("==> ")
	if x == 'q':
		break
	else:
		print fibonacci(int(x))