from sympy import *

class Errores(object):

	def __init__(self):
		self.variables = raw_input('Variables: ')
		self.variables = self.variables.split(' ')
		S = symbols(self.variables)
		self.values = eval(raw_input('Valores: '))
		self.errors = eval(raw_input('Errores: '))
		self.f = str(raw_input('funcion: '))
		for n in range(len(S)):
			selement = 'S['+str(n)+']'
			self.f = self.f.replace(self.variables[n], selement)
		print self.f
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

print Errores().Errors()
