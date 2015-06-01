def histogram(x, y, width):
	"""
	draw a simple histogram of the numbers in y versus the numbers in x.
	
	keyword arguments:
	x -- the list of x values for the histogram 
	y -- the list of quanities of each x which forms the y values for the histogram
	width -- the width which the longest bar is set at.
	"""
	if type(x) != list or type(y) != list or type(width) != int or len(x) != len(y) or width < 1:
		print "Error: Invalid arguments"
		return None
	ypc = []														#list of the %age values of y
	for quant in y:
		ypc.append(float(quant)/sum(y)*100)
	ratio = float(width)/max(ypc)									#"ratio" is a multiplier formed by the ratio beween the value "width" and the largest value in "y", so that the number of stars forming the charts is proportional to the y value.
	for i in range(len(x)):											#for each "x", print "x" (aligned if necessary), a number of "*" equal to "y*ratio" (rounded down), and the corresponding value of "y", seperated by a tab
		print x[i],
		if len(str(x[i]))<2:
			print '',
		print int(ratio*ypc[i])*'*', '\t', str(round(ypc[i], 2))+ "%", "(" + str(y[i]) + ")"			#two decimal places is a good enough level of accuracy

if __name__ == "__main__":
	print "Histogram of favourite colours, by perentage:"
	histogram(["Blue  ", "Red   ", "Yellow", "green ", "orange", "purple"], [97, 130, 65, 23, 81, 151], 50)