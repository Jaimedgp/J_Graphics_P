#########################################
#		Calculator (Formula Entry)	    #
#########################################
#
#	This class allows to make all the mathematical operations
#		that Python allows, between table's columns.
#	It should be indicated which columns by a upper C followed
#		(without space) by the column's number.
#
#	Required Attributes: - equation \ str(equation)
#			             - Columns values \ dict(table)
#                        - Columns index \ dict(index)
#
#	Function: - error: ErrorsCalculator function from WidgetsScrypt
#             - name: Change the Column's name
#                      Requisites: * The new Name
#             - delete: Delete a Column
#             - get_index: Get the index of the column to be changed
#             - translateAction: translate the "CX" for the X's column
#
#	Return: - The new Columns values and Columns index with the changes
#                  if the class return 0 it means that it has been an error
#
##############################################################################

from math import *

class Operations():

	def __init__(self, equation, table, index):

		c = 2.998*(10**8) # set speed of ligth
		g = 9.81 #set universal gravitational constant
		G = 6.67408 * (10**(-11)) # set gravitational constant
		h = 6.626 * (10**(-34)) # set Planck constant
		q = 1.6 * (10**(-19)) # set elementary charge
		k = 8.988 * (10**(9)) # set coulomb's constant on the vacuum

		self.table = table
		self.index = index

		newIndex, self.action = equation.split("=")
		self.newIndex = int(newIndex[1:])

		self.main()

	def main(self):

		try:
			self.index[self.newIndex]

			try:
				indexFunction = self.action.index("name(")
				self.action = self.action[:indexFunction-1] + 'self.' + self.action[indexFunction-1:]
				eval(self.action)
				return self.table, self.index
			except ValueError:

				try:
					indexFunction = self.action.index("delete(")
					self.action = self.action[:indexFunction-1] + 'self.' + self.action[indexFunction-1:]
					eval(self.action)
					return self.table, self.index
				except ValueError:
					return 0

		except KeyError:
			self.index[newIndex] = str(newIndex)

		try:
			indexFunction = self.action.index("Errors(")
			self.action = self.action[:indexFunction-1] + 'self.' + self.action[indexFunction-1:]
			eval(self.action)
			return self.table, self.index
		except ValueError:

			try:
				boolean = True
				element = 0
				self.action = self.action.replace('C', 'self.table[self.index[')
				initialI = self.action.index('self.table[self.index[') + 22
				finalI = self.action.index(']')
				involvedColumn = self.action[initialI:finalI]
				while boolean:
					try:
						element =self.action.index('self.table[self.index[', element, len(self.action)+23)
						self.action = self.action[:element] + ']][i]' + self.action[element:]
					except ValueError:
						boolean = False
				values = [ eval(str(self.action)) for i in range(len(self.table[self.index[involvedColumn]])) ]
				self.table[str(newIndex)] = values
				return self.table, self.index
			except (NameError, IndexError, ValueError, IOError):
				return 0

	def name(self, name):
		self.table[str(name)] = self.table[self.index[self.newIndex]]
		del self.table[self.index[self.newIndex]]

		self.index[self.newIndex] = str(name)

	def delete(self):
		del self.table[self.index[self.newIndex]]
		del self.index[self.newIndex]

	def Errors(self, symbols, values, errors, function):
		from WidgetsScrypt import ErrorsCalculator
		tableValues = []
		newValues = [eval(values[i].replace('C', 'self.table[self.index[') + ']]') for i in range(len(values))]
		newErrors = [eval(errors[i].replace('C', 'self.table[self.index[') + ']]') for i in range(len(errors))]

		for i in range(len(newValues[0])):
			values = [newValues[n][i] for n in range(len(newValues))]
			errors = [newErrors[n][i] for n in range(len(newErrors))]
			err = ErrorsCalculator(symbols, values, errors, funcion)
			tableValues.append(err)

		self.index[newIndex] = "Error"
		self.table["Error"] = tableValues
