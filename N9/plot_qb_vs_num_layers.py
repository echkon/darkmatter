import pickle
import matplotlib.pyplot as plt

"""
plot_qb_vs_num_layers.py
Plots the Quantum Cramér-Rao bound (QB) for different number of layers
(4 qubits, fully connected graph ansatz).
Determines which number of layers provides the best QB.
"""

# Variables
ansatz = "fullgraph9"
num_qubits = 9
num_layers_list = [1, 2, 3]
qbs = []

# Load QB
for num_layers in num_layers_list:
    with open(f'qb_{ansatz}/N9_L{num_layers}_qb.pkl', 'rb') as file:
        qb = pickle.load(file)
    qbs.append(qb)
print(qbs)

# Plot figure
fig, ax = plt.subplots(figsize=(4, 5), constrained_layout=True)
bar_color = "#3aa3a3"
line_color = "#1f77b4"  # matplotlib default blue

ax.bar(num_layers_list, qbs, color=bar_color, width=0.4)
ax.plot(num_layers_list, qbs, color=line_color, linewidth=2.5)
plt.xticks(num_layers_list)
ax.set_xlabel(r"$L_1$")
ax.set_ylabel("Quantum bound")
plt.ylabel("QB")

# Save figure
plt.tight_layout()
plt.savefig("_figures/N9_qb_vs_num_layers.png", pad_inches=0.3, facecolor="white")
plt.savefig("_figures/N9_qb_vs_num_layers.eps", pad_inches=0.3, facecolor="white")
