def arithm():
	b = 0
	x = input("Введите последовательность чисел: ")
	x = x.split(" ")
	for i in x:
		b += int(i)
	b /= len(x)
	print(b)
arithm()