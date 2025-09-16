import pickle
import numpy as np
import matplotlib.pyplot as plt

"""
plot_qb_vs_alpha.py
Plots the Quantum Cramér-Rao bound (QB) for different alpha
(fully connected graph ansatz, 4 qubits, 1 layer).
Determines which alpha provides the best QB.
"""

# Variables
alphas = np.linspace(0, np.pi, 100)

# Load QB
with open(f'qb_vs_alpha/qbs.pkl', 'rb') as file:
    qbs = pickle.load(file)

# Plot figure
plt.plot(alphas, qbs)
plt.title("QB vs Alpha (N=4, fullgraph, L=1)")
plt.xlabel("Alpha")
plt.ylabel("QB")
plt.xticks(np.linspace(0, np.pi, 7), labels=['0', 'π/6', 'π/3', 'π/2', '2π/3', '5π/6', 'π'])


# Save figure
plt.tight_layout()
plt.savefig(f"_figures/qb_vs_alpha.png")
plt.savefig(f"_figures/qb_vs_alpha.eps")

