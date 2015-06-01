import random

def roll():
	return int(random.random()*6)+1
def d6():
	return int(random.random()*6)+1
    
def d6_2():
	d6_2 = 0
	for i in range(2):
		d6_2 += d6()
	return d6_2

def yahtzee():
	results = [0]*5
	for n in range(5):
		results[n] = d6()
	return results

def many_dice(N, die):
	results = [0]*100
	for n in range(N):
		a = die(n)
		results[a] += 1
	return results

if __name__ == "__main__":
	print d6()
	print d6_2()
	#print many_dice(100, d6_2)
	print yahtzee()
