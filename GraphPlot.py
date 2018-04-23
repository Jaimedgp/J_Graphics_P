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
#   Function: - linearRegression: Calculate the coefficients of a linear 
#                                 regression
#                         * Return list(m, b) 
#                                  y = m*x + b
#             - logarithmicRegression: Calculate the coefficients of a 
#                                      logarithmic regression
#                         * Return list(m, b) 
#                                  y = m * ln(x) + b
#             - exponentialRegression: Calculate the coefficients of an 
#                                      exponential regression
#                         * Return list(m, b) 
#                                 y = b * e^(m*x)
#             - polynomialRegression: Calculate the coefficients of a polynomial
#                                     regression
#                         * Return array(an, ..., a2, a1, a0) 
#                                  y = an*x^(n)+...+a2*x^2+a1*x+a0
#             - PepepeRegression: Calculate the regression as my Laboratory's 
#                                 teacher wants
#                         * Return list(a , error of a) 
#                                  y = a*x^m
#             - nodosChebyshev: Obtein the Chebyshev's nodes for the theorical 
#                                 representation.
#
################################################################################

import numpy as np

class GraphPlot():

    def __init__(self, values, titles, Error=0):

        self.xAxis = values[0]
        self.yAxis = values[1]

        self.xTitle = titles[0]
        self.yTitle = titles[1]

        self.error = Error
        if type(self.error) == float or type(self.error) == int:
            self.error = [self.error for i in xrange(len(self.yAxis))]

        self.xTh = self.nodosChebyshev()

        self.setInterval(self.xAxis, self.yAxis) 

    def setInterval(self, x, y):
        from math import fabs

        xdiff = [fabs(x[i+1] - x[i]) for i in range(len(x)-1) 
                                                          if x[i+1] - x[i] != 0]
        xdiff = max(xdiff)

        ydiff = [fabs((y[i+1]+self.error[i+1]) - (y[i]-self.error[i])) 
                                 for i in range(len(y)-1) if y[i+1] - y[i] != 0]
        ydiff = max(ydiff)

        if ydiff == 0:

            ydiff = [fabs((y[i]+self.error[i]) - (y[i+1]-self.error[i+1])) 
                                 for i in range(len(y)-1) if y[i+1] - y[i] != 0]
            ydiff = max(ydiff)

        self.xInterval = [min(x) - fabs(xdiff)*0.5 , max(x) + fabs(xdiff)*0.5]
        self.yInterval = [min(y) - fabs(ydiff)*0.5 , max(y) + fabs(ydiff)*0.5]

    def setError(self, Error):

        self.error = Error

    def linearRegression(self):
        from scipy import stats

        slope, intercept, r_value, p_value, std_err = stats.linregress(
                                                         self.xAxis, self.yAxis)

        self.text = """
    <html>
    <head>
        <title>HTML Table Colspan/Rowspan</title>
    </head>

    <body>
        <center>
        <table border = "1">
            <tr>
                <th colspan= "3"><center> """+"y = mx + b"+""" </center></th>
            </tr>
            <tr>
                <td><center> m </center></td>
                <td><center> """+"%g" %(slope)+""" </center></td>
                <td><center> """+"%g" %(std_err)+""" </center></td>
            </tr>
            <tr>
                <td><center> b </center></td>
                <td><center> """+"%g" %(intercept)+""" </center></td>
            </tr>
            <tr>
                <td><center> R </center></td>
                <td><center> """+"%g" %(r_value)+""" </center></td>
            </tr>
        </table>
        </center>
    </body>
    </html>"""

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

        slope = ((sumLnXY- sumY*sumLnX/len(self.xAxis))/
                                      (sumLn2X - sumLnX*sumLnX/len(self.xAxis)))
        intercept = sumY/len(self.xAxis) - slope*sumLnX/len(self.xAxis)

        self.text = """
    <html>

        <head>
            <title>HTML Table Colspan/Rowspan</title>
        </head>

        <body>
            <center>
            <table border = "1">
                <tr>
                    <th colspan= "2"><center> """+"y = m * ln(x) + b"+""" </center></th>
                </tr>
                <tr>
                    <td><center> m </center></td>
                    <td><center> """+"%g" %(slope)+""" </center></td>
                </tr>
                <tr>
                    <td><center> b </center></td>
                    <td><center> """+"%g" %(intercept)+""" </center></td>
                    <td><center>  </center></td>
                </tr>
            </table>
            </center>
        </body>
    </html>"""

        return slope, intercept

    def exponentialRegression(self):
        from math import exp, log

        Mxx = [x**2 for x in self.xAxis]
        sumy = sum( [ log(y) for y in self.yAxis ] )
        medy = sumy / len(self.yAxis)
        xMedian = sum([x for x in self.xAxis]) / len(self.xAxis)

        sumXLn = sum([ self.xAxis[i]*log(self.yAxis[i])  
                                            for i in range(len(self.xAxis)) ])

        slope = ((sumXLn - (medy*sum(self.xAxis))) / 
                                             (sum(Mxx)-xMedian*sum(self.xAxis)))

        intercept = exp(medy-slope*xMedian)

        self.text = """
        <html>
            <head>
                <title>HTML Table Colspan/Rowspan</title>
            </head>

            <body>
                <center>
                <table border = "1">
                    <tr>
                        <th colspan= "2"><center> """+"y = b * e^(m*x)"+""" </center></th>
                    </tr>
                    <tr>
                        <td><center> m </center></td>
                        <td><center> """+"%g" %(slope)+""" </center></td>
                    </tr>
                    <tr>
                        <td><center> b </center></td>
                        <td><center> """+"%g" %(intercept)+""" </center></td>
                        <td><center>  </center></td>
                    </tr>
                </table>
                </center>
            </body>
        </html>"""

        return slope, intercept

    def polynomialRegression(self, grade):
        import numpy as np

        parameters = np.polyfit(self.xAxis, self.yAxis, grade)
        z = map(chr, range(97, 123))

        eqtion = 'y = ' + z[0] + '*x^' + str(len(parameters)-1)

        for i in range(1, len(parameters)):
            eqtion += ' + ' + z[i] + '*x^' + str(len(parameters)-(i+1))

        solution = ("""<tr>""" +
                        """<td><center> """ + z[0] + """ </center></td> """ + 
                        """<td><center> """ + "%g" %(parameters[0]) +  """ </center></td> """ + 
                        """<td><center> """ + z[1] + """ </center></td> """ +
                        """<td><center> """ + "%g" %(parameters[1])+""" </center></td> """+
                    """</tr>""")

        for i in range(1, len(parameters)/2):
            solution += ("""<tr>""" +
                             """<td><center> """ + z[2*i] + """ </center></td> """ + 
                             """<td><center> """ + "%g" %(parameters[2*i]) +  """ </center></td> """ + 
                             """<td><center> """ + z[2*i+1] + """ </center></td> """ +
                             """<td><center> """ + "%g" %(parameters[2*i+1])+""" </center></td> """+
                         """</tr>""")

        self.text = """<html>
                           <head>
                              <title>HTML Table Colspan/Rowspan</title>
                           </head>

                           <body>
                              <center>
                              <table border = "1">
                                 <tr>
                                    <th colspan= "4"><center> """+eqtion+""" </center></th>
                                 </tr>
                                 """+solution+"""
                              </table>
                              </center>
                           </body>
                        </html>"""

        return parameters

    def pepepe(self, m, path=None):
        from SaveScript import saveLaTex

        xTitle = self.xTitle.split('/')[0].replace('$', '')
        yTitle = self.yTitle.split('/')[0].replace('$', '')

        table = {self.xTitle.split('/')[0]+'$' : self.xAxis, 
                                      self.yTitle.split('/')[0]+'$':self.yAxis, 
                                              "$\Delta "+yTitle+"$": self.error}
        index = {0 : self.xTitle.split('/')[0]+'$',
                                             1 : self.yTitle.split('/')[0]+'$',
                                                      2 : "$\Delta "+yTitle+"$"}
        m = float(m)

        if m < 0:
            division0 = lambda x, m: x**m if x != 0 else 0
            xm = [ division0(x,m) for x in self.xAxis ]
            division0 = lambda x, m : x**(2*m) if x != 0 else 0
            x2m = [ division0(x,m) for x in self.xAxis ]

        else:
            xm = [ x**m for x in self.xAxis ]
            x2m = [ x**(2*m) for x in self.xAxis ]

        table["$"+xTitle+"^{2\cdot{"+str(int(m))+"}}$"] = x2m
        table["$"+xTitle+"^{"+str(int(m))+"}$"] = xm
        index[3] = "$"+xTitle+"^{"+str(int(m))+"}$"
        index[5] = "$"+xTitle+"^{2\cdot{"+str(int(m))+"}}$"

        absxm = [ abs(xmElement) for xmElement in xm ]
        table["$|"+xTitle+"^{"+str(int(m))+"}|$"] = absxm
        index[4] = "$|"+xTitle+"^{"+str(int(m))+"}|$"

        yxm = [ self.yAxis[i] * xm[i] for i in range(len(xm)) ]
        table["$"+yTitle+""+xTitle+"^{"+str(int(m))+"}$"] = yxm
        index[6] = "$"+yTitle+""+xTitle+"^{"+str(int(m))+"}$"

        absxmDy = [absxm[i]*self.error[i] for i in range(len(absxm))]
        table["$|"+xTitle+"^{"+str(int(m))+"}|\Delta "+yTitle+"$"] = absxmDy
        index[7] = "$|"+xTitle+"^{"+str(int(m))+"}|\Delta "+yTitle+"$"

        table[index[5]].append(sum(x2m))
        table[index[6]].append(sum(yxm))
        table[index[7]].append(sum(absxmDy))

        saveLaTex(table, index, [0,1,2,3,4,5,6,7], path)

        a = sum(yxm)/sum(x2m)
        Da = sum(absxmDy)/sum(x2m)

        self.text = 'y = %s * x ^ %s' %(a, m) + '\n' + 'Error de a = %s' %(Da)

        return a , Da

    def generalFit(self, guess, function):

        from scipy.optimize import leastsq

        global x
        x = np.asarray(self.xAxis)
        y = np.asarray(self.yAxis)

        func = lambda t: eval(function) - y

        self.text = function

        parameters = leastsq(func, guess)[0]

        solution = ("\n" + "\t" + 't['+str(0)+']' + ': ' + "\t" +
                       "%g" %(parameters[0]) + "\t" + 't['+str(1)+']' + 
                                                  ': ' + "%g" %(parameters[1]))

        for i in range(1, len(parameters)/2):
            solution += ("\n" + '\t' + 't['+str(2*i)+']' + " : " + 
                        "%g" %(parameters[2*i]) + "\t" + 't['+str(2*i+1)+']' +
                         ': ' + '\t' + '\t' + "\t" + "%g" %(parameters[2*i+1]))

        self.text = self.text + solution

        return parameters

    def nodosChebyshev(self):

        n = 1000
        x = np.zeros(n+4)
        a = min(self.xAxis)
        b = max(self.xAxis)
        x[0] = b
        x[n+3] = a

        for i in range(1,n+2):
            xC = np.cos((2*i+1)*np.pi/(2*n+2))
            x[i] = (xC*(b-a)/2) + (b+a)/2

        return x
