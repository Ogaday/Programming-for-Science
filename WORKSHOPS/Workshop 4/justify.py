def right_justify(s, width):
	print (width - len(s))*' ' + s
	
def list_right(L, width):
	for line in L:
		right_justify(line, width)

if __name__ == "__main__":
	raw_poem = open('owl_and_pussycat.txt', 'r').readlines()

	poem = []

	for line in raw_poem:
		poem.append(line.strip())

	print'0123456789'*7
	list_right(poem, width = 50)
