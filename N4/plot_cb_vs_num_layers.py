import pickle
import matplotlib.pyplot as plt
from onecircuit import *

"""
plot_cb.py
Plots the Clasical Cramér-Rao bound (CB) for different number of
measurement layers (4 qubits, fully connected graph ansatz).
Determines which number of layers provides the best QB.
"""

# Variables
ansatz = "fullgraph4"
num_qubits = 4
num_prep_layers = 1
num_meas_layers_list = [1, 2, 3, 4]
cbs = []
qbs = []

# Load CB
for num_meas_layers in num_meas_layers_list:
    with open(f'cb_{ansatz}/N{num_qubits}_L{num_meas_layers}_sensor.pkl', 'rb') as file:
        sensor = pickle.load(file)
    cbs.append(cls_bound(sensor))
    qbs.append(sld_bound(sensor))
print(f"CBs = {cbs}")
print(f"QBs = {qbs}")

# Plot figure
fig, ax = plt.subplots(figsize=(4, 5), constrained_layout=True)
ax.plot(num_meas_layers_list, cbs, linestyle="--", color="#2ca02c", linewidth=3.0, label="CB")
ax.scatter(num_meas_layers_list, cbs, color="#2ca02c", zorder=5)
ax.plot(num_meas_layers_list, qbs, color="#1f77b4", linewidth=3.0, label="QB")
plt.xticks(num_meas_layers_list)
plt.ylim(1.5e-2, 2e-2)
plt.xlabel("L2")
plt.ylabel("Classical bound")
plt.legend()

# Save figure
plt.savefig("_figures/N4_cb_vs_num_layers.png", pad_inches=0.3, facecolor="white", bbox_inches="tight")
plt.savefig("_figures/N4_cb_vs_num_layers.eps", pad_inches=0.3, facecolor="white", bbox_inches="tight")
