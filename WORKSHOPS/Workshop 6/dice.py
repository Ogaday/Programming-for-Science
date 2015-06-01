import random

def roll(n=6):
	return int(random.random()*n)+1

def test_roll(N = 6000):
	count = [0]*7
	for i in range(N):
		x = roll()
		count[x] += 1
	return count

#print test_roll()

def choose(L):
	if len(L) == 0:
		return None
	x = random.random()
	i = int(x*len(L))
	assert 0 <=i<len(L)
	return L[i]

def throw(dice = 1):
	sum = 0
	for n in range(dice):
		sum += roll()
	return sum