"""
	JDG (Just a Graphics' Printer) 

	This program has been develop by Jaime Diez Gonzalez-Pardo in Python in 
	order to facilitate operations in performing laboratory practice

													Version: Julio 2016
"""

#############################################################
#############         PACKAGE'S IMPORT         ##############
#############################################################

from math import fabs, sqrt, log, exp, sin, cos # import absolute and square root function from math package
import os # import os Miscellaneous operating system interfaces
import numpy as np # import numpy package
import matplotlib.pyplot as plt # import matplotlib.pyplot package

os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal window

#############################################################
###########               CLASSES               #############
#############################################################

class Variable:
	""" This class create the object Variable which contains """
	""" the name of the variable and a list with all the     """
	""" values that it takes.                                """ 
	
	def __init__(self, name, values):
		self.name = name # String with the name of the variable
		self.values = values # 1ist with all the values of the variable

	def get_name(self): # method to return the name of the variable
		return self.name

	def get_list_values(self): # method to return the list
		return self.values

	def get_values(self, position): # method to return a value of the list
		return self.values[position]

class New_table:
	""" This class store a certain number of objects Variable """
	""" with their names and values introduced by screen in a """
	""" list.                                                 """

	def __init__(self):
		self.name = str(raw_input('\n' + 'Column name: ')) # name of the column

		self.values = [] # inicialize the values list
		boolone = True # inicialize the boolean used into the while
		row = 1 # inicialize the row column
		x = (raw_input('%s x = ' %(row))) # introduce the first value

		while boolone : # loop to insert data 
			
			try: # handling exception
				if str(x) == 'End' or str(x) == 'end' or str(x) == 'Fin' or str(x) == 'fin': # if the new value is 'end', stop the loop
					boolone = False # stop the loop 
				else:
					boolone = True # continue with the loop
					self.values.append(float(x)) # append a new element to the lists
					row += 1 # plus another row
					x = (raw_input('%s x = ' %(row))) # introduce a new value
			except ValueError: # the element is not a float
				print 'Sorry, the value is not a float'
				x = (raw_input('%s x = ' %(row))) # introduce a new value
			

	def get_Variable(self): # return the Variable object
		return Variable(self.name, self.values)

class Open_file:
	""" This class store a certain number of objects Variable """
	""" with their names and values from a file in a list.    """

	def __init__(self):
		self.allData = [] # inicialize the list of Variable's objects
		self.fileName = str(raw_input('File directory: ')) # introduce directory name
		directory = True # inicialize the boolean used into the handling exceptions
		while directory:
			try: # handling exception
				fr = open(self.fileName,'r') # open file as read
				directory = False # break the exception
			except IOError:
				print 'Sorry that directory does not exist or no able to treated as file' # if it is not, print an error message
				self.fileName = raw_input('File directory: ') # introduce directory name

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

class Graphic:
	""" This class represent and save a graph with all values """
	""" of the two variables choosed                          """

	def graph(self): # represent and save the graph
		function = self.get_Ecuation()
		Xes = function[0]
		Yes = function[1]

		i = 1
		intervalY = self.Y[i]-self.Y[i-1]
		while intervalY == 0:
			i += 1
			intervalY = self.Y[i]-self.Y[i-1]
		i = 1
		intervalX = self.X[i]-self.X[i-1]
		while intervalX == 0:
			i += 1

			intervalX = self.X[i]-self.X[i-1]

		maxy = max(self.Y) + fabs(intervalY)*0.5 # Max value for y axis 
		miny = min(self.Y) - fabs(intervalY)*0.5 # Min value for y axis
		maxx = max(self.X) + fabs(intervalX)*0.5 # max value for x axis
		minx = min(self.X) - fabs(intervalX)*0.5 # min value for x axis

		yerr = self.error() # error for IV

		# Represent the graphic
		fig = plt.figure(1)
		plt.errorbar(self.X, self.Y, yerr=yerr, fmt='ro', ecolor='r') 
		plt.plot(self.X, self.Y, 'ro', Xes, Yes, 'r')
		plt.axis([minx, maxx, miny, maxy])
		plt.title(Title)
		plt.xlabel(self.Xname)
		plt.ylabel(self.Yname)
		plt.show()
		f2 = plt.figure(figsize=(12.0, 20.0))
		i = 2
		Path2 = Path+Title+'.png'
		while os.path.exists(Path2):
			Path2 = Path+Title+'('+str(i)+')'+'.png'
			i+=1
		fig.savefig(Path2)

	def error(self):
		booltwo = True
		while booltwo:
			type_error = raw_input('Type: ')

			if type_error == 'Colmn Error' or type_error == 'Colmn error' or type_error == 'colmn error':
				num_column = int(raw_input('Column: '))
				return allData[num_column].get_list_values()
			elif type_error == 'Fixed Value' or type_error == 'Fixed value' or type_error == 'fixed value':
				error_value = float(raw_input("The %s's error " %(self.Yname))) # error for IV
				return error_value
			elif type_error == 'Percentage' or type_error == 'percentage':
				error_percent = float(raw_input('Percentage: '))
				error = []
				for i in range(len(self.Y)):
					error.append(self.Y[i] * (error_percent/100))
				return error
			else:
				print 'That is not an option'

