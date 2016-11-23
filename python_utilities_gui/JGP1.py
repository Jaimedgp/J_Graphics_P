"""
	JDG (Just a Graphics' Printer) 

	This program has been develop by Jaime Diez Gonzalez-Pardo in Python in 
	order to facilitate operations in performing laboratory practice

													Version: Noviembre 2016
"""

#############################################################
#############         PACKAGE'S IMPORT         ##############
#############################################################

from math import fabs, sqrt, log, exp, sin, cos # import absolute and square root function from math library
import os # import os Miscellaneous operating system interfaces
import numpy as np # import numpy libraries
import matplotlib.pyplot as plt # import matplotlib.pyplot libraries
from sympy import * #import sympy library to resolve equations 
from PyQt5.QtWidgets import QMessageBox

#############################################################
###########               CLASSES               #############
#############################################################

class Variable():
	""" This class create the object Variable which contains """
	""" the name of the variable and a list with all the     """
	""" values that it takes.                                """ 
	
	def __init__(self, name, values):
		self.name = name # String with the name of the variable
		self.values = values # 1ist with all the values of the variable

	def get_name(self): # method to return the name of the variable
		return self.name

	def set_name(self, newname):
		self.name = newname

	def get_list_values(self): # method to return the list
		return self.values

	def set_list_values(self, newvalues):
		self.values = newvalues

	def set_values(self, newelement, position):
		self.values[position] = newelement

	def get_values(self, position): # method to return a value of the list
		return self.values[position]

class Open_file_CSV():
	""" This class store a certain number of objects Variable """
	""" with their names and values from a file in a list.    """

	def __init__(self, text):
		self.allData = [] # inicialize the list of Variable's objects
		self.fileName = str(text) # introduce directory name
		fr = open(self.fileName,'r') # open file as read

		titles = fr.readline().split(',') # list with all variables names
		numVar = len(titles) # number of variables
		Data = [[] for x in xrange(numVar)] # list with numVar lists
		row = fr.readline().split(',') # read first row
		while row[0] != '': # loop to read all rows
			for i in xrange(numVar): # loop to read each variable 
				Data[i].append(float(row[i])) # append each element to the list
			row = fr.readline().split(',') # read another row
		for x in xrange(numVar):
			self.allData.append(Variable(titles[x].split()[0], Data[x])) # creat a Variable Object with each variable

	def get_all(self): # return a list with all the objetcs
		return self.allData

class Open_file_TXT():
	""" This class store a certain number of objects Variable """
	""" with their names and values from a file in a list.    """

	def __init__(self, text):
		self.allData = [] # inicialize the list of Variable's objects
		self.fileName = str(text) # introduce directory name
		fr = open(self.fileName,'r') # open file as read

		titles = fr.readline().split('\t') # list with all variables names
		numVar = len(titles) # number of variables
		Data = [[] for x in xrange(numVar)] # list with numVar lists
		row = fr.readline().split('\t') # read first row
		while row[0] != '': # loop to read all rows
			for i in xrange(numVar): # loop to read each variable 
				Data[i].append(float(row[i])) # append each element to the list
			row = fr.readline().split('\t') # read another row
		for x in xrange(numVar):
			self.allData.append(Variable(titles[x].split()[0], Data[x])) # creat a Variable Object with each variable

	def get_all(self): # return a list with all the objetcs
		return self.allData

