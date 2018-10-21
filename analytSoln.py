#author@ twalla20
#
#This file contants the method for solving the decay chain alaytically.
#

#Imports

import os
import numpy as np
import math
from utilities import expDecay as eD
from utilities import decayConst as dC


#Module initialization for analytical solution
#
#Args:
#	hL:	array containing half lives of all three nuclides
#	N0:	array containing initial number of nucleons for 
#			for each nuclide
#	tf:		total time elapsed
#
#Returns:
#	atoms: array containg NAf, NBf and NCf

def analytSoln(hL, N0, tf):
	atoms = []
	lambda = dC(hL)
	
#Appends list with final number of parent nuclides
	atoms.append(eD(hL[0]), N0[0], tf)
 
#Appends list with final number of 1st daughter nuclides
	Nd1 = eD(hL[1]) + (lambda[0]*N0[0]*(math.exp(-lambda[0]*tf) - math.exp(-lambda[1]*tf)))/(lambda[1]-lambda[0])
	atoms.append(Nd1)

#Appends list with final number of stable daughter nuclides	
	Nd2 = N0[2] + N0[1](1 - math.exp(-lambda[1]*tf)) + (N0[0]*(lambda[1]*(1 - math.exp(-lambda[0]*tf)) - lambda[0]*(1 - math.exp(-lambda[1]*tf)))/(lambda[1] - lambda[0])
	atoms.append(Nd2)

	return atoms

#End of analySoln module
