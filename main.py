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
fromm analytSol import aSol

def solver(dt):
	"""
	Solves Three componemt decay chain analytically and numerically.
	Plots results and writes them to results file
	param = open("params.txt", "r")
        hL = [param.readline(1), param.readline(2), param.readline(3)]
        N0 = [param.readline(4), param.readline(5), param.readline(6)]
        tf = param.readline(7)
        param.close()
	
	N0A = N0.copy()
	rNA = fwdEu(tf, dt, 0, hL, N0A)
	N0B = N0.copy()
	rNB = fwdEu(tf, dt, 1, hL, N0B)
	N0C = N0.copy()
	rBC = fwdEu(tf, dt, 2, hL, N0C)

	



