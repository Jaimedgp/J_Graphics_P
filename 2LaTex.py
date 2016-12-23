"""
	2LaTex (LaTex TABLE CONVERTER)

	A Python program that allows convert your table of data as .csv 
	files to LaTex code for a table.

															Version 1.0
"""

import os  # import os Miscellaneous operating system interfaces

os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal window

############################################################
########               PROGRAM BODY             ############
############################################################

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
				try:
					row[i] = float(row[i])
					Data[i].append(row[i]) # append each element to the list
				except ValueError:
					error = 'error'
			row = fr.readline().split(',') # read another row
		for x in xrange(numVar):
			self.allData.append(Variable(titles[x].split()[0], Data[x])) # creat a Variable Object with each variable

	def get_all(self): # return a list with all the objetcs
		return self.allData

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

def save():
	length = len(allData[0].get_list_values())

	for i in range(len(allData)-1):
		if len(allData[i].get_list_values()) < len(allData[i+1].get_list_values()):
			length = len(allData[i+1].get_list_values())

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

Proyect = new_proyect()
Path = Proyect[0]
Title = Proyect[1]
allData = Open_file().get_all()
save()
