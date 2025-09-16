import pickle
import numpy as np
import matplotlib.pyplot as plt

"""
Plots QB for different lambda values using the dephasing noise model
(4 qubits, 1 'preparation' layer, not optimized)
"""

# Load QBs (not optimized)
with open(f'data_a.pkl', 'rb') as file:
    qbs = pickle.load(file)

# Plot figure
fig, ax = plt.subplots(figsize=(5, 4))
lamb_list = np.linspace(0.0, 0.9, 10)
ax.plot(lamb_list, qbs, 'o-', linewidth=2)

ax.set_xlabel(r'$\lambda$', fontsize=12)
ax.set_ylabel("Quantum bound", fontsize=12)
ax.grid(True, ls="--", alpha=0.6)

plt.tight_layout()
plt.show()
