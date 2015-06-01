a = [3, 4, 5, 6]
b = ['a', 'b', 'c', 'd']

def zipper(a, b):
	zip = []
	if len(a) != len(b):
		return 'error'
	else:
		for i in range(len(a)):
			list = []
			item = [a[i], b[i]]
			list.append(item)
			zip.append(list)
			
		return zip

print zipper(a, b)