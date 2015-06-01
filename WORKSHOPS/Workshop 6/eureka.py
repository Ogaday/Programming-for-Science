import dice
import drums

def eureka(meta):
	for i in range(len(meta)):
		word = dice.choose(meta[i])
		print word,

if __name__ == "__main__":
	print eureka(drums.drums)
	