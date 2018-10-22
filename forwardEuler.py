#author@ twalla20
#
# Module holds the Forward Euler's method for the numerical solution
#

# Imports
import math
import numpy as np
import matplotlib 
import pyplot as plt
from utilities import expDecay as eD
from utilities import decayConst as dC


def fwdEu(f, tf, hL, N0, dt, i):
	"""
	First Order ODE solver function using Forward Eurler's method for numerical solution

	Args:
		
	"""
	atoms = [] 
	L = dC(hL)
	n = tf/dt
	y = N0[i]
	x = 0
	for j in range(n):
		y += dt * f(L, N0, x)
		atoms.append(y)
		x += dt * n
	return atoms
# end of Forward Euler's method

def NA(L, N0, x):
	"""
	First Order ODE function for parent nuclide decay
	
	Args:
		L:	list of decay constants
		N0:	list of intial number of nuclides
		x:	current time position on x-axis
	
	Returns:
		NA'(x)
	"""
	return round(-L[0] * eD(L[0], N0[0], x))
# end of parent function

def NB(L, N0, x):
	"""
        First Order ODE function for 1st daughter 
	nuclide decay/production

        Args:
                L:      list of decay constants
                N0:     list of intial number of nuclides
                x:      current time position on x-axis

        Returns:
                NB'(x)
        """
	a = -L[1]*(eD(L[1], N0[1], x) + (L[0]*N0[0]*(math.exp(-L[0]*x) - math.exp(-L[1]*x)))/(L[1]-L[0]))
	b = L[0]*eD(L[0], No[0], x)
	return round(a+b)
# end of first daughter function

def NC(L, N0, x):
	"""
        First Order ODE function for 2nd daughter 
	(stable) nuclide production

        Args:
                L:      list of decay constants
                N0:     list of intial number of nuclides
                x:      current time position on x-axis

        Returns:
                NC'(x)
        """
	a = L[1]*(eD(L[1], N0[1], x) + (L[0]*N0[0]*(math.exp(-L[0]*x) - math.exp(-L[1]*x)))/(L[1]-L[0]))
	return round(a)
# end of stable daughter function
