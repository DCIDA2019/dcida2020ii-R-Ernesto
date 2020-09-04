import numpy as np

def solveWithEulerVectorized(periodsNumber,Period,stepsNumber,stepSize,a,y_0,z_0):
    x = np.linspace(0,periodsNumber*Period,stepsNumber) #creating an array
    y = np.zeros(stepsNumber,dtype='float')
    y[0]=y_0
    z = np.zeros(stepsNumber,dtype='float')
    z[0]=z_0

    for i in range(1,stepsNumber):
        y[i] = y[i-1] + stepSize*z[i-1] # theta actualization
        z[i] = z[i-1] - stepSize*a*y[i-1] # phi actualization

    return x,y
