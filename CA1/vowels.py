#program which constrcuts a list of all the words in lowercase.txt which contain all the vowels.

lines = open('lowercasewords.txt', 'r').readlines()	#retrieves list of words
words = []
all_vowels = []

for line in lines:
	words.append(line.strip())
	
def has_all_vowels(word):
	"""
	Return boolean value True if word contains all 5 vowels.
	"""
	if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word:
		return True
	else:
		return False


for word in words:
	value = has_all_vowels(word)
	if value == True:
		all_vowels.append(word)

min = len(all_vowels[0])

for vowels in all_vowels:
	if len(vowels) < min:
		min = len(vowels)

shortest_vowels = []

for vowels in all_vowels:
	if len(vowels) == min:
		shortest_vowels.append(vowels)

number = len(all_vowels)
print 'There are ' +str(number) + ' words which contain all 5 vowels'
print 'The list of shortest words with all 5 vowels is:'
print shortest_vowels
