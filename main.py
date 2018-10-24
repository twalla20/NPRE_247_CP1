#author@ twalla20
#
#File used for main function that will run and plot solutions
#

# Imports
import matplotlib.pyplot as plt
import os
import math
import numpy as np
from forwardEuler import fwdEu
from forwardEuler import NA
from forwardEuler import NB
from forwardEuler import NC
from analytSoln import aSol

def solver(dt):
	"""
	Solves Three componemt decay chain analytically and numerically.
	Plots results and writes them to results.txt
	"""	

	hL = []
	N0 = []
	x = []
	file_in = open('parameters.txt', 'r')
	for y in file_in.read().split('\n'):
		if y.isdigit():
			hL.append(float(y))
        for y in file_in.read().split('\n'):
                if y.isdigit():
                        hL.append(float(y))
	tf = int(param.readline(7))
	param.close()
	
	N0A = N0.copy()
	rNA = fwdEu(tf, dt, 0, hL, N0A)
	N0B = N0.copy()
	rNB = fwdEu(tf, dt, 1, hL, N0B)
	N0C = N0.copy()
	rBC = fwdEu(tf, dt, 2, hL, N0C)

	t = np.arange(0,50,dt)
	plt.plot(t, rNA)
	plt.plot(t, rNB)
	plt.plot(t, rNC)
	plt.show()

#end

