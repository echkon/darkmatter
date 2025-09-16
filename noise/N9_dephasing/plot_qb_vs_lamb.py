import pickle
import numpy as np
import matplotlib.pyplot as plt
import os

"""
plot_qb_vs_lamb.py
Plots the Quantum Cramér-Rao bound (QB) for different lambda
"""

# Variables
ansatz = "fullgraph9"
num_qubits = 9
num_layers = 2
lamb_list = [round(x, 4) for x in np.linspace(0.0, 1.0, 11)]
# lamb_list = [round(x, 4) for x in np.linspace(0.0001, 1.0, 100)]
qbs_N9_dephasing_notopt = []
qbs_N9_dephasing = []

# Load QB
for lamb in lamb_list:
    with open(f'notopt/N{num_qubits}_L{num_layers}_lamb{lamb}_qb.pkl', 'rb') as file:
        qb_N9_dephasing_notopt = pickle.load(file)
    with open(f'opt/N{num_qubits}_L{num_layers}_lamb{lamb}_qb.pkl', 'rb') as file:
        qb_N9_dephasing = pickle.load(file)
    qbs_N9_dephasing_notopt.append(qb_N9_dephasing_notopt)
    qbs_N9_dephasing.append(qb_N9_dephasing)

# Plot figure
plt.figure(figsize=(6, 6))
ax = plt.gca()
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plot for N=4, dephasing (optimized)
ax.plot(lamb_list, qbs_N9_dephasing,
         label="dephasing, optimized",
         color=colors[0], # First color from your list
         linewidth=2.0,
         linestyle="--",
         marker='o',
         markersize=7,
         fillstyle='full',
         zorder=1)

# Plot for N=4, dephasing (not optimized)
ax.plot(lamb_list, qbs_N9_dephasing_notopt,
         label="dephasing, not optimized",
         color=colors[1], # Second color from your list
         linewidth=2.0,
         linestyle="--",
         marker='o',
         markersize=7,
         fillstyle='full',
         zorder=2) # Higher zorder to ensure it's on top if overlapping

ax.set_xscale('log')
ax.set_xlabel(r"$\lambda$", fontsize=14)
ax.set_ylabel("Quantum bound", fontsize=14)
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)
ax.yaxis.offsetText.set_fontsize(14)
ax.legend(prop={'size': 14}, loc='center left', bbox_to_anchor=(0.1, 0.6667))
ax.grid(True, which="both", ls="--", c='0.7') # Dashed grid, light gray

# Save figure
plt.savefig("../_figures/N9_dephasing.png", dpi=300, bbox_inches="tight", facecolor="white")
plt.savefig("../_figures/N9_dephasing.eps", format='eps', bbox_inches="tight", facecolor="white")