class Straigth():
	""" This class store a certain number of objects Variable """
	""" This class calculate the regression of the graphic    """
	""" supposing that both variables has a linear relation   """
	"""                       y = mx + b                      """

	def inice(self):
		self.n = len(self.Dependent)
		self.Mxx = []
		for i in xrange(self.n):
			self.Mxx.append(self.Dependent[i]**2)

	def Linslope(self):
		xless = [] # inicialize a list DV-Xmean
		a = [] # inicialize a list 
		xxi = [] # inicialize a list xless*xless
		for i in xrange(self.n): # loop append a new element to lists 
			xless.append(self.Dependent[i] - medianX(self.Dependent))
			a.append(xless[i] * self.Independent[i])
			xxi.append(xless[i]**2)
		return sum(a) / sum(xxi) # return the slope
			
	def Linintercept(self):
		Mxy = [] # inicialize a list for DV*IV
		for i in xrange(self.n): # loop that append an element 
			Mxy.append(self.Dependent[i]*self.Independent[i]) # create the list DV * IV
		return (sum(self.Independent)*sum(self.Mxx)-sum(self.Dependent)*sum(Mxy)) / (self.n*sum(self.Mxx) - (sum(self.Dependent))**2) # return intercept

	def Linerrorslope(self):
		recta = []
		for i in xrange(self.n):
			recta.append((self.Independent[i]-self.Linslope()*self.Dependent[i]-self.Linintercept())**2)
		sigma = sqrt(sum(recta)/(self.n-2)) 
		return (sqrt(self.n)*sigma/sqrt((self.n*sum(self.Mxx))-sum(self.Dependent)**2))

	def Linertercept(self):
		a = self.Linerrorslope() * sqrt(sum(self.Mxx)/self.n)
		return a

	def Linget_Ecuation(self):
		self.inice()
		xes = np.arange(min(self.Dependent),max(self.Dependent), ((max(self.Dependent)-min(self.Dependent))/100)) # create an array to represent the straight graphic on X axis
		yes = self.Linslope()*xes + self.Linintercept() # create a list to represent the straght graphic on Y axis
		main = [xes, yes]
		return main

class Logarithmic():
	""" This class calculate the regression of the graphic    """
	""" supposing that both variables has a logarithmic       """
	""" relation:        y = m * ln(x) + b                    """

	def Loginice(self):
		self.sumX = sum(self.Dependent) 
		self.sumY= sum(self.Independent)
		self.sumLnX = 0
		self.sumLn2X = 0 
		self.sumLnXY = 0
		self.sumY2 = 0
		for i in xrange(len(self.Dependent)):
			self.sumLnX += log(self.Dependent[i])
			self.sumLn2X += log(self.Dependent[i])*log(self.Dependent[i])
			self.sumLnXY += log(self.Dependent[i])*self.Independent[i]
			self.sumY2 += self.Independent[i]**2

	def Logslope(self):
		return (self.sumLnXY- self.sumY*self.sumLnX/len(self.Dependent))/(self.sumLn2X - self.sumLnX*self.sumLnX/len(self.Dependent))

	def Logintercept(self):
		return self.sumY/len(self.Dependent) - self.Logslope()*self.sumLnX/len(self.Dependent)
	
	def Logget_Ecuation(self):
		self.Loginice()
		xes = np.arange(min(self.Dependent),max(self.Dependent), ((max(self.Dependent)-min(self.Dependent))/100)) # create an array to represent the curve graphic on X axis
		yes = [] # inicialize a list to represent the curve graphic on Y axis
		for x in xrange(xes.size):
			yes.append(self.Logslope()*log(xes[x])+self.Logintercept())

		main = [xes, yes]
		return main

class Exponential():
	""" This class calculate the regression of the graphic    """
	""" supposing that both variables has an exponential      """
	""" relation:          y = b * e^(m*x)                    """

	def Expinice(self):
		self.Mxx = []
		self.sumy = 0
		for i in xrange(len(self.Dependent)):
			self.Mxx.append(self.Dependent[i]**2)
			self.sumy += log(self.Independent[i])
		self.medy = self.sumy / len(self.Independent)

	def Expslope(self):
		sumXLn = 0
		for i in xrange(len(self.Independent)):
			sumXLn += self.Dependent[i] * log(self.Independent[i])
		return (sumXLn - (self.medy*sum(self.Dependent))) / (sum(self.Mxx)-medianX(self.Dependent)*sum(self.Dependent))

	def Expintercept(self):
		return exp(self.medy-self.Expslope()*medianX(self.Dependent))

	def Expget_Ecuation(self):
		self.Expinice()
		xes = np.arange(min(self.Dependent),max(self.Dependent), ((max(self.Dependent)-min(self.Dependent))/100))# create an array to represent the curve graphic on X axis
		yes = [] # inicialize a list to represent the curve graphic on Y axis
		for x in xrange(xes.size):
			yes.append(self.Expintercept()*exp(self.Expslope()*xes[x]))

		main = [xes , yes]
		return main