class Straigth(Graphic):
	""" This class store a certain number of objects Variable """
	""" This class calculate the regression of the graphic    """
	""" supposing that both variables has a linear relation   """
	"""                       y = mx + b                      """

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.X = allData[x].get_list_values()
		self.Y = allData[y].get_list_values()
		self.Xname = allData[x].get_name()
		self.Yname = allData[y].get_name()

		self.n = len(self.X)
		self.Mxx = []
		for i in xrange(self.n):
			self.Mxx.append(self.X[i]**2)

	def slope(self):
		xless = [] # inicialize a list DV-Xmean
		a = [] # inicialize a list 
		xxi = [] # inicialize a list xless*xless
		for i in xrange(self.n): # loop append a new element to lists 
			xless.append(self.X[i] - medianX(self.x))
			a.append(xless[i] * self.Y[i])
			xxi.append(xless[i]**2)
		return sum(a) / sum(xxi) # return the slope
			
	def intercept(self):
		Mxy = [] # inicialize a list for DV*IV
		for i in xrange(self.n): # loop that append an element 
			Mxy.append(self.X[i]*self.Y[i]) # create the list DV * IV
		return (sum(self.Y)*sum(self.Mxx)-sum(self.X)*sum(Mxy)) / (self.n*sum(self.Mxx) - (sum(self.X))**2) # return intercept

	def errorslope(self):
		recta = []
		for i in xrange(self.n):
			recta.append((self.Y[i]-self.slope()*self.X[i]-self.intercept())**2)
		sigma = sqrt(sum(recta)/(self.n-2)) 
		return (sqrt(self.n)*sigma/sqrt((self.n*sum(self.Mxx))-sum(self.X)**2))

	def ertercept(self):
		a = self.errorslope() * sqrt(sum(self.Mxx)/self.n)
		return a

	def printer(self): # Print means and the graph equation 
		fl = open(Path+Title+'.txt','w')
		for x in xrange(1):
			fl.write('Los valores medios de X y de Y son:' + "\n")
			fl.write('\t' + ' <x>= %gm y <y>= %gs' %(medianX(self.x), medianX(self.y)) +'\n')
			fl.write('La ecuacion de la recta obtenida por el ajuste por minimos cuadrados es:' + '\n')
			fl.write('\t' + 'y = %gx + %g' %(self.slope(), self.intercept())+ '\t' + '\t' + 'Error m = %g' %(self.errorslope()) + '\n')
		fl.close()
		print 'Los valores medios de X y de Y son:' + "\n" + "\t" + ' <x>= %gm y <y>= %gs' %(medianX(self.x), medianX(self.y))
		print 'La ecuacion de la recta obtenida por el ajuste por minimos cuadrados es:' + '\n' + '\t' + 'y = %gx + %g' %(self.slope(), self.intercept())
		print 'EM = %g and EI = %g' %(self.errorslope(), self.ertercept())

	def get_Ecuation(self):
		xes = np.arange(min(self.X),max(self.X), ((max(self.X)-min(self.X))/100)) # create an array to represent the straight graphic on X axis
		yes = self.slope()*xes + self.intercept() # create a list to represent the straght graphic on Y axis
		main = [xes, yes]
		return main

