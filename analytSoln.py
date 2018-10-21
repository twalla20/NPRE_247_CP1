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


#Function initialization for analytical solution
#
#Args:
#	hL:	list containing half lives of all three nuclides
#	N0:	list containing initial number of nucleons for 
#		for each nuclide
#	tf:	total time elapsed
#
#Returns:
#	Nf: list containg NAf, NBf and NCf

def aSol(hL, N0, tf):
	"""
	Function initialization for analytical solution
	
	Args:
		hL:     list containing half lives of all three nuclides
		N0:     list containing initial number of nucleons for
			for each nuclide
		tf:     total time elapsed
		
	Returns:
		Nf: list containg NAf, NBf and NCf
	"""
	
#Creates list of decay constants
	L = dC(hL)
	
#Computes final number of parent nuclides
	NAf = eD(hL[0], N0[0], tf)
 
#Computes final number of 1st daughter nuclides
	NBf = eD(hL[1], N0[1], tf) + (L[0]*N0[0]*(math.exp(-L[0]*tf) - math.exp(-L[1]*tf)))/(L[1]-L[0])

#Computes final number of stable (2nd daughter) nuclides	
	NCf = N0[2] + N0[1]*(1 - math.exp(-L[1]*tf)) + (L[1]*(1 - math.exp(-L[0]*tf)) - L[0]*(1 - math.exp(-L[1]*tf)))*(N0[0]/(L[1]-L[0]))

	return [int(NAf), int(NBf), int(NCf)]

#End of analySoln function
