###########################################
#		write and save the Data           #
###########################################
#	Store a certain number of Table's columns with their
#		names and values into a dictionary, from a CSV file
#
#		Required: - Directory and name of the CSV file \ str(path)
#
#		Return: - Data with name and values \ Dictionary(Table)
#               - Columns index \ dict(index)
#
####################################################################

def Open_file_CSV(path):

	if type(path) !=  str:
		path = str(path)

	fr = open(path, 'r')

	titles = fr.readline().split(',')
	numColumns = len(titles)

	rowValues = [[] for x in xrange(numColumns)]
	row = fr.readline().split(',')

	while row[0] != '':
		for i in xrange(numColumns):
			try:
				rowValues[i].append(float(row[i])) # append each element to the list
			except (ValueError):
				error = 1
		row = fr.readline().split(',') # read another row

	table = dict([(titles[i].split()[0], rowValues[i]) for i in xrange(numColumns)])
	index = dict([(i, titles[i].split()[0]) for i in xrange(numColumns)])

	return table, index


###########################################
#		write and save the Data           #
###########################################
#	Store a certain number of Table's columns with their
#		names and values into a dictionary, from a TXT file
#
#		Required: - Directory and name of the TXT file \ str(path)
#
#		Return: - Data with name and values \ Dictionary(Table)
#
######################################################################

def Open_file_TXT(path):

	if type(path) !=  str:
		path = str(path)

	fr = open(path, 'r')

	titles = fr.readline().split('\t')
	numColumns = len(titles)

	rowValues = [[] for x in xrange(numColumns)]
	row = fr.readline().split('\t')

	while row[0] != '':
		for i in xrange(numColumns):
			try:
				rowValues[i].append(float(row[i])) # append each element to the list
			except (ValueError):
				error = 1
		row = fr.readline().split('\t') # read another row

	table = dict([(titles[i].split()[0], rowValues[i]) for i in xrange(numColumns)])
	index = dict([(i, titles[i].split()[0]) for i in xrange(numColumns)])

	return table, index