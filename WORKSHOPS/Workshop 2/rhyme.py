lines = open('mary.txt', 'r').readlines()
sum=0.0
a = ''
for l in lines:
	a += str(len(l)) +', '
	sum = sum+len(l)

print sum
print a	
avg = sum/len(lines)	
print 'The average word length is', avg