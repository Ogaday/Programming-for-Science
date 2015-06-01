def getDicts():
	names = {}
	numbers = {}	
	directory = open("phone.txt", "r").readlines()
	for i in range(len(directory)):
		directory[i] = directory[i].strip()
		numbers[directory[i][-12:]] = directory[i].lower().split(",")[0]
		names[directory[i].lower().split(",")[0]] = directory[i].replace(" ", "").split(",")[1][:-11]			#might strip and replace the elements of the original list, so it's easier to create the two new dicts.
	return (names, numbers)

def lookupName(x, nam, num):
	x = x.lower()
	if x in nam.keys():
		print nam[x], x.title(), num[x]
	
def lookupNumber(x, nam, num):
	x = x.lower()
	if x in num.keys():
		print nam[x], x.title()


	
names, numbers = getDicts()
#print names	
#print numbers
while True:
	lookupName(raw_input("enter a name"), names, numbers)

	
#for key in names.keys():
#	print key,
#	print names[key],
#	print numbers[key]


#HOOOOOOOWWWW TOOOO DOOOOO THIIIIIIIS D: