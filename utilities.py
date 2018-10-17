#author@ twalla20
#
#This file will contain utilities such as the exponential decay method and
#the forward differencing solver.
#

import os
import numpy as np
import math


def expDecay(tH, N0, tf):
	"""Analytical model of exponential decay function.
	Args:
		tH:	half life of nuclide (hours)
		N0:	intial number of atoms
		tf:	final time (hours)
	Returns number of atoms at some final time tf.
	"""

	return N0*math.exp(-(math.log(2)*tf)/tH)

#end of expDecay


	 
