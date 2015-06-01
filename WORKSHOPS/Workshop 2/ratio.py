prev = 1
L = [prev]

for n in range(19):
	x = (1 + prev)**0.5
	L.append(x)
	prev = x

print L
print len(L)
