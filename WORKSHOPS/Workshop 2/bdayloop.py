birthday = [14, 10, 1066]
sum=0
product=1

for b in birthday:
	print b
	sum=sum + b
	product=product*b
	b = b+1

print 'sum is', sum
print 'product is', product