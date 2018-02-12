import numpy as np

ti=float(input("Ingrese temperatura inicial del huevo: "))
M=47
p=1.038
c=3.7
K=5.4*10**(-3)
Tw=100
Ty=70
pte1=((M**(2/3))*c*(p**(1/3)))/(K*(np.pi**2)*((4*np.pi/3)**(2/3)))
pte2=np.log(0.76*((ti-Tw)/(Ty-Tw)))
print(pte1*pte2/60)
