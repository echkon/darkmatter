import pickle
import numpy as np
import matplotlib.pyplot as plt

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

# Plot contour
fig, ax = plt.subplots(figsize=(4, 5), constrained_layout=True)
contourf_ = ax.contourf(alpha_unique, delta_unique, qb_matrix.T, 400, vmin=np.nanmin(qb_matrix), vmax=np.nanmax(qb_matrix))
cbar = fig.colorbar(contourf_)
plt.xscale("linear")
plt.yscale("log")
plt.xlabel("Alpha")
plt.ylabel("Delta")
plt.xticks(np.linspace(0, np.pi, 7), labels=['0', 'π/6', 'π/3', 'π/2', '2π/3', '5π/6', 'π'])

# Save figure
plt.tight_layout()
plt.savefig("_figures/qb_contour.png")
plt.savefig("_figures/qb_contour.eps")
