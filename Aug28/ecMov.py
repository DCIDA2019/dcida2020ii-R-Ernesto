import argparse
from math import sqrt, pi
import numpy as np
import eulerVectorized
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser(description='Simple pendulum EOM solver for small angles.')
parser.add_argument("--length",default=1,help="Length of the rope in meters, default is 1.")
parser.add_argument("--periods",default=1,help="Number of periods to compute, default is 1.")
parser.add_argument("--figname",default='figure.png',help="Name of the figure to be generated, default is figure.")

args = parser.parse_args()
l = float(args.length)
periods = int(args.periods)
g = 9.8
a = g/l
omega = sqrt(a)
T =2*pi/omega

stepsNumber = 10000
theta_0 = 8.73e-2
Dtheta_t0 = 0.1
stepSize = periods*T/stepsNumber

t, theta = eulerVectorized.solveWithEulerVectorized(periods,T,stepsNumber,stepSize,a,theta_0,Dtheta_t0)
theta_real = theta_0*np.cos(omega*t)

sol_figure = plt.figure(figsize=[3*1.5,2.5*1.5],dpi=150)
plt.plot(t,theta,':',label='Numerical')
plt.plot(t,theta_real,label='Analitical')
plt.legend()
plt.ylabel("$\\theta$ [rads]")
plt.xlabel("time [s]")
plt.title("Solutions: Old School vs New School")
#plt.show()
sol_figure.savefig(args.figname)

print("Plot saved on "+args.figname+" \n")


