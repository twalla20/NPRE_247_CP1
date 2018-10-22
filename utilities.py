#author@ twalla20
#
#This file will contain mathematical utilities used throughout the solutions
#

import os
import numpy as np
import math


def expDecay(L, N0, tf):
	"""Model of exponential decay function.
	Args:
		L:	decay constant of nuclide
		N0:	intial number of atoms
		tf:	final time (hours)
	Returns number of atoms at some final time tf.
	"""

	return N0*math.exp(-L*tf)

#end of expDecay function

def decayConst(hL):
	"""Converts array of half-lives to array of decay constants.
	Args:
		hL:		list of half lives
	Returns:
		a:		list of decay constants
	Index in array is number of daughter nuclide where 0 is parent nuclide.
	Removes index if the half-life is zero (stable).
	"""
	k = [math.log(2)/hL[i] for i in range(0, len(hL)) if (int(hL[i])!=0)]
	return k

#end of decay constant function	 
