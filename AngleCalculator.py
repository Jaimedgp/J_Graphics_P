from math import asin, pi

h = [6.4, 14.7, 22.2, 29.9, 37.6, 45.2, 52.6, 60, 69.8, 77.1, 84.4, 91.7]
hA = []
alpha = []
alphag =[]

for i in range(len(h)):
	hA.append(h[i]+1.95)
	alpha.append(asin(hA[i]/100.2))
	alphag.append(alpha[i]*180/(pi))

fl = open('C:\Users\jaime\Desktop\Inercia\sabla.csv', 'w') # open and create an .ods file
for x in xrange(1): # loop to write the file
	fl.write('Altura/cm' + '\t' + 'cateto/cm' + '\t' + 'alpha/rad'+ '\t' + 'alpha/' + "\n") # write a header
	for i in range(len(h)): # loop to write element by element to the file
		fl.write(str(h[i]) + "\t"+ str(hA[i]) + "\t" + str(alpha[i])+ "\t" + str(alphag[i])+ "\n") # write in two colums
fl.close() # close file
