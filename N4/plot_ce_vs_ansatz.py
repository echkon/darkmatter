import pickle
import matplotlib.pyplot as plt
from onecircuit import *
from tqix.vqa.entanglement import concentratable_entanglement

"""
plot_ce_vs_ansatz.py
Plots the Quantum Cramér-Rao bound (QB) for different ansatz architectures,
and number of qubits (1 layer).
Determines which ansatz provides the best QB.
"""

# Variables
ansatz_list = ["ghz", "exc", "line", "ring", "star", "full"]
num_qubits = 4
ces = []

# Load QB
for ansatz in ansatz_list:
    if ansatz == "ghz" or ansatz == "exc":
        with open(f'qb_{ansatz}{num_qubits}/N{num_qubits}_sensor.pkl', 'rb') as file:
            sensor = pickle.load(file)
        sensor1 = sensor[0][0](sensor[0][1], sensor[0][2], sensor[0][3])
        ce = concentratable_entanglement(sensor1)
        ces.append(ce)
    else:
        with open(f'qb_{ansatz}graph{num_qubits}/N{num_qubits}_L1_sensor.pkl', 'rb') as file:
            sensor = pickle.load(file)
        sensor1 = sensor[0][0](sensor[0][1], sensor[0][2], sensor[0][3])
        ce = concentratable_entanglement(sensor1)
        ces.append(ce)
print(f"CEs = {ces}")

# Plot figure
x_positions = range(len(ansatz_list))
for i in range(len(ansatz_list)):
    plt.bar(x_positions[i], ces[i], label=f"{ansatz_list[i]}", width=0.4)
plt.xticks(x_positions, ansatz_list)
plt.xlabel("Configurations")
plt.ylabel("Concentratable entanglement")

# Save figure
plt.tight_layout()
plt.savefig(f"_figures/N{num_qubits}_ce_vs_ansatz.png", pad_inches=0.3, facecolor="white", bbox_inches="tight")
plt.savefig(f"_figures/N{num_qubits}_ce_vs_ansatz.eps", pad_inches=0.3, facecolor="white", bbox_inches="tight")

