def invert(d):
	"""
	invert the key and items of a dictionary "d" in place
	"""
	
	for key in d.keys():
		d[d[key]] = key
		del d[key]

dict = {
"a":1,
"b":2,
"c":3
}

print dict
invert(dict)
print dict
