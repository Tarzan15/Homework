# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 16:00:59 2017

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
    
def MercaBinomial(option, S, Rf, beta, sigma, T, N):
        H = T/N
        up = np.exp((Rf-beta)*H + sigma*(np.sqrt(H)))
        down = np.exp((Rf-beta)*H - sigma*(np.sqrt(H)))
        pu = (np.exp((Rf-beta)*H)-down)/(up-down)
        pd = 1 - pu
        discount = np.exp(-Rf * H)
        du = pu * discount
        dp = pd * discount
        numSteps = N
        numNodes = numSteps + 1
        spot_price = np.zeros(numNodes)
        payoff = no.zeros(numNodes)
        for i in range(numNodes):
            spot_price[i] = S * (up **(numSteps - i)) * (down**(i))
            payoff[i] = option.value(spot_price[i])
        for i in range ((numSteps - 1)), -1,-1):
            for j in range(i+1):
                payoff[j] = du * payoff[j] + dp * payoff[j+1]
                spot_price[j] = spot_price[j] / up
                payoff[j] = np.maximum(payoff[j], option.value(spot_price[j]))
        return payoff[0]
def main():
    P = 41
    K = 40
    Rf = 0.08
    T = 1
    N = 3
    beta = 0.0
    sigma = 0.30
    option = VanillaCallOption(K, T)
    callPrice = MercaBinomial(option, P, Rf, beta, sigma, T, N)
    print("The Mercan Binomial price is = {0:.4f}".format(callPrice))
main()
