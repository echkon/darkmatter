import pickle
import matplotlib.pyplot as plt

"""
Plots the CB for different number of 'measurement' layers 
(4 qubits, F4 configuration, 1 'preparation' layer).
"""

# Load CBs
with open(f'data_a.pkl', 'rb') as file:
    cbs = pickle.load(file)

# Load QB
with open(f'../fig2/data_b.pkl', 'rb') as file:
    qbs = pickle.load(file)
qb = qbs[0]  # QB for 1 'preparation' layer

# Plot figure
fig, ax = plt.subplots(figsize=(4, 5), constrained_layout=True)
num_meas_layers_list = [1, 2, 3, 4]

ax.plot(num_meas_layers_list, cbs, linestyle="--", color="#2ca02c", linewidth=3.0, label="CB")
ax.scatter(num_meas_layers_list, cbs, color="#2ca02c", zorder=5)
ax.plot(num_meas_layers_list, [qb]*len(num_meas_layers_list), color="#1f77b4", linewidth=3.0, label="QB")
plt.xticks(num_meas_layers_list)
plt.ylim(1.5e-2, 2e-2)
ax.set_xlabel("L2")
plt.ylabel("Classical bound")
plt.legend()
plt.tight_layout()
plt.show()
