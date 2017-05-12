#########################################
#           Graphics Values             #
#########################################
#
#   This class get and caulculate all needed
#        values to plot a graph.
#
#   Required Attributes: - Columns values \ list(valuesX, valuesY)
#                        - Columns index \ list(str(TitleX), str(TitleY))
#                        - Y-Axis' Error \ float or list \ by default is 0
#
#   Attributes: - X-axis values \ list(xAxis)
#               - Y-axis values \ list(yAxis)
#               - X-axis title \ str(xTitle)
#               - Y-axis title \ str(yTitle)
#               - X-axis interval \ list(xInterval) = [min, max]
#               - X-axis interval \ list(yInterval) = [min, max]
#
#   Function: - linearRegression: Calculate the coefficients of a linear regression
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

import numpy as np

class GraphPlot():

    def __init__(self, values, titles, Error=0):
        from math import fabs

        self.xAxis = values[0]
        self.yAxis = values[1]

        self.xTitle = titles[0]
        self.yTitle = titles[1]

        self.error = Error
        if type(self.error) == float or type(self.error) == int:
            self.error = [self.error for i in xrange(len(self.yAxis))]

        self.xTh = np.arange(min(self.xAxis),max(self.xAxis), ((max(self.xAxis)-min(self.xAxis))/100))

        xdiff = [fabs(self.xAxis[i+1] - self.xAxis[i]) for i in range(len(self.xAxis)-1) if self.xAxis[i+1] - self.xAxis[i] != 0]
        xdiff = max(xdiff)

        ydiff = [fabs((self.yAxis[i+1]+self.error[i+1]) - (self.yAxis[i]-self.error[i])) for i in range(len(self.yAxis)-1) if self.yAxis[i+1] - self.yAxis[i] != 0]
        ydiff = max(ydiff)

        self.xInterval = [min(self.xAxis) - fabs(xdiff)*0.5 , max(self.xAxis) + fabs(xdiff)*0.5]
        self.yInterval = [min(self.yAxis) - fabs(ydiff)*0.5 , max(self.yAxis) + fabs(ydiff)*0.5]


    def setError(self, Error):

        self.error = Error

    def linearRegression(self):
        from scipy import stats

        slope, intercept, r_value, p_value, std_err = stats.linregress(self.xAxis, self.yAxis)

        self.text = "    " + "y = mx + b " + "\t" + "\n" + "m : " + "\t" + "%g" %(slope) + "\n" + "b : " + "\t" + "%g" %(intercept)

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
        intercept = sumY/len(self.xAxis) - slope*sumLnX/len(self.xAxis)

        self.text = "    " + "y = m * ln(x) + b" + "\t" + "\n" + "m : " + "\t" + "%g" %(slope) + "\n" + "b : " + "\t" + "%g" %(intercept)

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

        self.text = "    " + "y = b * e^(m*x)" + "\t" + "\n" + "m : " + "\t" + "%g" %(slope) + "\n" + "b : " + "\t" + "%g" %(intercept)

        return slope, intercept

    def polynomialRegression(self, grade):
        import numpy as np

        parameters = np.polyfit(self.xAxis, self.yAxis, grade)
        z = map(chr, range(97, 123))

        eqtion = 'y = ' + z[0] + '*x^' + str(len(parameters)-1)

        for i in range(1, len(parameters)):
            eqtion += ' + ' + z[i] + '*x^' + str(len(parameters)-(i+1))

        solution = "\t" + "\n" + z[0] + ': ' + "\t" + "%g" %(parameters[0])

        for i in range(1, len(parameters)):
            solution += "\n" + z[i] + ": " + "\t" + "%g" %(parameters[i])

        self.text = "    " + eqtion + solution

        return parameters

    def pepepe(self, m, path=None):
        from SaveScript import saveLaTex

        table = {self.xTitle : self.xAxis, self.yTitle:self.yAxis, "$\Delta "+self.yTitle+"$": self.error}
        index = {0 : self.xTitle, 1 : self.yTitle, 2 : "$\Delta "+self.yTitle+"$"}
        m = float(m)

        if m < 0:
            division0 = lambda x, m: x**m if x != 0 else 0
            xm = [ division0(x,m) for x in self.xAxis ]
            division0 = lambda x, m : x**(2*m) if x != 0 else 0
            x2m = [ division0(x,m) for x in self.xAxis ]

        else:
            xm = [ x**m for x in self.xAxis ]
            x2m = [ x**(2*m) for x in self.xAxis ]

        table["$"+self.xTitle+"^{2\cdot{"+str(m)+"}}$"] = x2m
        table["$"+self.xTitle+"^{"+str(m)+"}$"] = xm
        index[3] = "$"+self.xTitle+"^{"+str(m)+"}$"
        index[5] = "$"+self.xTitle+"^{2\cdot{"+str(m)+"}}$"

        absxm = [ abs(xmElement) for xmElement in xm ]
        table["$|"+self.xTitle+"^{"+str(m)+"}|$"] = absxm
        index[4] = "$|"+self.xTitle+"^{"+str(m)+"}|$"

        yxm = [ self.yAxis[i] * xm[i] for i in range(len(xm)) ]
        table["$"+self.yTitle+""+self.xTitle+"^{"+str(m)+"}$"] = yxm
        index[6] = "$"+self.yTitle+""+self.xTitle+"^{"+str(m)+"}$"

        absxmDy = [absxm[i]*self.error[i] for i in range(len(absxm))]
        table["$|"+self.xTitle+"^{"+str(m)+"}|\Delta "+self.yTitle+"$"] = absxmDy
        index[7] = "$|"+self.xTitle+"^{"+str(m)+"}|\Delta "+self.yTitle+"$"

        table[index[5]].append(sum(x2m))
        table[index[6]].append(sum(yxm))
        table[index[7]].append(sum(absxmDy))

        saveLaTex(table, index, [0,1,2,3,4,5,6,7], path)

        a = sum(yxm)/sum(x2m)
        Da = sum(absxmDy)/sum(x2m)

        self.text = 'y = %s * x ^ %s' %(a, m) + '\n' + 'Error de a = %s' %(Da)

        return a , Da
