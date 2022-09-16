# Determinar si tres numeros pueden formar los lados de un triangulo 


import math 


print("-----------------------")
print("----VERIFICAR-LADOS----")
print("-----------------------")



#INPUT
a=int(input("Digite el valor del lado a: "))
b=int(input("Digite el valor del lado b: "))
c=int(input("Digite el valor del lado c: "))

#PROCESAMIENTO
if (a + b < c or a + c < b or b + c < a):
    s = "NO se puede construir un triangulo con esos lados"
else:
    s="SI se puede construir un triangulo con esos lados"

#RESULTADOS
print("----------------")
print("---RESULTADOS---")
print("----------------")
print(s)