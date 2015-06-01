limerick = [
    ['There','was', 'a', 'young', 'lady', 'named', 'Wright'],
    ['Whose', 'speed', 'was', 'much', 'faster', 'than', 'light'],
    ['She', 'left', 'home', 'one', 'day'],
    ['In', 'a', 'relative', 'way'],
    ['And', 'returned', 'on', 'the', 'previous', 'night']
]

words = 0
letters = 0

for line in range(len(limerick)):
	line = limerick[line]
	print line
	words += len(line)
	for word in line:
		letters += len(word)

print 'there are ' + str(words) + ' words in the poem'
print 'there are ' + str(letters) + ' letters in the poem'