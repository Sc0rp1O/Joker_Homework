text = input("Введите текст")
text = text.split(" ")
for i in text:
	x = int(text.rfind(i))
	print(i)