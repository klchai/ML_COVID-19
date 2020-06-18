# coding: utf-8

import numpy as np

from .base import BaseModel
from scipy.integrate import odeint

class SEIRModel(BaseModel):
    """
    Blabla sur SEIR model
    
    TODO : equations

    """
    def __init__(self, beta=0.1, delta=0.1, gamma=0.1):
        super().__init__()
        self.beta_ = beta
        self.delta_ = delta
        self.gamma_ = gamma
    
    @property
    def params(self):
        return self.beta_, self.delta_, self.gamma_

    @params.setter
    def params(self, new_params):
        self.beta_, self.delta_, self.gamma_ = new_params
    
    def deriv(self, t, S, E, I, R, beta, delta, gamma):
        N = S + E + I + R
        lambda_ = beta * I / N
        dS_dt = -lambda_ * S
        dE_dt = lambda_ * S - delta * E
        dI_dt = delta * E - gamma * I
        dR_dt = gamma * I
        return dS_dt, dE_dt, dI_dt, dR_dt

    def fit(self, t, N, I, R=None):
        if R is None:
            return self.fit_NI(t, N, I)
        else:
            return self.fit_NIR(t, N, I, R)

    def fit_NIR(self, t, N, I, R):
        y = np.hstack((I, R))
        I0 = I[0]
        y_0 = (N-I0, 1, I0, 0)
        def f(t, *params):
            y_t = self._predict(t, y_0, params)
            I_pred = y_t[2] # infected number
            R_pred = y_t[3] # recovered number
            pred = np.hstack((I_pred, R_pred))
            return pred
        self._curve_fit(f, t, y)
        return self

    def fit_NI(self, t, N, I):
        I0 = I[0]
        y_0 = (N-I0, 1, I0, 0)
        def f(t, beta, delta, gamma):
            y_t = self._predict(t, y_0, (beta, delta, gamma))
            I_pred = y_t[2] # infected number
            return I_pred
        self._curve_fit(f, t, I)
        return self
