#author@ twalla20
#
#This file contants the method for solving the decay chain alaytically.
#

#Imports

import os
import numpy as np
import math
from utilities import expDecay as expDecay
from utilities import lamda as lamda


#Class initialization for solution
#
#Args:
#	halflife:	array size 3 containing half lives of all three nuclides
#	initNum:	array size 3 containing initial number of nucleons for 
#			for each nuclide
#	tf:		total time elapsed
#
#Returns:
#	atoms: array size 3 containg NAf, NBf and NCf

Class AnalytDecaySolution:

	def __init__(self, halfLife, initNum, tf):
		lamda = lamda(halfLife)
		
		

	return atoms
