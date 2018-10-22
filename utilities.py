#author@ twalla20
#
#This file will contain mathematical utilities used throughout the solutions
#

import os
import numpy as np
import math


def expDecay(hL, N0, tf):
	"""Model of exponential decay function.
	Args:
		hL:	half life of nuclide (hours)
		N0:	intial number of atoms
		tf:	final time (hours)
	Returns number of atoms at some final time tf.
	"""

	return N0*math.exp(-(math.log(2)*tf)/hL)

#end of expDecay function

def decayConst(halfLife):
	"""Converts array of half-lives to array of decay constants.
	Args:
		halfLife:	list of half lives
	Returns:
		a:		list of decay constants
	Index in array is number of daughter nuclide where 0 is parent nuclide.
	Returns 0 if it finds the half-life of a stable nuclide (0 hrs) in the argument list.
	"""
	if 0 in halfLife:
		return 0
	else:
		k = [math.log(2)/halfLife[i] for i in range(0, len(halfLife))]
		return k

#end of decay constant function	 
