def search_n_print(x, info):
	for entry in info:
		if x.lower() in entry.lower():
			print entry
	
numbers = open("phone.txt", "r").readlines()
for i in range(len(numbers)):
	numbers[i] = numbers[i].strip()
while True:
        search_n_print(raw_input("ENTER NAME:\n==> "), numbers)
