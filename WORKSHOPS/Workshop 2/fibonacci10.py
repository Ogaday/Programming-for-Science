#to generate the finacci series, sum the previous two elements.

fib = [0, 1]
u = 0

def fibonacci(x):
	u = fib[x+1] + fib[x]
	return u

for n in range(20):
	u = fibonacci(n)
	fib.append(u)

print fib