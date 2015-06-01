from patience import *
from justify import right_justify

def histogram(x, y, width):
	"""
	draw a simple histogram of the numbers in y versus the numbers in x.
	"""
	ratio = float(width)/max(y)
	for n in x:
		if n%2 == 0:
			print x[n],
			if x[n] <10:
				print '',
			print int(ratio*y[n])*'*',
			print '\t',
			print y[n]
		else:
			print x[n], 
			if x[n] <10:
				print '',
			if y[n]<100:
				right = int(ratio*y[n])*'*' +'  ' + '\t' + str(y[n])
			elif y[n]<1000:
				right = int(ratio*y[n])*'*' + ' '+'\t' + str(y[n])
			else:
				right = int(ratio*y[n])*'*' + '\t' + str(y[n])
			right_justify(right, 70)

if __name__ == "__main__":
	histogram(range(53), many_plays(10000), 65)