a = [0.04904772, 1.38633599, 0.94084723, -0.96782833, -0.66058869]
b = [1.07227778, -0.75143678, 0.54550933, 0.20866252, -1.4619395 ]

def dot(u, v):
	sum = 0.0
	if len(u) != len(v):
		return 'error'
	else:
		for i in range(len(a)):
			sum += a[i]*b[i]
		return sum

print dot(a, b)