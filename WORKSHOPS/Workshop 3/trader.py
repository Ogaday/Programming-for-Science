data = open('trader.txt', 'r').readlines()
returns =[]

for i in range(len(data)):
	returns.append(float(data[i].strip()))

sum = 0.0
bonusdays =[]
bonus = 0.0
positives = []
negatives = []
for i in range(len(returns)):
	sum+=returns[i]
	if sum > 200000:
		bonusdays.append(i)
		bonus += returns[i]
		sum = 0.0
	if returns[i] > 0:
		positives.append(returns[i])
	elif returns[i]< 0:
		negatives.append(returns[i])
ratio = float(len(positives))/float(len(negatives))
print ratio
print bonusdays, bonus

