a=int(input("Introdusca un año: "))
if a>=1582:
	z=a%100
	if z==0:
		b=a%400
		if b==0:
			print(a,"Es bisiesto")
		else:
			print(a,"No es bisiesto")
	else:
		c=a%4
		if c==0:
			print(a,"Es bisiesto")
		else:
			print(a,"No es bisiesto")
elif a<1582:
	d=a%4
	if d==0:
		print(a,"Es bisiesto")
	else:
		print(a,"No es bisiesto")