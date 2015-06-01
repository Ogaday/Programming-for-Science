def algae(axiom):
	"""
	return the axiom rewritten by the algae rules
	
	keword arguments:
	axiom -- The orignal value to be rewritten
	"""
	if type(axiom) != str:							#defensive code
		return "invalid argument type"
	
	stage_1 = ""									#function works by itereating through the string, applying the rewriting rules, and appending the rewritten strings to a new list, "stage_1", which is finally returned
	
	for x in axiom:									#application of the rewriting rules
		if x == "A":
			stage_1 += "AB"
		elif x == "B":
			stage_1 += "A"
		else:										#necessary?
			stage_1 += x
			
	return stage_1
	
def algae_adv(axiom):
	"""
	prints the axiom and the first 10 rewritings of the algae 
	sequences, according to the rules, and fnds the length of
	the string corresponding to n = 30
	
	keyword arguments:
	axiom -- The original value to be rewritten
	"""
	
	print "The axiom is " + str(axiom)				
	
	next = axiom									#to get the consecutive rewritings, as it loops, it runs the algae function output of the function from the last loop.
	for i in range(1, 31):
		next = algae(next)
		if i<11:
			print "n = " + str(i) + " " + next
	print "The length of the 30th rewritten string is " + str(len(next))
	
if __name__ == "__main__":
	algae_adv("A")