class Operations():
	""" This class allows to make all the mathematicals       """
	""" operartions that Python allows, between data columns  """
	""" It should be indicated which columns by a upper C     """
	""" followed (without space) by the column's number       """

	def __init__(self, formula, allData):
		c = 2.998*(10**8) # set speed of ligth
		G = 6.67408 * (10**(-11)) # set gravitational constant
		h = 6.626 * (10**(-34)) # set Planck constant
		q = 1.6 * (10**(-19)) # set elementary charge
		k = 8.988 * (10**(9)) # set coulomb's constant
		self.new_Data = []
		self.formula = formula
		self.allData = allData
		self.action = self.translateAction()
		try:
			self.new_name = self.allData[int(self.i)].get_name()
		except IndexError:
			self.new_name = str(int(self.i))
		
		try:
			if self.action.index("name(") >= 0:
				numElement = self.action.index("name(")
				self.action = self.action[:numElement-1] + 'self.' + self.action[numElement-1:]
				eval(self.action)
		except ValueError:
			try:
				if self.action.index("delete(") >= 0:
					numElement = self.action.index("delete(")
					self.action = self.action[:numElement-1] + 'self.' + self.action[numElement-1:]
					eval(self.action)
			except ValueError:	
				try:
					for i in range(len(self.allData[0].get_list_values())):
						self.new_Data.append(eval(str(self.action)))
				except (NameError, IndexError, ValueError, IOError):
					error = QMessageBox()
					error.setText('Not able that operation')
					error.setWindowTitle('Not able that operation')
					window = error.exec_()

	def translateAction(self):
		try: # excepcion
			i = self.formula.index('C', 0, len(self.formula)) # indice donde acaba allData

			self.i = int(self.formula[i+1:i+2])

			booltwo = True # se inicializa el booleano para bucle while y la excepcion
			index = 0 # se inicializa el indice a partir del cual se leera
			self.action = self.formula.split('=')[1]
			self.action = self.action.replace('C', 'self.allData[') # se sustituyen todas la C por allData[
			while booltwo:
				try: # excepcion
					index = self.action.index('self.allData[', index, len(self.action))+14 # indice donde acaba allData
					self.action = self.action[:index] + '].get_values(i)' + self.action[index:]
				except ValueError:
					booltwo = False # se para el bucle
			return self.action
		except ValueError:
			error = QMessageBox()
			error.setText("Error 99")
			error.setWindowTitle("Error 99")
			window = error.exec_()

	def name(self, name):
		self.new_name = name
		self.new_Data = self.allData[self.i].get_list_values()

	def delete(self):
		self.new_Data = "Delete Column"

	def Returner(self):
		return self.new_name, self.new_Data, int(self.i)

class Modify_Table():
	""" This class allows modify values of the object Variable """
	""" adding, deleting or changing the values. Also checks   """
	""" always if the length is equal for all values list      """

	def __init__(self):
		function = raw_input('Choose action: ')
		try:
			if function == 'Add Value' or function == 'add value' or function == 'Add value':
				list_values = int(raw_input('Select column: '))
				self.add_value(list_values)
			elif function == 'Delete value' or function == 'Delete Value' or function == 'delete value':
				list_values = int(raw_input('Select column: '))
				self.delete_value(list_values)
			elif function == 'Change value' or function == 'change value' or function == 'Change Value':
				list_values = int(raw_input('Select column: '))
				self.change_value(list_values)
			elif function == 'Add Column' or function == 'add column' or function == 'Add column':
				list_values = int(raw_input('Select column: '))
				self.add_column(list_values)
			elif function == 'Delete Column' or function == 'delete column' or function == 'Delete column':
				list_values = int(raw_input('Select column: '))
				self.delete_column(list_values)
			else:
				print 'That is not an option '
		except (ValueError, NameError) :
			print 'Has been a problem'

	def add_value(self, list_values):
		element = int(raw_input('In which element??')) # select in which element add the new number
		x = (raw_input('x = ')) # new element
		allData[list_values].get_list_values().insert(element, float(x)) # append the new element
	
	def delete_value(self, list_values):
		element = int(raw_input('which element do U want to delete ?? ')) # element to delete started from 1 instead 0
		del allData[list_values].get_list_values()[element] # delete the element 

	def change_value(self, list_values):
		element = int(raw_input('which element do U want to change ?? ')) # element to change started from 1 instead 0
		x = (raw_input('x = ')) # new element
		allData[list_values].get_list_values().insert(element, float(x)) # append the new element
		del allData[list_values].get_list_values()[element] # delete the old element

	def add_column(self, list_values):
		allData.insert(list_values, New_table().get_Variable())

	def delete_column(self, list_values):
		del allData[list_values]

