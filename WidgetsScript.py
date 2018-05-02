#########################################
#       Calculate the Hamiltonian       #
#########################################
#
#   Teacher's scrypt wrote in Java and translated
#       to python which calculate the hamiltonian
#       of a Central elastic potencial
#
#   Required floats: - mass\ m                               - initial radial speed \ vr
#                    - elastic constant \ k                  - initial angular speed \ vtheta
#                    - springy initial length \ l0           - shots \ n
#                    - initial radial coordenate \ r0        - time interval \ dt
#                    - initial angular coordenate \ theta0
#
#   Return: - The path of the CSV file with a table with the time, radius, angle
#                and Hamiltonian of the movement.
#
################################################################################################

def Hamiltonian(m, k, l0, r0, theta0, vr, vtheta, n, dt):

    dataT = []
    dataR = []
    dataTheta = []
    dataH = []

    t = 0.0
    pr0 = m*vr # initial radial moment
    ptheta0 = m*r0*r0*vtheta # initial angular moment
    h = ptheta0*ptheta0/(2.0*m*r0*r0)+pr0*pr0/(2.0*m)+(k/2.0)*(r0-l0)*(r0-l0)

    dataT.append(t)
    dataR.append(r0)
    dataTheta.append(theta0)
    dataH.append(h)

    for i in range(1,n):
        derR = pr0/m
        derTheta = ptheta0/(m*r0*r0)
        derPr = ptheta0*ptheta0/(m*r0*r0*r0)-k*(r0-l0)
        derPtheta = 0.0
        t = t+dt
        r = r0+dt*derR
        theta = theta0+dt*derTheta
        pr = pr0+dt*derPr
        ptheta = ptheta0+dt*derPtheta
        h = ptheta*ptheta/(2.0*m*r*r)+pr*pr/(2.0*m)+(k/2.0)*(r-l0)*(r-l0)

        dataT.append(t)
        dataR.append(r)
        dataTheta.append(theta)
        dataH.append(h)

        r0 = r
        theta0 = theta
        pr0 = pr
        ptheta0 = ptheta

    data = [dataT, dataR, dataTheta, dataH]
    names = ["$t/s$", "$r/cm$", "$\Theta/rad$", "$H/J$"]

    table = {names[i]:data[i] for i in range(len(data))}
    index = {i:names[i] for i in range(len(names))}

    return table, index


#########################################
#       Calculate the Error             #
#########################################
#
#   This function calculate the error of a magnitude 
#       from an equation which depends on others magnitudes
#       by its partials derivatives
#
#   Required: - symbols \ [str str]
#             - variables' values \ [floats]
#             - variables' error's values \  [floats]
#             - function \ str(function)
#
#   Return: - The result
#
#############################################################################################

def ErrorsCalculator(symbol, values, errors, function):

    from sympy import symbols, evalf, diff
    from math import (fabs, sqrt, log, exp, sin, pi, cos, tan, acos, asin,
                                                                      atan)

    symbol = symbol.split(' ')
    S = symbols(symbol)

    for n in range(len(S)):
        sElement = 'S['+str(n)+']'
        function = function.replace(symbol[n], sElement)

    function = eval(function)

    Error_sq = 0

    for i in range(len(symbol)):
        Error_sq += ((function.diff(symbol[i])*errors[i])**2)

    Error_re = 'Error_sq.evalf(subs={symbol[0]:values[0]'

    for x in range(1,len(symbol)):
        Error_re += ', symbol['+ str(x) + ']:values[' + str(x) + ']'
    Error_re += '})'

    Error_re = eval(Error_re)

    Error = sqrt(Error_re)

    return Error


#########################################
#       Calculate  the Derivative       #
#########################################
#
#   This function calculate the derivative dy/dx
#        using the approach (y2 - y1)/(x2 - x1) = dy/dx 
#
#   Required: - Columns values \ dict(table)
#             - Columns index \ dict(index)
#             - Indexes of the Columns you want to derivative \ list(columns)[y, x]
#
#   Return: - The new Columns values and Columns index with the changes
#                  if the class return 0 it means that it has been an error
#                return [table, index]
#
######################################################################################

def derivative(table, index, columns):
    y = table[index[columns[0]]]
    x = table[index[columns[1]]]

    derivative = [ (y[i+1]-y[i]) / (x[i+1]-x[i]) for i in xrange(len(x)-1) ]

    if not "Derivative" in table:
        table["Derivative"] = derivative
        index[max(index.keys())+1] = "Derivative"
    else:
        i = 1
        boolean = True
        while boolean:
            if not "Derivative "+str(i) in table:
                table["Derivative "+str(i)] = derivative
                index[max(index.keys())+1] = "Derivative "+str(i)
                boolean = False
            else:
                i = i+1
