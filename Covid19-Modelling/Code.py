import numpy as np
import matplotlib.pyplot as plt
from covid19_base import *

class Covid(Covid_base):

    def step(self): # Perform a single integration step
        super().step()
        INT_Pi = np.arange(1,len(self.Pi))
        Di = np.zeros(len(self.Pi)-1)
        Di[::1] = self.DI[self.pad + self.d-INT_Pi[::1]]*self.Pi[INT_Pi[::1]] #goes through the array to make Di by step 1 until the end of the array
        DI = sum(Di)
        self.DI[self.d + self.pad] = self.Rpar * DI * self.S[self.d]/self.Pop

        INT_Pr = np.arange(1,len(self.Pr))
        drd = np.zeros(len(self.Pr)-1)
        drd[::1] = self.DI[self.pad + self.d-INT_Pr[::1]]*self.Pi[INT_Pr[::1]]
        Drd = sum(drd)

        self.DR[self.d] = (1-self.Kf) * Drd
        self.DF[self.d] = self.Kf * Drd
        self.S[self.d+1] = self.S[self.d] - self.DI[self.pad + self.d]
        self.I[self.d+1] = self.I[self.d] + self.DI[self.pad + self.d] - (self.DR[self.d] + self.DF[self.d])
        self.R[self.d+1] = self.R[self.d] + self.DR[self.d]
        self.F[self.d+1] = self.F[self.d] + self.DF[self.d]
