beginnings = open('beginning.txt', 'r').readlines()
adjectives = open('adjective.txt', 'r').readlines()
inflates = open('inflate.txt', 'r').readlines()
nouns = open('noun.txt', 'r').readlines()

for i in range(len(beginnings)):
	beginnings[i] = beginnings[i].strip()
for i in range(len(adjectives)):
	adjectives[i] = adjectives[i].strip()
for i in range(len(inflates)):	
	inflates[i] = inflates[i].strip()
for i in range(len(nouns)):	
	nouns[i] = nouns[i].strip()
	
options = []
options.append(beginnings)
options.append(adjectives)
options.append(inflates)
options.append(nouns)

import eureka
if __name__ == "__main__":
	eureka.eureka(options)