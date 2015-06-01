import oracle

def guess(T = 10):
	answer = 50.0
	n=1
	while n<T:
		if oracle.oracle(answer):
			answer += 50*.5**n
		else:
			answer -= 50*.5**n
		n+=1
		print answer
	return answer
print guess()
print 'the answer is', oracle.reveal()