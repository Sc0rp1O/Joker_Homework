def multi(a , b):
	c = a * b
	print("Результат умножения : ", c)
def delit(a , b):
	c = a / b
	print("Результат деления :", c)
def minus(a , b):
	c = a - b
	print("Результат вычитания: ", c)
def slozh(a, b):
	c = a - b
	print("Результат сложения:", c)
while True:
	print("""Что вы хотите сделать 
1.Сложение
2.Вычитание
3.Умножение
4.Деление
5.Выйти из программы
""")
	n = int(input("Ваш выбор:"))
	if n == 1:
		slozh(int(input()) , int(input()))
		continue
	if n == 2:
		minus(int(input()) , int(input()))
		continue	
	if n == 3:
		multi(int(input()) , int(input()))
		continue
	if n == 4:
		delit(int(input()) , int(input()))
		continue
	if n == 5:
		break 
