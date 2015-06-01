def invert(d):
	"""
	invert the key and items of a dictionary "d" in place. return all values in lists.
	"""
	transmuted = []
	for key in d.keys():
		value = d[key]
		if value in transmuted:
			d[value] += key		
		else:
			d[value] = [key]
			transmuted.append(value)
		del d[key]

dict = {
"a":1,
"b":2,
"c":3
}

print dict
invert(dict)
print dict

multi = {'a' : 21, 'b' : 'a', 'c' : 21, 'd' : 56, 'e': 56}
print multi
invert(multi)
print multi