#########################################
#		    Graphics Values     	    #
#########################################
#
#	This class get and caulculate all needed
#        values to plot a graph.
#
#	Required Attributes: - Columns values \ dict(table)
#			             - Columns index \ dict(index)
#                        - Indexes of the Columns you want to plot \ list(columns) [X-axis, Y-axis]
#
#	Attributes: - X-axis values \ list(xAxis)
#               - Y-axis values \ list(yAxis)
#               - X-axis title \ str(xTitle)
#               - Y-axis title \ str(yTitle)
#               - X-axis interval \ list(xInterval) = [min, max]
#               - X-axis interval \ list(yInterval) = [min, max]
#
#	Function: - linearRegression: Calculate the coefficients of a linear regression
#                         * Return list(m, b) 
#                                  y = m*x + b
#             - logarithmicRegression: Calculate the coefficients of a logarithmic regression
#                         * Return list(m, b) 
#                                  y = m * ln(x) + b
#             - exponentialRegression: Calculate the coefficients of an exponential regression
#                         * Return list(m, b) 
#                                 y = b * e^(m*x)
#             - polynomialRegression: Calculate the coefficients of a polynomial regression
#                         * Return array(an, ..., a2, a1, a0) 
#                                  y = an*x^(n)+...+a2*x^2+a1*x+a0
#             - PepepeRegression: Calculate the regression as my Laboratory's teacher wants
#                         * Return list(a , error of a) 
#                                  y = a*x^m
#
#######################################################################################################

class GraphPlot():

	def __init__(self, table, index, columns):
		from math import fabs

		self.xAxis = table[index[columns[0]]]
		self.yAxis = table[index[columns[1]]]

		self.xTitle = index[columns[0]]
		self.yTitle = index[columns[1]]

		xdiff = [fabs(self.xAxis[i+1] - self.xAxis[i]) for i in range(len(self.xAxis)-1) if self.xAxis[i+1] - self.xAxis[i] != 0]
		xdiff = max(xdiff)

		ydiff = [fabs(self.yAxis[i+1] - self.yAxis[i]) for i in range(len(self.yAxis)-1) if self.yAxis[i+1] - self.yAxis[i] != 0]
		ydiff = max(ydiff)

		self.xInterval = [min(self.xInterval) - fabs(xdiff)*0.5 , max(self.xAxis) + fabs(xdiff)*0.5]
		self.yInterval = [min(self.yInterval) - fabs(ydiff)*0.5 , max(self.yAxis) + fabs(ydiff)*0.5]

	def linearRegression(self):
		from scipy import stats

		slope, intercept, r_value, p_value, std_err = stats.linregress(self.xAxis, self.yAxis)

		return slope, intercept

	def logarithmicRegression(self):
		from math import log

		sumX = sum(self.xAxis)
		sumY= sum(self.yAxis)
		sumLnX = 0
		sumLn2X = 0
		sumLnXY = 0
		sumY2 = 0
		for i in xrange(len(self.xAxis)):
			sumLnX += log(self.xAxis[i])
			sumLn2X += log(self.xAxis[i])**2
			sumLnXY += log(self.xAxis[i])*self.yAxis[i]
			sumY2 += self.yAxis[i]**2

		slope = (sumLnXY- sumY*sumLnX/len(self.xAxis))/(sumLn2X - sumLnX*sumLnX/len(self.xAxis))
		intercept = sumY/len(self.xAxis) - slope*sumLnX/len(self.Dependent)

		return slope, intercept

	def exponentialRegression(self):
		from math import exp, log

		Mxx = [x**2 for x in self.xAxis]
		sumy = sum( [ log(y) for y in self.yAxis ] )
		medy = sumy / len(self.yAxis)
		xMedian = sum([x for x in self.xAxis]) / len(self.xAxis)

		sumXLn = sum( [ self.xAxis[i]*log(self.yAxis[i])  for i in range(len(self.xAxis)) ] )

		slope = (sumXLn - (medy*sum(self.xAxis))) / (sum(Mxx)-xMedian*sum(self.xAxis))

		intercept = exp(medy-slope*xMedian)

		return slope, intercept

	def polynomialRegression(self, grade):
		import numpy as np

		parameters = np.polyfit(self.xAxis, self.yAxis, grade)

		return parameters

	def pepepe(self, error, m, path):
		from SaveScrypt import saveLaTex

		Dy = error

		table = {self.xTitle : self.xAxis, self.yTitle:self.yAxis, "$\Delta y$": Dy}
		index = {0 : self.xTitle, 1 : yTitle, 2 : "$\Delta y$"}
		m = float(m)

		xm = [ x**m for x in self.xAxis ]
		table["$x^m$"] = xm
		index[3] = "$x^m$"

		absxm = [ abs(xmElement) for xmElement in xm ]
		table["$|x^m|$"] = absxm
		index[4] = "$|x^m|$"

		x2m = [ x**(2*m) for x in self.xAxis ]
		table["$x^{2m}$"] = x2m
		index[5] = "$x^{2m}$"

		yxm = [ self.yAxis[i] * xm[i] for i in range(len(xm)) ]
		table["$yx^m$"] = yxm
		index[6] = "$yx^m$"

		try:
			absxmDy = [absxm[i]*Dy[i] for i in range(len(absxm))]
		except TypeError:
			absxmDy = [absxmElement*Dy for absxmElement in absxm]
		table["$|x^m|\Delta y$"] = absxmDy
		index[7] = "$|x^m|\Delta y$"

		saveLaTex(table, index, [0,1,2,3,4,5,6,7], path)

		return sum(self.yxm)/sum(self.x2m) , sum(absxmDy)/sum(x2m)
