import random

first_num = int(input("Введите первое число:"))
second_num = random.randint(1,10) # генерируем случайное число от 1 до 10

result = int(input("Чему равно " + str(first_num)
+ " умножить на " + str(second_num) + "?\nОтвет:"))

if result == first_num*second_num: # сравнение на равенство
	print("МолодчаГ")
	print("Держи пряник!")
else:
	print("Лошара")
	print("*хлесткий удар кнутом")