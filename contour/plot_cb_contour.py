import pickle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogFormatterMathtext, LogLocator, FormatStrFormatter

# Load results
with open('qb_contour/results.pkl', 'rb') as file:
    results = pickle.load(file)
alphas, deltas, qbs = zip(*results)
alphas = np.array(alphas)
deltas = np.array(deltas)
qbs = np.array(qbs)

# Reshape data into QB matrix
alpha_unique = np.unique(alphas)
delta_unique = np.unique(deltas)
qb_matrix = np.zeros((len(alpha_unique), len(delta_unique)))

for i, alpha in enumerate(alpha_unique):
    for j, delta in enumerate(delta_unique):
        qb_matrix[i, j] = qbs[(alphas == alpha) & (deltas == delta)][0]

# Plot contour (X = delta, Y = alpha)
fig, ax = plt.subplots(figsize=(4, 5), constrained_layout=True)
vmin, vmax = np.nanmin(qb_matrix), np.nanmax(qb_matrix)
contourf_ = ax.contourf(delta_unique, alpha_unique, qb_matrix, 400, vmin=vmin, vmax=vmax, cmap='viridis')

# Axis settings
ax.set_xscale('log')
ax.set_xlabel(r'$\delta$', fontsize=14)
ax.set_ylabel(r'$\alpha$', fontsize=14, rotation=0, labelpad=15)

# Set x-axis log scale with manually defined ticks
tick_values = np.logspace(np.log10(min(delta_unique)), np.log10(max(delta_unique)), num=7)
ax.set_xticks(tick_values)

# Format y-axis with 4 decimal places (since it's linear, no need for log formatting)
ax.set_yticks([0, np.pi/2, np.pi])
ax.set_yticklabels([r'$0$', r'$\frac{\pi}{2}$', r'$\pi$'], fontsize=12)

# Colorbar at the top with 4 ticks
cbar = fig.colorbar(contourf_, ax=ax, orientation='horizontal', pad=0.05, aspect=30, location='top')
ticks = np.linspace(vmin, vmax, 4)
cbar.set_ticks(ticks)
cbar.ax.tick_params(labelsize=10)

# Save figure
plt.savefig("_figures/qb_contour.png", dpi=300)
plt.savefig("_figures/qb_contour.eps")
