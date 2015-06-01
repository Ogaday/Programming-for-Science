filename = raw_input("Enter Filename:\n==>")


try:
	f = open(filename, 'r')			#Access file
	lines = f.readlines()
	f.close()
	
	maxes = []
	max = max(lines)
	
	for word in lines:
		if len(word) > len(max):
			max = word
	
	for word in lines:
		if len(word) == len(max):
			maxes.append(word.strip())
	
	print maxes
	
			
except:
	print 'Something wrong reading', filename
