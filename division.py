num1=int(input("Ingrese el dividendo numero: "))
num2=int(input("Ingrese el divisor numero: "))
x=num1//num2
y=num1%num2
print("Dividendo:",num1)
print("Divisor:",num2)
if y==0:
	print("La division es exacta")
else:
	print("La division no es exacta")
print("Coeciete",x)
print("resto",y)