class Logarithmic(Graphic):
	""" This class calculate the regression of the graphic    """
	""" supposing that both variables has a logarithmic       """
	""" relation:        y = m * ln(x) + b                    """

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.X = allData[x].get_list_values()
		self.Y = allData[y].get_list_values()
		self.Xname = allData[x].get_name()
		self.Yname = allData[y].get_name()

		self.sumX = sum(self.X) 
		self.sumY= sum(self.Y)
		self.sumLnX = 0
		self.sumLn2X = 0 
		self.sumLnXY = 0
		self.sumY2 = 0
		for i in xrange(len(self.X)):
			self.sumLnX += log(self.X[i])
			self.sumLn2X += log(self.X[i])*log(self.X[i])
			self.sumLnXY += log(self.X[i])*self.Y[i]
			self.sumY2 += self.Y[i]**2

	def slope(self):
		return (self.sumLnXY- self.sumY*self.sumLnX/len(self.X))/(self.sumLn2X - self.sumLnX*self.sumLnX/len(self.X))

	def intercept(self):
		return self.sumY/len(self.X) - self.slope()*self.sumLnX/len(self.X)

	def printer(self): # Print means and the graph equation 
		fl = open(Path+Title+'.txt','w')
		for x in xrange(1):
			fl.write('Los valores medios de X y de Y son:' + "\n")
			fl.write('\t' + ' <x>= %g m y <y>= %g s' %(medianX(self.x), medianX(self.y))+'\n')
			fl.write('La ecuacion de la recta obtenida por el ajuste por minimos cuadrados es:' + '\n')
			fl.write('\t' + 'y = %g* ln(x) + %g' %(self.slope(), self.intercept()) + '\n')
		print 'Los valores medios de X y de Y son:' + "\n" + "\t" + ' <x>= %gm y <y>= %gs' %(medianX(self.x), medianX(self.y))
		print 'La ecuacion de la curva es:' + '\n' + '\t' + 'y = %g*ln(x) + %g' %(self.slope(), self.intercept())
	
	def get_Ecuation(self):
		xes = np.arange(min(self.X),max(self.X), ((max(self.X)-min(self.X))/100)) # create an array to represent the curve graphic on X axis
		yes = [] # inicialize a list to represent the curve graphic on Y axis
		for x in xrange(xes.size):
			yes.append(self.slope()*log(xes[x])+self.intercept())

		main = [xes, yes]
		return main

class Exponential(Graphic):
	""" This class calculate the regression of the graphic    """
	""" supposing that both variables has an exponential      """
	""" relation:          y = b * e^(m*x)                    """

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.X = allData[x].get_list_values()
		self.Y = allData[y].get_list_values()
		self.Xname = allData[x].get_name()
		self.Yname = allData[y].get_name()

		self.Mxx = []
		self.sumy = 0
		for i in xrange(len(self.X)):
			self.Mxx.append(self.X[i]**2)
			self.sumy += log(self.Y[i])
		self.medy = self.sumy / len(self.Y)

	def slope(self):
		sumXLn = 0
		for i in xrange(len(self.Y)):
			sumXLn += self.X[i] * log(self.Y[i])
		return (sumXLn - (self.medy*sum(self.X))) / (sum(self.Mxx)-medianX(self.x)*sum(self.X))

	def intercept(self):
		return exp(self.medy-self.slope()*medianX(self.x))

	def printer(self): # Print means and the graph equation 
		fl = open(Path+Title+'.txt','w')
		for x in xrange(1):
			fl.write('Los valores medios de X y de Y son:' + "\n")
			fl.write('\t' + ' <x>= %g m y <y>= %g s' %(medianX(self.x), medianX(self.y))+'\n')
			fl.write('La ecuacion de la recta obtenida por el ajuste por minimos cuadrados es:' + '\n')
			fl.write('\t' + 'y = %g*e^(%gx)' %(self.intercept(), self.slope()) + '\n')
		print 'Los valores medios de X y de Y son:' + "\n" + "\t" + ' <x>= %gm y <y>= %gs' %(medianX(self.x), medianX(self.y))
		print 'La ecuacion de la curva es:' + '\n' + '\t' + 'y = %g*e^(%gx)' %(self.intercept(), self.slope())

	def get_Ecuation(self):
		xes = np.arange(min(self.X),max(self.X), ((max(self.X)-min(self.X))/100))# create an array to represent the curve graphic on X axis
		yes = [] # inicialize a list to represent the curve graphic on Y axis
		for x in xrange(xes.size):
			yes.append(self.intercept()*exp(self.slope()*xes[x]))

		main = [xes , yes]
		return main

