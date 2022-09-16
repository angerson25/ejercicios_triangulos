# Determinar si un triangulo es obtuso, recto o agudo.


import math 
s=""

print("-------------------------------------")
print("----DETERMINAR-OBTUSO-RECTO-AGUDO----")
print("-------------------------------------")


#INPUT
a=int(input("\nDigite el valor del angulo a: "))
b=int(input("Digite el valor del angulo b: "))
c=int(input("Digite el valor del angulo c: "))

#PROCESAMIENTO
if (a + b + c == 180):
    if (a == 90 or b == 90 or c == 90):
        s = "El triangulo es RECTO"
    if (a<90 and b<90 and c<90):
        s = "EL triangulo es AGUDO"
    else: s = "El triangulo es OBTUSO"  

    #RESULTADOS
    print("\n---RESULTADOS---")
    print("\n" + s)
else:
    print("\nERROR! esos angulos no corresponden a un triangulo")

