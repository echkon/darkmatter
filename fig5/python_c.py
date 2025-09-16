import pickle
import matplotlib.pyplot as plt

"""
Plots the CB for different number of 'measurement' layers 
(9 qubits, F9 configuration, 2 'preparation' layers).
"""

# Load CBs
with open(f'data_c.pkl', 'rb') as file:
    cbs = pickle.load(file)

# Load QB
with open(f'data_b.pkl', 'rb') as file:
    qbs = pickle.load(file)
qb = qbs[1]  # QB for 2 'preparation' layers

# Plot figure
fig, ax = plt.subplots(figsize=(4, 5), constrained_layout=True)
num_meas_layers_list = [1, 2, 3]

ax.plot(num_meas_layers_list, cbs, linestyle="--", color="#2ca02c", linewidth=3.0, label="CB")
ax.scatter(num_meas_layers_list, cbs, color="#2ca02c", zorder=5)
ax.plot(num_meas_layers_list, [qb]*len(num_meas_layers_list), color="#1f77b4", linewidth=3.0, label="QB")
plt.xticks(num_meas_layers_list)
plt.xlabel("L2")
plt.ylabel("Classical bound")
plt.ylim(2e-3, 7e-3)
plt.legend()
plt.tight_layout()
plt.show()
