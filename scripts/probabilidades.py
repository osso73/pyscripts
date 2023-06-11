#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 21:33:59 2021

Comprueba la probabilidad de ganar del siguiente planteamiento: hay 3 puertas,
una tiene premio y las otras no. A un concursante le piden escoger una puerta,
luego el presentador abre otra puerta que está vacía, y le pregunta al 
concursante si quiere cambiar su opción. Dice que sí, ya que tiene el 2/3 
de probabilidad de ganar.

Este programa comprueba la probabilidad jugando un número alto de veces, y
contando los aciertos siguiendo esta estrategia. Se confirma la probabilidad
esperada.


@author: oriol
"""

import random


NUM = 1000000

resultados = list()

# crear puertas: una con premio (1), dos sin premio (0)
puertas = [1, 0,  0]

for n in range(NUM):
    # mezclar las puertas
    random.shuffle(puertas)
    
    # escoger una puerta al azar
    opcion = random.randint(0, 2)
    
    # abrir una que no sea premiada, y que no haya escogido
    abre = random.randint(0, 2)
    while abre == opcion or puertas[abre] == 1:
        abre = random.randint(0, 2)
    
    # cambiar de selección -- a la otra que queda
    if opcion == 0:
        nueva = 2 if abre == 1 else 1
    elif opcion == 1:
        nueva = 0 if abre == 2 else 2
    else:
        nueva = 0 if abre == 1 else 1
    
    # comprobar si acierta o no, añadir resultado a una lista
    resultados.append(puertas[nueva])

# estimar % e imprimir resultado
aciertos = 0
for item in resultados:
    aciertos += item

pct = aciertos / len(resultados)
print(f'Porcentaje acierto: {pct*100:.02f}%.')