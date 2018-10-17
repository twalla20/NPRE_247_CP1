#author@ twalla20
#
#This file will contain utilities such as the exponential decay method and
#the forward differencing solver.
#

import os
import numpy as np
import math


def expDecay(tH, N0, tf):
	"""Model of exponential decay function.
	Args:
		tH:	half life of nuclide (hours)
		N0:	intial number of atoms
		tf:	final time (hours)
	Returns number of atoms at some final time tf.
	"""

	return N0*math.exp(-(math.log(2)*tf)/tH)

#end of expDecay module

def decayConst(halfLife):
	"""Converts array of half-lives to array of decay constants.
	Args:
		halfLife:	list of half lives
	Returns:
		a:		list of decay constants
	Index in array is number of daughter nuclide where 0 is parent nuclide.
	"""

	a = halfLife[:]
#	for x in np.nditer(a,'readwrite'):
#		x[...] = (math.log(2))/x
	return a

#end of lambda module	 
