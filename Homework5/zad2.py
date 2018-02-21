import random
schet1 = 1000
schet2 = 1000
first = input(""""Приветствую вас в казино Пери 777.У вас 1000 биткоинов.
Только мы заботимся о вас и ваших деньгах поэтому мы не забираем процент от вашей выигранной ставки.
У нас вы можете поиграть в:
1.Black Jack.
2.Казино.
3.Игровые автоматы. """ )
if first == 1:
	print("""Приветствую вас в игре black jack.Правила игры совершенно просты.Каждому игроку раздаются две карты.
У кого сумма карт больше приближены к 21 тот и выиграл.""")

	name = input('Имя первого игрока: ')
	name2 = input('Имя второго игрока: ')
	while True:
		stavka1 = int(input("Первый игрок ставит: "))
		stavka2 = int(input("Второй игрок ставит: "))	
		karta1 = random.randint(1, 11)	
		karta2= random.randint(1, 11)
		print("У первого игрока" , karta1)
		print("У второго игрока" , karta2)
		while:
			print("Хотите взять ещё одну карту")
			vybor = input("Первый игрок:")
			vybor2 = input("Второй игрок:")
			if vybor == "Да":
				karta1 += random.randint(1,11)
			if vybor2 = "Да":
				karta2 += random.randint(1,11)
			if vybor == "Нет" and "Нет":
				break
			else:
				continue
		if karta1 > karta2 and karta1 >= 21:
			print("Первый игрок забирает ставку")
			schet1 = schet1 + stavka2
			schet2 -= stavka2  
		if karta2 > karta1 and karta2 >= 21:
			print("Первый игрок забирает ставку")
			schet2 = schet2 + stavka1
			schet1 -= stavka1
		if karta1 < karta2 and karta2 > 21:
			print(name , "Забирает ставку")
			schet1 = schet1 + stavka2
			schet2 -= stavka2
		if karta2 < karta1 and karta1 > 21:
			print(name , "Забирает ставку")
			schet2 = schet2 + stavka1
			schet1 -= stavka1
		print("")
		prodolzh = input("")
		if prodolzh == "":
			continue
		if prodolzh == "":
			break		
