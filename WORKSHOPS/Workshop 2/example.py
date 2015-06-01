prev = 11
L = [prev]

for n in range(7):
	x = 3*prev+5
	L.append(x)
	prev = x

print L