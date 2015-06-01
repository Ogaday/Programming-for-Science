birthday = [14, 10, 1066]
sum = 0.0
product = 1.0
for n in birthday:
	sum += n
	product *= n

print sum, product

for i in range(len(birthday)):
	print i, birthday[i]
