#########################################################
#######              PACKAGES                   #########
#########################################################

from math import fabs, sqrt, log, exp # import absolute and square root function from math package
import os # import os Miscellaneous operating system interfaces
import numpy as np # import numpy package
import matplotlib.pyplot as plt # import matplotlib.pyplot package

#########################################################
#######            CLEAR TERMINAL              ##########
#########################################################

os.system('cls' if os.name == 'nt' else 'clear')

#########################################################
#######         INTRODUCE DATA(LISTAS)         ##########
#########################################################

Mx = [] # inicialize the data list of DV
boolone = True # inicialize the boolean used into the while
samplex = 1 # inicialize the number of samples of DV

while boolone : # loop to insert data 
	x = (raw_input('%s x = ' %(samplex))) # introduce a new value

	if str(x) == 'End' or str(x) == 'end' or str(x) == 'Fin' or str(x) == 'fin': # if the new value is 'end', stop the loop
		boolone = False # stop the loop 
	else:
		boolone = True # continue with the loop
		Mx.append(float(x)) # append a new element to the list
		samplex += 1 # plus another sample

My = [] # inicialize the data list of IV
booltwo = True # inicialize the boolean used into the while
sampley = 1 # inicialize the number of samples of IV

while booltwo : # loop to insert data
	y = (raw_input('%s y = ' %(sampley))) # introduce a new value

	if str(y) == 'End' or str(y) == 'end' or str(y) == 'Fin' or str(y) == 'fin': # if the new value is 'end', stop the loop
		booltwo = False # stop the loop 
	else:
		booltwo = True # continue with the loop
		My.append(float(y)) # append a new element to the list
		sampley += 1 # plus another sample

#########################################################
#######            SAVE DATA(LISTS)           ##########
#########################################################

fl = open('Directory of file', 'w') # open and create an .ods file
	for x in xrange(1): # loop to write the file
		fl.write('title 1' + '\t' + 'title 2' + "\n") # write a header
		for i in range(len(Mx)): # loop to write element by element to the file
			fl.write('element1.1' + "\t" + 'element2.1'+ "\n") # write in two colums
fl.close() # close file

#########################################################
#######            PLOT DATA(LISTS)           ##########
#########################################################

# Represent the graphic
fig = plt.figure(1)
plt.plot(Data1, Data2, 'ro') # represent Data1 and Data2
plt.axis([minValueX, maxValueX, minValueY, maxValueY]) # window size
plt.title(Title)
plt.xlabel(Xname)
plt.ylabel(Yname)
fig.savefig('Directory') # Save plot figure
plt.show()
f2 = plt.figure(figsize=(12.0, 20.0))

#########################################################
#######       CONVERT FILE 2 DATA(LISTS)      ##########
#########################################################

fl = open(nameData,'r')
Titles = fl.readline().split('\t')  
nameX = Titles[0]
nameY = Titles[1]
Data = fl.read().split( )
Mx = []
My = []
for i in xrange(len(Data)/2):
	Mx.append(float(Data[i*2]))
	My.append(float(Data[2*(i+1) - 1]))
fl.close()

#########################################################
#######       		MY FIRST SCRIPT		       ##########
#########################################################

nombre = raw_input("¿Cual es tu nombre?")
mision = raw_input("¿cual es tu mision en la vida?")
Color = raw_input("¿Cual es tu color favorito?")

print "Entonces tu nombre es %s, tu mision en la vida es %s y tu color favorito es %s." % (nombre, mision,Color)

fl = open('prueba.ods','w')
for i in range(1000):
    fl.write(nombre+"\t"+mision+"\t"+Color+"\n")
fl.close()

#########################################################
#######       		SOME NOTES   		       ##########
#########################################################

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