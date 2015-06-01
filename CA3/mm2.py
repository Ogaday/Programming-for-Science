def nNumGen(n):
	"""
	return an "n" digit string of numerals
	"""											#actually only works for n <= 12, because len(str(float)) = 14. Could use modulo division to repeat the process and concatenate the strings. for i in range(n%12): rand += str(random())[2:int(n)+2]? Or would have to do int(n)/12 for the last one? yeaahhhh.
	return str(random())[2:int(n)+2]			#for some reason, it works for large numbers, will you try and guess, in which case it returns a 12 digit number	
