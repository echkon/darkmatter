import pickle
import matplotlib.pyplot as plt
import os

"""
plot_qb_vs_num_layers.py
Plots the Quantum Cramér-Rao bound (QB) for different number of layers
(4 qubits, fully connected graph ansatz).
Determines which number of layers provides the best QB.
"""

# Variables
num_layers_list = [1, 2, 3, 4, 5, 6, 7]
qbs = []

# Load QB
for num_layers in num_layers_list:
    with open(f'qb_fullgraph4/N4_L{num_layers}_qb.pkl', 'rb') as file:
        qb = pickle.load(file)
    qbs.append(qb)
print(f"QBs = {qbs}")

# Plot figure
fig, ax = plt.subplots(figsize=(4, 5), constrained_layout=True)
bar_color = "#87CEEB"  # light blue
line_color = "#1f77b4"  # matplotlib default blue

ax.bar(num_layers_list, qbs, color=bar_color, width=0.4)
ax.plot(num_layers_list, qbs, color=line_color, linewidth=2.5)
ax.set_xticks(num_layers_list)
ax.set_ylim(0.015, 0.0167)
ax.set_xlabel(r"$L_1$")
ax.set_ylabel("Quantum bound")
ax.text(1.1, 0.01635, "F4 configuration", color="brown", fontsize=10)

# Save figure
os.makedirs("_figures", exist_ok=True)
plt.tight_layout()
plt.savefig("_figures/N4_qb_vs_num_layers.png", dpi=300, bbox_inches="tight", facecolor="white")
plt.savefig("_figures/N4_qb_vs_num_layers.eps", format='eps', bbox_inches="tight", facecolor="white")