class Operations():
	""" This class allows to make all the mathematicals       """
	""" operartions that Python allows, between data columns  """
	""" It should be indicated which columns by a upper C     """
	""" followed (without space) by the column's number       """

	def __init__(self):
		c = 2.998*(10**8) # set speed of ligth
		G = 6.67408 * (10**(-11)) # set gravitational constant
		h = 6.626 * (10**(-34)) # set Planck constant
		q = 1.6 * (10**(-19)) # set elementary charge
		k = 8.988 * (10**(9)) # set coulomb's constant
		self.new_name = raw_input('Column name: ')
		self.new_Data = []
		self.action = raw_input('C%s = ' %(len(allData))) # Se pide por pantalla la operacion
		booltwo = True # se inicializa el booleano para bucle while y la excepcion
		index = 0 # se inicializa el indice a partir del cual se leera
		self.action = self.action.replace('C', 'allData[') # se sustituyen todas la C por allData[
		while booltwo:
			try: # excepcion
				index = self.action.index('allData[', index, len(self.action))+9 # indice donde acaba allData
				self.action = self.action[:index] + '].get_values(i)' + self.action[index:]
			except ValueError:
				booltwo = False # se para el bucle
		try:
			for i in range(len(allData[0].get_list_values())):
				self.new_Data.append(eval(self.action))
		except (NameError, IndexError, ValueError, IOError):
			print 'Not able that operation'

		new_Object = Variable(self.new_name, self.new_Data)
		allData.append(new_Object)

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

#############################################################
###########              FUNCTIONS              #############
#############################################################

def new_proyect(): # Create a new proyect
	Title = str(raw_input('Title: ')) # Introduce the title of the practice
	Path = './Desktop/Python/'+Title+'/' # Directory wherever all document will be saved
		# if the directory does not exist, it will create it 
	dir = os.path.dirname(Path)
	if not os.path.exists(Path):
		os.makedirs(Path)
	return Path, Title # return a list with the Path and the Title

def print_screen(): # clear and print the data on screen
	global Title
	
	try: # handling exception
		length = len(allData[0].get_list_values())

		for i in range(len(allData)-1):
			if len(allData[i].get_list_values()) < len(allData[i+1].get_list_values()):
				length = len(allData[i+1].get_list_values())
	except (NameError, IndexError):
		error = 'error'

	os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal window

	try: # handling exception
		print '%50s' %(Title) + '\n' # if there is a title, print it as header
	except NameError, e:
		Title = 'Untitled' # if there is not, set Untitled has title

	print ' | '+'New Proyect'+' | '+'New Table'+' | '+'Open file'+' | '+'Graph'+' | '+'Curve Fit'+' | '+'Formula Entry'+' | '+'Modify Table'+' | '+'Save'+' | '+'\n' # print functions available

	try: # handling exception
		line = '' # inicialize the line
		for x in range(len(allData)): # loop for each variable
			line += '%12s' %(allData[x].get_name()) + '\t' # add each name to the line
		print line # print the line
				
		for i in range(length): # loop for the number of values
			try:
				line = '%6g' %(allData[0].get_values(i)) # the first number of each line is the corresponding value of the first variable
			except IndexError:
				line = '%6s' %(' ')
			for x in range(1, len(allData)): # loop for each variable
				try:
					line += '\t' + '%15.3g' %(allData[x].get_values(i)) # add the rest values of variables
				except IndexError:
					line += '\t' + '%15.3s' %(' ')
			print line # print the line
	except (NameError, IndexError):
		error = 'error'

def save(): # save lists into a .csv archive in /home/jaime/Documentos/Data/ path
	fl = open(Path+Title+'.csv', 'w') # open and create an .csv file

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

	fl = open(Path+'LaTex.txt', 'w') # open and create an .ods file
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
		for x in range(len(allData)-1):
			line += ' & ' + '%s' %(allData[x+1].get_name())
		fl.write(line+' \\'+'\\\hline'+'\n')

		for i in range(length-1):
			try:
				line = '\t'+'\t'+'\t'+'%g' %(allData[0].get_values(i))
			except IndexError:
				line = '\t'+'\t'+'\t'+' '

			for x in range(len(allData)-1):
				try:
					line += ' & ' + '%g' %(allData[x+1].get_values(i))
				except IndexError:
					line += ' & '+' '					
			fl.write(line+ ' \\'+'\\'+'\n')
		
		try:
			line = '\t'+'\t'+'\t'+'%g' %(allData[0].get_values(i))
		except IndexError:
			line = '\t'+'\t'+'\t'+' '

		for x in range(len(allData)-1):
			try:
				line += ' & '+'%g' %(allData[x+1].get_values(length-1))
			except IndexError:
				line += ' & '+' '
		fl.write(line+' \\'+'\\\hline'+'\n')

		fl.write('\t'+'\\end{tabular}'+'\n')
		fl.write('\t'+'\\caption{\\label{Tab:}}'+'\n')
		fl.write('\\end{table}'+'\n')
	fl.close() # close file

