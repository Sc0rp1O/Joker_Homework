first = input("Введи список слов через пробел")
first2 = input("Введи второй список слов через")
first = first.split(" ")
first2 = first2.split(" ")
for i in first:
	if i in first2:
		print(i)