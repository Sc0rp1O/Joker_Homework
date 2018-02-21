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
#my_sum()
my_max()