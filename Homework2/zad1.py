f = int(input("Ведите первое число:"))
s = int(input("Ведите второе число:"))
t = int(input("Ведите третье число:"))
if f < s < t:
	print(f , s , t)
elif s < f < t:
	print(s , f , t)
elif t < s < f:	
	print(t , s , f)
elif t < f < s:
	print(t , f , s) 
elif f < t < s:
	print(f , t , s)
elif s < t < f:
	print(s , t , f)		