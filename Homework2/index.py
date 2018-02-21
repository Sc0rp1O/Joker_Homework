weight = float(input("Введите свою массу:"))
height = float(input("Введите свой рост:"))
ind = weight / height**2
print("Ваш индекс равен:" , ind) 
if 17.5 > ind > 19.5:
	print("Худая")
elif 19.4 > ind > 23:
	print("Нормально")
elif  22 > ind > 27.4:
	print("Чуть полненькая")
elif  27.3 > ind > 40:
	print("Полная")
elif  20 > ind > 26:
	print("Нормально")
elif  25.9 > ind > 28:
	print("Чуть полненькая")
elif  27.9 > ind > 415:
	print("Полная")