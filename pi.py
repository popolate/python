N=int(input("Inserte un numero para paroximar pi"))
suma=0
for ciclo in range(N):
    if ciclo%2==1:
        suma-=(1/(2*ciclo+1))
    elif ciclo%2==0:
        suma+=(1/(2*ciclo+1))
    print("El valor de pi aproximado es: ",suma)
print("El resultado es: ",4*suma)











##X=0
##while(X<N):
##    X=X+1
##    print("el numero actual es de ",X)
##
##
##X=0
##for i in range(N):
##    X=X+1
##    print("el numero actual es de ",X)
##    print("i vale: ",i)