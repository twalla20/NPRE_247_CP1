#author@ twalla20
#
# Module holds the Forward Euler's method for the numerical solution
#

# Imports
import math
import numpy as np
from utilities import expDecay as eD
from utilities import decayConst as dC


def fwdEu(tf, dt, tp, hL, N0):
	"""
	First Order ODE solver function using Forward Eurler's method for numerical solution

	Args:
		
	"""
	if dt <= 0:
		return [0]
	L = dC(hL)
	n = round(tf/dt)
	atoms = [N0[tp]]
	y = N0[tp]
	x = 0
	if tp==0:
		for i in range(n):
			s = dt * NA(L, N0, x)
			N0[0] += s
			N0[1] -= s
			y += dt * s
			x +=  dt * (n+1)
			atoms.append(y)

	if tp==1:
		for i in range(n):
			k = NB(L, N0, x)
			N0[1] += dt * k[0]
			N0[2] += dt * k[1]
			y += dt * (k[0]+k[1])
			x +=  dt * (n+1)
			atoms.append(y)

	if tp==2:
		for i in range(n):
			o = NC(L, N0, x)
			N0[0] += dt * o[1]
			N0[1] -= dt * o[1]
			N0[2] += dt * o[0]
			y += dt * o[0]
			x +=  dt * (n+1)
			atoms.append(y)
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
	b = L[0]*eD(L[0], N0[0], x)
	return [round(a), round(b)]
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
	h = round(-L[0] * eD(L[0], N0[0], x))
	a = L[1]*(eD(L[1], N0[1], x) + (L[0]*N0[0]*(math.exp(-L[0]*x) - math.exp(-L[1]*x)))/(L[1]-L[0]))
	return [round(a), round(h)]
# end of stable daughter function
