import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mean, std):
    """Create gaussian distribution."""    
    return np.exp(-0.5 * ((x - mean)/std)**2) / (std * np.sqrt(2*np.pi))

phase = np.linspace(0.001, 0.1, 1000)
mean = 0.05
qb = 0.015654779006850635
var = qb
std = np.sqrt(var)
gaussian_dist = gaussian(phase, mean, std)

plt.figure()
plt.plot(phase, gaussian_dist)
plt.savefig("_figures/gaussian/gaussian.png")