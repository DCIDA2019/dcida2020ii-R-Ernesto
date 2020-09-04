import argparse # package to introduce commmands via terminal
from math import sqrt, pi # useful functions
import numpy as np 
import eulerVectorized # a modula implementation
from matplotlib import pyplot as plt

# comand line parameters parsing
parser = argparse.ArgumentParser(description='Simple pendulum EOM solver for small angles.')
parser.add_argument("--length",default=1,help="Length of the rope in meters, default is 1.")
parser.add_argument("--periods",default=1,help="Number of periods to compute, default is 1.")
parser.add_argument("--figname",default='figure.png',help="Name of the figure to be generated, default is figure.")


# parameters definition
args = parser.parse_args() 
l = float(args.length) # given trough command line
periods = int(args.periods) # given trough command line
g = 9.8
a = g/l
omega = sqrt(a)
T =2*pi/omega
stepsNumber = 10000
theta_0 = 8.73e-2
Dtheta_t0 = 0.1
stepSize = periods*T/stepsNumber

# numerical method
t, theta = eulerVectorized.solveWithEulerVectorized(periods,T,stepsNumber,stepSize,a,theta_0,Dtheta_t0)
theta_real = theta_0*np.cos(omega*t)

# plotting the solution
sol_figure = plt.figure(figsize=[3*1.5,2.5*1.5],dpi=150)
plt.plot(t,theta,':',label='Numerical')
plt.plot(t,theta_real,label='Analitical')
plt.legend()
plt.ylabel("$\\theta$ [rads]")
plt.xlabel("time [s]")
plt.title("Solution")
#plt.show()
sol_figure.savefig(args.figname)

# saving the figure
print("Plot saved on "+args.figname+" \n")


