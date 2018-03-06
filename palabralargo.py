y=input("Introdusca una palabra: ")
x=input("Introdusca una palabra: ")
a=len(y)
b=len(x)
if b<a:
	j=a-b
	print("la palabra",y,"tiene",j,"letras mas que",x)
else:
	l=b-a
	print("la palabra",x,"tiene",l,"letras mas que",y)