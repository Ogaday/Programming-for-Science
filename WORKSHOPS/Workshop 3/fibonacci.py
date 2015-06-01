def fibonacci(n):
	fibonacci = [0, 1]
	for i in range(n-2):
		nth = fibonacci[i] + fibonacci[i+1]
		fibonacci.append(nth)
	return fibonacci

print fibonacci(20)