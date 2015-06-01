def invert(d):
	"""
	invert the key and items of a dictionary "d" in place. return all values in lists.
	"""
	transmuted = []								#keeps a record of the values changed into keys, so that
	for key in d.keys():						#additional (old) keys with same (old) values are assigned
		value = d[key]							#to the same (new) key
		if  not isinstance(value, list):		
			value = [value]
		for i in range(len(value)):
			v = tuple(value)[i]					#lsits are mutable, and therefore non hashable
			if v in transmuted:					#checks if key has already been made
				d[v] += [key]
			else:								#if not, creates a new key and corresponding value from the
				d[v] = [key]					#inverse
				transmuted.append(value[i])
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

	multi = {'a' : 21, 'b' : 'a', 'c' : 21, 'd' : 56, 'e': 56, 'f' : [26, 27]}
	print "original:", multi
	invert(multi)
	print "inverted:",multi
	invert(multi)
	print "inverted twice:",multi