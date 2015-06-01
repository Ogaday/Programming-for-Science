rhyme = ['Mary', 'had', 'a', 'little', 'lamb', 'whose', 'fleece', 'was', 'white', 'as', 'snow']
numwords = 0
numletters = 0

for i in range(len(rhyme)):
	numwords = i+1
	numletters += len(rhyme[i])

print 'the number of words in the rhyme is ', numwords, ' and the number of letters in the whyme is ', numletters