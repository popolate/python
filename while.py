contador = 1

while(contador <= 44):
    print("El contador va en el numero: ", contador)
    contador = contador + 1

print("Termino el primer while")

contador = 1

while(True):
    print("El contador va en el numero: ", contador)
    if(contador == 44):
        break
    contador = contador + 1

print("Termino el segundo while")

for i in range(5):
    print("Hola!")

print("Termino el primer for")

for contador in range(1, 45):
    if contador == 10:
        continue 
    print("El contador va en el numero: ", contador)
   

print("Termino el segundo for")












