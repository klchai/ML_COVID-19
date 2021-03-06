import numpy as np
import pandas as pd
from scipy.integrate import odeint
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

class SIRModel():
    """
    SIR Model
    """
    def __init__(self, beta=0.1, gamma=0.1):
        self.beta_ = beta
        self.gamma_ = gamma
 
    def deriv(self, y0, t, N, beta, gamma):
        S, I, R = y0
        dSdt = -beta * S * I / N
        dIdt = beta * S * I / N - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt
    
    def fit(self, t, N, I):
        I0 = I[0]
        y_0 = (N-I0, I0, 0)
        def f(t, beta, gamma):
            y_t = odeint(self.deriv, y_0, t, args=(N, beta, gamma))
            S,I,R = y_t.T # infected number
            return I
        params, pcov = curve_fit(f, t, I)
        return params
    
    def predict(self, t, old_t, N, I):
        b, g =self.fit(old_t, N, I)
        I0 = I[0]
        y0 = (N-I0, I0, 0)
        ret = odeint(self.deriv, y0, t, args=(N, b, g))
        S,I,R=ret.T
        return S,I,R
        
    def plotsir(self, t, S, I, R):
        f, ax = plt.subplots(1,1)
        ax.plot(t, S, 'b', alpha=0.7, linewidth=2, label='Susceptible')
        ax.plot(t, I, 'y', alpha=0.7, linewidth=2, label='Infected')
        ax.plot(t, R, 'g', alpha=0.7, linewidth=2, label='Recovered')
        ax.set_xlabel('Time (days)')
        ax.yaxis.set_tick_params(length=0)
        ax.xaxis.set_tick_params(length=0)
        legend = ax.legend()
        legend.get_frame().set_alpha(0.5)
        for spine in ('top', 'right', 'bottom', 'left'):
            ax.spines[spine].set_visible(False)
        plt.show()