#!/usr/bin/env python
# -*- coding: utf-8 -*-

#LAS DEFINICIONES DE MCM,MCD,INV_MULT NO LAS INCLUYO EN EL CÓDIGO, VALE CUALQUIER FUNCION QUE REALICE ESA TAREA



diccionario = "ABCDEFGHIJKLMN3OPQRSTUVWXYZ"
print("Creado por Carlos Andres Iborra Alvarez")
texto = raw_input("Introduzca el texto a descifrar mediante un ataque: ")
claveA = 0
claveB = 0


while claveA<=len(diccionario) and claveB<=len(diccionario):
if claveA<len(diccionario) and claveB<len(diccionario):
print(claveA,claveB)
descifrado = ""
if inv_mult(claveA, len(diccionario)) == 999:
print("claveA no tiene inverso multiplicativo")
claveA = claveA  +1
claveB = 0
enter = raw_input("Pulse enter para continuar")
else:
for letra in texto:
if letra in diccionario:
numero = diccionario.find(letra)
numero = (numero - claveB)*inv_mult(claveA, len(diccionario))
while numero >= len(diccionario):
numero = numero - len(diccionario)
while numero < 0:
numero = numero + len(diccionario)
descifrado = descifrado + diccionario[numero]
claveB = claveB + 1
if claveB > len(diccionario):
claveA = claveA  +1
claveB = 0
enter = raw_input("Pulse enter para continuar")
print("El texto descifrado es ", descifrado)