class Errores(object):
	""" This class allows to make all the mathematicals       """
	""" This class calculate the error of a magnitud from an  """
	""" equation which depends on others magnitudes by its    """
	""" partials											  """

	def __init__(self, simbolos, valores, errores, funcion):
		self.variables = simbolos
		self.variables = self.variables.split(' ')
		S = symbols(self.variables)
		self.values = valores
		self.errors = errores
		self.f = funcion
		for n in range(len(S)):
			selement = 'S['+str(n)+']'
			self.f = self.f.replace(self.variables[n], selement)
		self.f = eval(self.f)

	def Errors(self):

		Error_sq = 0
		for i in range(len(self.variables)):
			Error_sq += ((self.f.diff(self.variables[i])*self.errors[i])**2)
		Error_re = 'Error_sq.evalf(subs={self.variables[0]:self.values[0]'
		for x in range(1,len(self.variables)):
			Error_re += ', self.variables['+ str(x) + ']:self.values[' + str(x) + ']'
		Error_re += '})'
		Error_re = eval(Error_re)
		Error = sqrt(Error_re)
		return Error

class Hamilton():

	def __init__(self, m, k, l0, r0, theta0, vr, vtheta, n, dt):

		self.m = m
		self.k = k
		self.l0 = l0
		self.r0 = r0
		self.theta0 = theta0
		self.vr = vr
		self.vtheta = vtheta 
		self.n = n
		self.dt = dt

	def get_file(self):

		path = "./File.csv"
		fw = open(path, 'w')
 
		t = 0.0
		pr0 = self.m*self.vr
		ptheta0 = self.m*self.r0*self.r0*self.vtheta
		h = ptheta0*ptheta0/(2.0*self.m*self.r0*self.r0)+pr0*pr0/(2.0*self.m)+(self.k/2.0)*(self.r0-self.l0)*(self.r0-self.l0)

		fw.write("Tiempo/s,Radio/cm,Angulo/rad,Hamiltoniano"+"\n")

		for i in range(1,self.n):
			derR = pr0/self.m
			derTheta = ptheta0/(self.m*self.r0*self.r0)
			derPr = ptheta0*ptheta0/(self.m*self.r0*self.r0*self.r0)-self.k*(self.r0-self.l0)
			derPtheta = 0.0
			t = t+self.dt
			r = self.r0+self.dt*derR
			theta = self.theta0+self.dt*derTheta
			pr = pr0+self.dt*derPr
			ptheta = ptheta0+self.dt*derPtheta
			h = ptheta*ptheta/(2.0*self.m*r*r)+pr*pr/(2.0*self.m)+(self.k/2.0)*(r-self.l0)*(r-self.l0)
			fw.write('%g' %(t)+","+'%g' %(r)+","+'%g' %(theta)+","+'%g' %(h)+"\n")
			self.r0 = r
			self.theta0 = theta
			pr0 = pr
			ptheta0 = ptheta
		fw.close()
		return path

class Graphics(Straigth, Logarithmic, Exponential):

	def __init__(self, Data, columns):
		self.names = [Data[columns[0]].get_name(), Data[columns[1]].get_name()]
		self.Dependent = Data[columns[0]].get_list_values()
		self.Independent = Data[columns[1]].get_list_values()

	def Names(self):
		return self.names

	def Values(self):
		return self.Dependent, self.Independent

	def IntervalLimits(self):
		intervalY = fabs(self.Independent[1] - self.Independent[0])
		for i in range(2,len(self.Dependent)):
			if intervalY == 0:
				intervalY = fabs(self.Independent[i] - self.Independent[i-1])
		if intervalY == 0:
			intervalY = fabs(self.Independent[0]/10)

		intervalX = fabs(self.Dependent[1] - self.Dependent[0])
		for i in range(2,len(self.Dependent)):
			if intervalX == 0:
				intervalX = fabs(self.Dependent[i] - self.Dependent[i-1])
		if intervalX == 0:
			intervalX = fabs(self.Dependent[0]/10)

		maxy = max(self.Independent) + fabs(intervalY)*0.5 # Max value for y axis 
		miny = min(self.Independent) - fabs(intervalY)*0.5 # Min value for y axis
		maxx = max(self.Dependent) + fabs(intervalX)*0.5 # max value for x axis
		minx = min(self.Dependent) - fabs(intervalX)*0.5 # min value for x axis

		return [minx, maxx], [miny, maxy]

