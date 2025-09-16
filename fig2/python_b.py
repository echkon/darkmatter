import pickle
import matplotlib.pyplot as plt

"""
Plots the QB for different number of 'preparation' layers 
(4 qubits, F4 configuration).
"""

# Load QBs
with open(f'data_b.pkl', 'rb') as file:
    qbs = pickle.load(file)

# Plot figure
fig, ax = plt.subplots(figsize=(4, 5), constrained_layout=True)
num_layers_list = [1, 2, 3, 4, 5, 6, 7]
bar_color = "#76c5d6"
line_color = "#1f77b4"

ax.bar(num_layers_list, qbs, color=bar_color, width=0.5)
ax.plot(num_layers_list, qbs, color=line_color, linewidth=2.5)
ax.set_xticks(num_layers_list)
ax.set_ylim(0.015, 0.0167)
ax.set_xlabel("L1")
ax.set_ylabel("Quantum bound")
plt.tight_layout()
plt.show()
