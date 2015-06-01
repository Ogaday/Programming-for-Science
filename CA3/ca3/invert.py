def invert(d):
	"""
	invert the key and items of a dictionary "d" in place
	"""
	
	for key in d.keys():
		d[d[key]] = key
		del d[key]

if __name__ == "__main__":
	dict = {
	"a":1,
	"b":2,
	"c":3
	}

	print "original:", dict
	invert(dict)
	print "inverted:",dict
	invert(dict)
	print "double invert:",dict