#############################################################
###########              FUNCTIONS              #############
#############################################################

def Convert_to_Column(text):
	path = "./File.csv"
	fw = open(path, 'w')
	fw.write(text)
	fw.close()

	data = Open_file_CSV(path).get_all()
	os.remove(path)
	return data

def saveCSV(Path, allData): # save lists into a .csv archive in /home/jaime/Documentos/Data/ path

	fl = open(Path, 'w') # open and create an .csv file

	length = len(allData[0].get_list_values())

	for i in range(len(allData)-1):
		if len(allData[i].get_list_values()) < len(allData[i+1].get_list_values()):
			length = len(allData[i+1].get_list_values())

	line = '%s' %(allData[0].get_name())
	for x in range(1, len(allData)):
		line += ',' + '%s' %(allData[x].get_name())
	fl.write(line + '\n')
			
	for i in range(length):
		try:
			line = '%g' %(allData[0].get_values(i))
		except IndexError:
			line = ' '
		for x in range(1, len(allData)):
			try:
				line += ',' + '%g' %(allData[x].get_values(i))
			except IndexError:
				line += ',' + ' '
		fl.write(line + '\n')
	fl.close()

def saveText(Path, allData):
	fl = open(Path, 'w') # open and create an .csv file

	length = len(allData[0].get_list_values())

	for i in range(len(allData)-1):
		if len(allData[i].get_list_values()) < len(allData[i+1].get_list_values()):
			length = len(allData[i+1].get_list_values())

	line = '%s' %(allData[0].get_name())
	for x in range(1, len(allData)):
		line += '\t' + '%s' %(allData[x].get_name())
	fl.write(line + '\n')
			
	for i in range(length):
		try:
			line = '%g' %(allData[0].get_values(i))
		except IndexError:
			line = ' '
		for x in range(1, len(allData)):
			try:
				line += '\t' + '%g' %(allData[x].get_values(i))
			except IndexError:
				line += '\t' + ' '
		fl.write(line + '\n')
	fl.close()

def saveLaTex(Path, allData):

	length = len(allData[0].get_list_values())

	for i in range(len(allData)-1):
		if len(allData[i].get_list_values()) < len(allData[i+1].get_list_values()):
			length = len(allData[i+1].get_list_values())

	fl = open(Path+'.tex', 'w') # open and create an .ods file
	for x in xrange(1): # loop to write the file
		fl.write('\\begin{table}[H]'+'\n')
		fl.write('\t'+'\\centering'+'\n')
		line = '\t'+'\\begin{tabular}{ '
		for i in range(len(allData)):
			line += 'c '
		fl.write(line+'}'+'\n')
		fl.write('\t'+'\t'+ ' \\'+ '\\\hline'+'\n')
		fl.write('\t'+'\t'+'\\centering'+'\n')

		line = '\t'+'\t'+'\t'+'%s' %(allData[0].get_name())
		for x in range(1, len(allData)):
			line += ' & ' + '%s' %(allData[x].get_name())
		fl.write(line+' \\'+'\\\hline'+'\n')

		for i in range(length-1):
			try:
				line = '\t'+'\t'+'\t'+'%g' %(allData[0].get_values(i))
			except IndexError:
				line = '\t'+'\t'+'\t'+' '

			for x in range(1, len(allData)):
				try:
					line += ' & ' + '%g' %(allData[x].get_values(i))
				except IndexError:
					line += ' & '+' '					
			fl.write(line+ ' \\'+'\\'+'\n')
			
		try:
			line = '\t'+'\t'+'\t'+'%g' %(allData[0].get_values(length-1))
		except IndexError:
			line = '\t'+'\t'+'\t'+' '

		for x in range(1,len(allData)):
			try:
				line += ' & '+'%g' %(allData[x].get_values(length-1))
			except IndexError:
				line += ' & '+' '
		fl.write(line+' \\'+'\\\hline'+'\n')

		fl.write('\t'+'\\end{tabular}'+'\n')
		fl.write('\t'+'\\caption{\\label{Tab:}}'+'\n')
		fl.write('\\end{table}'+'\n')
	fl.close() # close file

def medianX(column): # return the mean of DV
	thisData = column
	med = sum(thisData) / len(thisData) # return the DV mean
	return med