forum = input()
n = int(forum.find("корруп"))
l = int(len(forum)) - n
if n > 0:
	print((forum[0:n]) + str("*" * l ))
else:
	print(forum)	