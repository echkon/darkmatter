import pickle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogFormatterMathtext, LogLocator, FormatStrFormatter

"""
Plots a contour plot of CB as a function of alpha and delta 
(4 qubits, F4 configuration, 1 layer).
"""

# Load CBs
with open('data_b.pkl', 'rb') as file:
    cbs = pickle.load(file)

# Reshape data into CB matrix
alphas, deltas, cbs = zip(*cbs)
alphas = np.array(alphas)
deltas = np.array(deltas)
cbs = np.array(cbs)

alpha_unique = np.unique(alphas)
delta_unique = np.unique(deltas)
cb_matrix = np.zeros((len(alpha_unique), len(delta_unique)))

for i, alpha in enumerate(alpha_unique):
    for j, delta in enumerate(delta_unique):
        cb_matrix[i, j] = cbs[(alphas == alpha) & (deltas == delta)][0]

# Plot contour (X = delta, Y = alpha)
fig, ax = plt.subplots(figsize=(4, 5), constrained_layout=True)
vmin, vmax = np.nanmin(cb_matrix), np.nanmax(cb_matrix)
contourf_ = ax.contourf(delta_unique, alpha_unique, cb_matrix, 400, vmin=vmin, vmax=vmax, cmap='viridis')
ax.set_xscale('log')
ax.set_xlabel(r'$\delta$', fontsize=14)
ax.set_ylabel(r'$\alpha$', fontsize=14, rotation=0, labelpad=15)
tick_values = np.logspace(np.log10(min(delta_unique)), np.log10(max(delta_unique)), num=7)
ax.set_xticks(tick_values)
ax.set_yticks([0, np.pi/2, np.pi])
ax.set_yticklabels([r'$0$', r'$\frac{\pi}{2}$', r'$\pi$'], fontsize=12)
cbar = fig.colorbar(contourf_, ax=ax, orientation='horizontal', pad=0.05, aspect=30, location='top')
ticks = np.linspace(vmin, vmax, 4)
cbar.set_ticks(ticks)
cbar.ax.tick_params(labelsize=10)
plt.show()
