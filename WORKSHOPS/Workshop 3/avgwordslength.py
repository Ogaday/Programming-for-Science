tostrip = open('words.txt', 'r').readlines()
sum=0.0
a = ''
lines=[]
# by doing this I am writing all the lengths as a single string, and then printing them after the iteration.
# Each iteration turns the length (len(l)) into a string, and adds it to a. a += ... is the same as a = a + ...
for i in range(len(tostrip)):
	stripped = tostrip[i].strip()
	lines.append(stripped)
	
for l in lines:
	a += str(len(l)) +', '
	sum = sum+len(l)
	
print 'there are ', len(lines), ' words.'
# print a	
avg = sum/len(lines)	
print 'The average word length is', avg