def medianX(column): # return the mean of DV                   
	thisData = allData[column].get_list_values()
	med = sum(thisData) / len(thisData) # return the DV mean
	return med

def graph(x, y): # print the graph

	X = allData[x].get_list_values()
	Y = allData[y].get_list_values()

	i = 1
	intervalY = Y[i]-Y[i-1]
	while intervalY == 0:
		i += 1
		intervalY = Y[i]-Y[i-1]
	i = 1
	intervalX = X[i]-X[i-1]
	while intervalX == 0:
		i += 1
		intervalX = X[i]-X[i-1]

	maxy = max(Y) + fabs(intervalY)*0.5 # Max value for y axis 
	miny = min(Y) - fabs(intervalY)*0.5 # Min value for y axis
	maxx = max(X) + fabs(intervalX)*0.5 # max value for x axis
	minx = min(X) - fabs(intervalX)*0.5 # min value for x axis

	# Represent the graphic
	fig = plt.figure(1)
	plt.plot(X, Y, 'ro')
	plt.axis([minx, maxx, miny, maxy])
	plt.title(Title)
	plt.xlabel(allData[x].get_name())
	plt.ylabel(allData[y].get_name())
	plt.show()
	f2 = plt.figure(figsize=(12.0, 20.0))
	fig.savefig(Path+Title+'.png')

#############################################################
###########              INTERFACE              #############
#############################################################

print '| New Proyect | New Table | Open file | Graph | Curve Fit | Formula Entry | Modify Table | Save |'+'\n' # print functions available

function = str(raw_input('Choose function: ')) # select one function

while function != 'close': # loop to select function. if the close, stop the program

	try:
		if function == 'New Proyect' or function == 'new proyect' or function == 'New proyect': # start a new proyect
			Proyect = new_proyect() # new proyect
			Title = Proyect[1] # proyect name
			Path = Proyect[0] # directory Path
			allData = [] # inicialize the Data list
			print_screen()

		elif function == 'Open file' or function == 'open file' or function == 'Open File': # get the data from a file		
			allData = Open_file().get_all() # take data from a file
			print_screen()

		elif function == 'New Table' or function == 'new table' or function == 'New table':
			try:
				allData.append(New_table().get_Variable()) # insert data
				print_screen()
				addcol = str(raw_input('add a Column '))
				while addcol == 'yes':
					allData.append(New_table().get_Variable())
					print_screen()
					addcol = str(raw_input('add a Column '))
				print_screen()
			except NameError:
				print 'First create a new proyect'

		elif function == 'Graph' or function == 'graph': # print the graph
			x = int(raw_input('Dependent variable column: '))
			y = int(raw_input('Independent variable column: '))
			try:
				graph(x,y)
				print_screen()
			except IndexError:
				print_screen()
				print 'Could not represent variable with differents meassures'

		elif function == 'Curve Fit' or function == 'Curve fit' or function == 'curve fit': # print the graph
			boolfour = True
			try:
				while boolfour:
					type_of = raw_input('Choose type: ')
					if type_of == 'Linear' or type_of == 'linear':
						fit = Straigth(x,y)
						fit.graph() # print the linear function
						fit.printer() # print the result of the Straigth
						boolfour = False
						print_screen()
					elif type_of == 'Logarithmic' or type_of == 'logarithmic':
						fit = Logarithmic(x,y)
						fit.graph() # print a logarithmic function
						fit.printer() # print the results of a logarithmic expresion
						boolfour = False
						print_screen()
					elif type_of == 'Exponential' or type_of == 'exponential':
						fit = Exponential(x,y)
						fit.graph() #print an exponential function
						fit.printer() # print the results of an exponential expresion
						boolfour = False
						print_screen()
					else:
						print 'Sorry that is not an option'
			except IndexError:
				print_screen()
				print 'Could not represent variable with differents meassures'

		elif function == 'Save' or function == 'save':
			save() # ejecute save()function	
			print_screen()

		elif function == 'Formula Entry' or function == 'Formula entry' or function == 'formula entry':
			try:
				Operations()
				print_screen()
			except IndexError:
				print_screen()
				print 'Could not represent variable with differents meassures'

		elif function == 'Modify Table' or function == 'Modify table' or function == 'modify table':
			Modify_Table()
			print_screen()
		
		else:
			print 'Sorry I do not understand'

	except (NameError, IndexError, ValueError, IOError, SyntaxError):
		print_screen()
		print 'Error 99'

	function = str(raw_input('Choose function: ')) # select one function

#############################################################
#############################################################
os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal window
