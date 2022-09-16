# Determinar si un triangulo es escaleno, isosceles o equilatero.


import math 
s=""

print("----------------------------------------------")
print("---DETERMINAR-ESCALENO-ISOSCELES-EQUILATERO---")
print("----------------------------------------------")


#INPUT
a=int(input("\nDigite el valor del lado a: "))
b=int(input("Digite el valor del lado b: "))
c=int(input("Digite el valor del lado c: "))

#PROCESAMIENTO
if (a + b < c or a + c < b or b + c < a):
    print("\nERROR! esos lados no corresponden a un triangulo")
else:
    if (a == b and b == c):
        s = "El triangulo es EQUILATERO"
    else:
        if (a==b or a==c or b==c):
            s = "EL triangulo es ISOSCELES"
        else: s = "El triangulo es ESCALENO"  

    #RESULTADOS
    print("\n---RESULTADOS---")
    print("\n" + s)
    

