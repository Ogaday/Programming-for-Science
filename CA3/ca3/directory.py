from minvert2 import invert

def getDicts():
	names = {}
	numbers = {}	
	directory = open("phone.txt", "r").readlines()
	transmuted = []
	for i in range(len(directory)):
		directory[i] = directory[i].strip()
		surname = directory[i].lower().split(",")[0]
		name = directory[i].replace(" ", "").split(",")[1][:-11]
		number = directory[i][-12:]
		if surname in transmuted:			
			names[surname] += [name]
			numbers[surname] += [number]
		else:
			names[surname] = [name]
			numbers[surname] = [number]
			transmuted += [surname]
	#print transmuted
	return names, numbers



#print nam
#print num

#print num['hunt'], nam['hunt'], 'hunt'

#invert(nam)
#invert(num)

#print nam
#print nam[num['01914 418870'][0]], num['01914 418870']

while True:
	nam, num = getDicts()
	lookup = raw_input("enter a surname or number")
	try:
		int(lookup[:5])
		#print lookup
		invert(num)
		#print num[lookup]
		if lookup in num.keys():						#SORT OUT THIS SECTION!!!!
			if len(num[lookup] = 1:
				print nam[num[lookup]], num[lookup]
			else:
				
		
		#	for i in range(:
		#		print num[lookup][i], nam[num[lookup][i]][i]
	except:
		if lookup in nam.keys():
			for i in range(len(nam[lookup])):
				print nam[lookup][i], lookup, num[lookup][i]

#while True:
#	lookup = raw_input("enter a surname or number")
#	try:
#		int(lookup)
#		invert(num)
#		for a in num[lookup]:
#			print a, nam[a]
#			
#	except:
#		pass
#	elif type(lookup
#print nam["patel"], num["patel"]