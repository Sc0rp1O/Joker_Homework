def my_sum():
	b = 0
	x = input()
	x = x.split(" ")
	for i in x:
		b += int(i)
	print(b)
def my_max():
	x = input()
	x = x.split(" ")
	x.sort()
	print(x[len(x)])
def my_len():
	b = 0
	lens = input()
	lens = lens.split(" ")
	for i in lens:
		b += 1
	print(b)	
#my_sum()
#my_max()
#my_len()
