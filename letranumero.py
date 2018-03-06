variable=input("ingrese un numero o letra: ")
ascii=ord(variable)
if ascii<=57 and ascii>=48:
	print(variable,"es un numero")
elif ascii<=90 and ascii>=65:
	print(variable,"es una letra mayuscula")
elif ascii<=122 and ascii>=97:
	print(variable,"es una letra minuscula")
else:
	print(variable,"no es letra ni numero")