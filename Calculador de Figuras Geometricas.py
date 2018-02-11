correr = True
import numpy as np
while(correr):
    H=input("¿Quieres calcular el area o el perimetro? ")
    if H=="Area" or H=="area":
        Figura=input("¿Que figura quieres calcular? ")
        if Figura=="Triangulo" or Figura=="triangulo":
            Altura=float(input("¿Cual es la altura del triangulo? "))
            Base=float(input("¿Cual es la base del triangulo? "))
            Area=(Altura*Base)/2
            print("El area del triangulo es: ",Area)
        elif Figura=="Cuadrado" or Figura=="cuadrado":
            Lado=float(input("¿Cual es la medida del lado del cuadrado? "))
            Area=Lado*Lado
            print("El area del cuadrado es: ",Area)
        elif Figura=="Rectangulo" or Figura=="rectangulo":
            LadoA=float(input("¿Cual es la medida del ancho del rectangulo? "))
            LadoB=float(input("¿Cual es la medida de la altura del rectangulo? "))
            Area=LadoA*LadoB
            print("El area del rectangulo es = ",Area_rec)
        elif Figura=="Circulo" or Figura=="circulo":
            Diametro=float(input("¿Cual es el diametro de la circunferencia? "))
            Area=(Diametro/2)**2*np.pi
            print("El area de la circunferencia es =",Area)
        elif Figura=="Trapecio" or Figura=="trapecio":
            Base_1=float(input("¿Cual es la primera base del trapecio? "))
            Base_2=float(input("¿Cual es la segunda base del trapecio? "))
            Altura=float(input("¿Cual es la altura del trapecio? "))
            Area=(Base_1+Base_2)/2*Altura
            print("El area del trapecio es ",Area)
        elif Figura=="cerrar" or Figura=="Cerrar":
            correr = False
        else:
            print("Por favor, escriba el nombre de una figura geométrica")
       
    elif H=="Perimetro" or H=="perimetro":
        Figura=input("Que figura quieres calcular?")
        if Figura=="Triangulo" or Figura=="triangulo":
            Base=float(input("¿Cual es la medida de la base? "))
            Lado_1=float(input("¿Cual es la medida de primer lado? "))
            Lado_2=float(input("¿Cual es la medida del lado restante??"))
            Perimetro=Base+Lado_1+Lado_2
            print("El perimetro del triangulo es: ",Perimetro)
        elif Figura=="Cuadrado" or Figura=="cuadrado":
            Lado=float(input("¿Cual es la medida del lado del cuadrado? "))
            Perimetro=Lado*4
            print("El perimetro del cuadrado es: ",Perimetro)
        elif Figura=="Rectangulo" or Figura=="rectangulo":
            LadoA=float(input("¿Cual es la medida del ancho del rectangulo? "))
            LadoB=float(input("¿Cual es la medida de la altura del rectangulo? "))
            Perimetro=LadoA*2+LadoB*2
            print("El perimetro del rectangulo es = ",Perimetro)
        elif Figura=="Circulo" or Figura=="circulo":
            Diametro=float(input("¿Cual es el diametro de la circunferencia? "))
            Perimetro=Diametro*np.pi
            print("El perimetro de la circunferencia es =",Perimetro)
        elif Figura=="Trapecio" or Figura=="Trapecio":
            Base_1=input("¿Cual es la medida de la primera base?")
            Base_2=input("¿Cual es la medida de la segunda base?")
            Lado_1=input("¿Cual es la medida del primer lado?")
            Lado_2=input("¿Cual es la medida del lado restante?")
            Perimetro=Base_1+Base_2+Lado_1+Lado_2
            print("El perimetro del trapecio es ",Perimetro)
        elif Figura=="cerrar" or Figura=="Cerrar":
            correr = False
        else:
            print("Por favor, escriba el nombre de una figura geométrica")
    elif H=="cerrar" or H=="Cerrar":
        correr=False
    else:
        print("Por favor, escriba area o perimetro")
    





    
