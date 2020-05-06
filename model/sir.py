import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class SIRModel():
    
    def __init__(self, beta_init=0.2,gamma_init=1./10):
        self.beta_0 = beta_init
        self.gamma_0 = gamma_init
        self.beta_ = None
        self.gamma_ = None
        self.N = 67e6 # Total population in France

    def deriv(self,y, t, N, beta, gamma):
        S, I, R = y
        dSdt = -beta * S * I / N
        dIdt = beta * S * I / N - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt

    def fit(self,x,y):
        return self

    def predict(self,t):
        # Initial number of infected and recovered individuals, I0 and R0.
        I0, R0 = 1, 0
        # Everyone else, S0, is susceptible to infection initially.
        S0 = self.N - I0 - R0
        # Initial conditions vector
        y0 = S0, I0, R0
        # Integrate the SIR equations over the time grid, t.
        ret = odeint(self.deriv,y0,t,args=(self.N, self.beta_0,self.gamma_0))
        S, I, R = ret.T
        return S, I, R

def plot_curves(sir):
    # A grid of time points (in days)
    t = np.linspace(0,365)
    S,I,R = sir.predict(t)
    fig = plt.figure(facecolor='w')
    ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
    ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
    ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
    ax.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
    ax.set_xlabel('Time /days')
    ax.set_ylabel('Number (1000s)')
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    for spine in ('top', 'right', 'bottom', 'left'):
        ax.spines[spine].set_visible(False)
    plt.show()
        
if __name__=="__main__":
    sir=SIRModel().fit(0,0)
    plot_curves(sir)
