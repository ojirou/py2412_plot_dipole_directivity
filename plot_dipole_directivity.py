import matplotlib.pyplot as plt
import numpy as np
def HW_dipole_np(theta):
    return np.abs(np.cos((np.pi/2.0)*np.cos(theta))/np.sin(theta))
def to_dBi(d_real, dBi=2.15):
    PdBm=10*np.log(1000*np.power(d_real,2)/(120*np.pi))
    Pmax=np.max(PdBm)
    return PdBm+(dBi-Pmax)
def plotd(theta,d):
    ax=plt.subplot(111, projection="polar")
    ax.plot(theta, d)
    plt.show()
if __name__=="__main__":
    theta=np.arange(0.01, 2*np.pi, 0.01)
    D=HW_dipole_np(theta)
    plotd(theta, D)
    plotd(theta, to_dBi(D))