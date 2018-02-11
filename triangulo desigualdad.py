estado = ""

while(True):
    lado_1=float(input("Medida del primer lado "))
    lado_2=float(input("Medida del segundo lado "))
    lado_3=float(input("Medida del lado restante "))
    if lado_1+lado_2>lado_3 and lado_2+lado_3>lado_1 and lado_1+lado_3>lado_2:
        print("Las medidas dadas si forman un triangulo")
        if lado_1==lado_2==lado_3:
            print("el triangulo formado es equilatero")
        elif lado_1==lado_2 or lado_2==lado_3 or lado_3==lado_1:
            print("el triangulo formado es isoseles")
        else:
            print("el triangulo formado es triangulo escaleno")
    else:
        print("las medidas de los lados no forman un triangulo")
    estado = input("cerrar?")
    if(estado == "si"):
        break
    else:
        continue























