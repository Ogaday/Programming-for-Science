def invert(d):
	"""
	invert the key and items of a dictionary "d" in place. return all values in lists.
	"""
	transmuted = []
	for key in d.keys():
		value = d[key]
		if  not isinstance(value, list):
			value = [value]
		for i in range(len(value)):
			v = tuple(value)[i]
			if v in transmuted:
				d[v] += [key]
			else:
				d[v] = [key]
				transmuted.append(value[i])
		del d[key]

		
if __name__ == "__main__":
	dict = {
	"a":1,
	"b":2,
	"c":3
	}

	print dict
	invert(dict)
	print dict

	multi = {'a' : 21, 'b' : 'a', 'c' : 21, 'd' : 56, 'e': 56, 'f' : [26, 27]}
	print multi
	invert(multi)
	print multi
	invert(multi)
	print multi