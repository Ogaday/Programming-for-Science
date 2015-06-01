def annual_returns(daily_returns_file, annual_pay, bonus_threshold, holidays):
	data = open(daily_returns_file, 'r').readlines()
	returns =[]

	for i in range(len(data)):
		returns.append(float(data[i].strip()))

	sum = 0.0
	bonusdays =[]
	bonus = 0.0
	positives = []
	negatives = []
	profit = 0.0
	for i in range(len(returns)):
		sum+=returns[i]
		profit+=returns[i]
		if sum > bonus_threshold:
			bonusdays.append(i)
			bonus += returns[i]
			sum = 0.0
		if returns[i] > 0:
			positives.append(returns[i])
		elif returns[i]< 0:
			negatives.append(returns[i])
		

	ratio = float(len(positives))/float(len(negatives))
	days = 5.0/7.0*(365-holidays)		#he works for 5/7*(365-holidays) days a year
	years = 2000/days
	expenses = years*annual_pay+bonus
	avgannual = (profit - expenses)/years
	analytics = (ratio, bonus, avgannual, bonusdays)
	return analytics

print annual_returns(daily_returns_file = 'trader.txt', annual_pay = 100000.00, bonus_threshold = 200000, holidays = 28)
