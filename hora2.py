hora_i=int(input("hora actual "))
ctdad=int(input("cantidad de horas "))
hora_f=(hora_i+ctdad)%12
print("en", ctdad, "horas, el reloj marcara las", hora_f)
