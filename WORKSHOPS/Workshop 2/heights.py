heights = [189, 154, 213, 130.2, 168.5]
sum = 0.0
sumsq=0.0
n=0

for h in heights:
	print n, h
	sum = sum+h
	sumsq = sumsq +h*h
	n=n+1

print 'length is', n
print 'sum is', sum
print'sum of squares is', sumsq