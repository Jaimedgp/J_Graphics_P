def costo_del_vuelo(ciudad):

	""" DICCIONARIO"""

    cities = {
        "Córdoba": 821,
        "Iguazú": 941,
        "Ushuaia": 1280,
        "Bariloche": 1848,
    }
    return cities[Cordoba]

def Ordenar_listas(lista):

	lista.sort() #ordena la lista en orden alfabetico si es una lista de Strings
	lista.sort() # ordena la lista de menor a mayor si es una lista de numeros

def Deferenciabilidad():
    from sympy import *
    import numpy as np
    x = Symbol('x')
    y = 2*log(3*x)
    while 1 == 1:
        y = y.diff(x)
        print y
        raw_input('')