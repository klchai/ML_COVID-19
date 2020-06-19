# coding: utf-8

import numpy as np

from .base import BaseModel


class SEIRDModel(BaseModel):

    def __init__(self, alpha:float=0.01, beta:float=0.1, delta:float=0.1, gamma:float=0.1, rho:float=0.5):
        super().__init__()
        self.alpha_ = alpha
        self.beta_ = beta
        self.delta_ = delta
        self.gamma_ = gamma
        self.rho_ = rho
    
    @property
    def params(self):
        return self.alpha_, self.beta_, self.delta_, self.gamma_, self.rho_

    @params.setter
    def params(self, new_params):
        self.alpha_, self.beta_, self.delta_, self.gamma_, self.rho_ = new_params

    def deriv(self, t, S, E, I, R, D, alpha, beta, delta, gamma, rho):
        N = S + E + I + R + D
        lambda_ = beta * I / N
        dS_dt = -lambda_ * S
        dE_dt = lambda_ * S - delta * E
        dI_dt = delta * E - (1-alpha) * gamma * I - alpha * rho * I
        dR_dt = gamma * I
        dD_dt = alpha * rho * I
        return dS_dt, dE_dt, dI_dt, dR_dt, dD_dt

    def fit(self, t, N, I, R, D):
        y = np.hstack((I, R, D))
        E0 = 1
        I0 = I[0]
        R0 = R[0]
        D0 = D[0]
        S0 = N - E0 - I0 - R0 - D0
        y_0 = (S0, E0, I0, R0, D0)
        def f(t, *params):
            y_t = self._predict(t, y_0, params)
            I_pred = y_t[2] # infected number
            R_pred = y_t[3] # recovered number
            D_pred = y_t[4] # dead number
            pred = np.hstack((I_pred, R_pred, D_pred))
            return pred
        self._curve_fit(f, t, y )
        return self
