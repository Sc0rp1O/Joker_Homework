list = ["Фильмы" , "Игры" , "И что-то типа того."]
print(list)
print("""Что вы хотите сделать?
1.Добавить что-то в конец.
2.Добавить что-то в любое место.
3.Удалить что-то из списка.
4.Очистить список.
5.Создать копию списка.
6.Вывести список целиком.""")
n = int(input())
if n == 1:
	list.append(input("""Что вы хотите добавить?"""))
	print(list)
if n == 2:
	print("Что вы хотите добавить?")
	list.insert(int(input() , input()))
	print(list)
if n == 3:
	f = input("Что вы хотите удалить?")
	game = list.remove([f])
	print(game)
if n == 4:
	list.clear()
	print(list)
if n == 6:
	print(list)
if n == 5:
	list2 = list[:]
	print(list2)