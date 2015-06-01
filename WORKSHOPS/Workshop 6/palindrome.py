def palindromes():
	read = open('words.txt', 'r').readlines()
	words = []
	palindromes = []
	for i in range(len(read)):
		words.append(read[i].strip())
		if (len(words[i]) > 2) and(words[i] == words[i][::-1]):
			palindromes.append(words[i])
	return palindromes

print palindromes()