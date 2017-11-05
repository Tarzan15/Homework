# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 14:09:31 2017

@author: JaceDonaldBroadbent
"""

import numpy as np
from scipy.stats import binom

class VanillaOption(object):
        def __init__(self, strike, expiry):
            self.strike = strike
            self.expiry = expiry
        def value(self,spot):
            pass
        
class VanillaCallOption(VanillaOption):
        def value(self, spot):
            max = np.maximum(spot - self.strike, 0.0)
            return max
class VanillaPutOption(VanillaOption):
    def value(self, spot):
        max = np.maximum(self.strike - spot, 0.0)
        return max
    
def EuropeanBinomial(option, S, Rf, beta, sigma, T, N):
        H = T/N
        up = np.exp((Rf-beta)*H + sigma*(np.sqrt(H)))
        down = np.exp((Rf-beta)*H - sigma*(np.sqrt(H)))
        pu = (np.exp((Rf-beta)*H)-down)/(up-down)
        pd = 1 - pu
        numSteps = N
        numNodes = numSteps + 1
        spotT = 0.0
        callT = 0.0
        for i in range(numNodes):
            spotT = S * (up ** (numSteps -i)) * (down ** (i))
            callT += option.value(spotT) * binom.pmf(numSteps -i, numSteps, pu)
        callPrice = callT * np.exp(-Rf * T)
        return callPrice
def main():
    P = 41
    K = 40
    Rf = 0.08
    T = 1
    N = 3
    beta = 0.0
    sigma = 0.30
    option = VanillaCallOption(K, T)
    callPrice = EuropeanBinomial(option, P, Rf, beta, sigma, T, N)
    print("The two Period European Binomial price is = {0:.4f}".format(callPrice))
main()


            