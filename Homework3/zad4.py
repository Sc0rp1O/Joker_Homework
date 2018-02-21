first = input("""Имя первого друга
""")
second = input("""Имя второго друга
""")
third = input("""Имя третьего друга
""")
length1 = int(len(first))
length2 = int(len(second))
length3 = int(len(third))
if length3 > length2 > length1:
	print("Обладатель самого длинного имени:" , str(third))
if length2 > length1 > length3:
	print("Обладатель самого длинного имени:" , str(second))
if length1 > length3 > length2:
	print("Обладатель самого длинного имени:" , str(third))
if length1 > length2 > length3:
	print("Обладатель самого длинного имени:" , str(third))
if length2 > length3 > length1:
	print("Обладатель самого длинного имени:" , str(second))
if length3 > length1 > length2:
	print("Обладатель самого длинного имени:" , str(third))