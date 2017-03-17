###########################################
#		write and save the Data           #
###########################################
#	write the data given in a CSV file
#
#		Required: - Data with name and values \ Dictionary(Table)
#                 - Dictionary(table)'s indexes \ Dictionary(index)
#				  - Directory and name of the file \ str(path)
#
#		Return: - Create the CSV file
#
####################################################################

def saveCSV(table, index, path):

	fw = open(path, 'w')

	length = 0
	title = []

		# length of the largest column
	for name, values in table.iteritems():

		if length < len(values):
			length = len(values)
	
	fw.write(' , '.join([index[i] for i in index]) + '\n')

	# Columns' rows
	for i in range(length):
		row = []
		for col in index:
			try:
				row.append(str(table[index[col]][i]))
			except IndexError:
				row.append(' ')
		row = ' , '.join(row)
		fw.write(row + '\n')
	fw.close()


###########################################
#		write and save the Data           #
###########################################
#	write the data given in a TXT file
#
#		Required: - Data with name and values \ Dictionary(Table)
#                 - Dictionary(table)'s indexes \ Dictionary(index)
#				  - Directory and name of the file \ str(path)
#
#		Return: - Create the TXT file
#
####################################################################

def saveTXT(table, index, path):

	fw = open(path, 'w')

	length = 0
	title = []

		# length of the largest column
	for name, values in table.iteritems():

		if length < len(values):
			length = len(values)

	fw.write(' \t '.join([index[i] for i in index]) + '\n')

	# Columns' rows
	for i in range(length):
		row = []
		for col in index:
			try:
				row.append(str(table[index[col]][i]))
			except IndexError:
				row.append(' ')
		row = ' \t '.join(row)
		fw.write(row + '\n')
	fw.close()


###########################################
#		write and save the Data           #
###########################################
#	write the data given in a LaTeX file
#
#		Required: - Data with name and values \ Dictionary(Table)
#                 - Dictionary(table)'s indexes \ Dictionary(index)
#                 - Indexes of the Columns you want to save \ list(columns)
#				  - Directory and name of the file \ str(path)
#
#		Return: - Create the LaTeX file
#
#################################################################################

def saveLaTex(table, index, columns, path):

	fw = open(path, 'w')

	length = 0
	# Largest column's length
	for values in table.values():
		if length < len(values):
			length = len(values)

	# LaTex Header
	fw.write('\\begin{table}[H]'+'\n')
	fw.write('\t'+'\\centering'+'\n')
	fw.write('\t'+'\\begin{tabular}{ '+ ' '.join([ 'c ' for name in table ]) + '}'+'\n')
	fw.write('\t'+'\t'+ '\\'+ '\\\hline'+'\n')
	fw.write('\t'+'\t'+'\\centering'+'\n')

	title = [index[col] for col in columns]
	# Columns' title
	fw.write('\t'+'\t'+'\t'+ ' & '.join(title) +' \\'+'\\\hline'+'\n')

	# Columns' rows
	for i in range(length-1):
		row = []
		for col in columns:
			try:
				row.append(str(table[index[col]][i]))
			except IndexError:
				row.append(' ')
		fw.write('\t'+'\t'+'\t'+ ' & '.join(row) +' \\'+'\\'+'\n')

	# last columns' row
	row = []
	for col in columns:
		try:
			row.append(str(table[index[col]][length-1]))
		except IndexError:
			row.append(' ')
	fw.write('\t'+'\t'+'\t'+ ' & '.join(row) +' \\'+'\\\hline'+'\n')

	# Footer
	fw.write('\t'+'\\end{tabular}'+'\n')
	fw.write('\t'+'\\caption{\\label{Tab:}}'+'\n')
	fw.write('\\end{table}'+'\n')
	fw.close()