import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

"""
plot_qb_vs_delta.py
Plots the Quantum Cramér-Rao bound (QB) for different delta
(4 qubits, fully connected graph ansatz, 1 layer).
Determines which delta provides the best QB.
"""

# Variables
delta_list = np.linspace(pow(10, -3), pow(10, 0), 100)

# Load QB
with open(f'qb_vs_delta/qbs.pkl', 'rb') as file:
    qbs = pickle.load(file)

# Plot figure
plt.plot(delta_list, qbs, label=f"fullgraph")
plt.title("QB vs Delta (4 Qubits, fullgraph, 1 Layer)")
plt.xlabel("Delta")

# Offset for y-axis
offset = min(qbs)
plt.ylabel(f"QB - {offset:.6f}")
ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x-offset:.1e}"))

plt.tick_params(axis='both', which='major')

# Save figure
plt.tight_layout()
plt.savefig(f"_figures/qb_vs_delta.png", pad_inches=0.3, facecolor="white", bbox_inches="tight")
plt.savefig(f"_figures/qb_vs_delta.eps", pad_inches=0.3, facecolor="white", bbox_inches="tight")

