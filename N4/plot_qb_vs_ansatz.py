import pickle
import matplotlib.pyplot as plt

"""
plot_qb_vs_ansatz.py
Plots the Quantum Cramér-Rao bound (QB) for different ansatz architectures,
and number of qubits (1 layer).
Determines which ansatz provides the best QB.
"""

# Variables
ansatz_list = ["ghz", "exc", "line", "ring", "star", "full"]
num_qubits = 4
qbs = []

# Load QB
for ansatz in ansatz_list:
    if ansatz == "ghz" or ansatz == "exc":
        with open(f'qb_{ansatz}4/N{num_qubits}_qb.pkl', 'rb') as file:
            qb = pickle.load(file)
        qbs.append(qb)
    else:
        with open(f'qb_{ansatz}graph4/N{num_qubits}_L1_qb.pkl', 'rb') as file:
            qb = pickle.load(file)
        qbs.append(qb)
print(f"QBs = {qbs}")

# Plot figure
x_positions = range(len(ansatz_list))
for i in range(len(ansatz_list)):
    plt.bar(x_positions[i], qbs[i], label=f"{ansatz_list[i]}", width=0.4)
plt.xticks(x_positions, ansatz_list)
plt.xlabel("Configurations")
plt.ylabel("Quantum bound")

# Save figure
plt.tight_layout()
plt.savefig(f"_figures/N4_qb_vs_ansatz.png", pad_inches=0.3, facecolor="white", bbox_inches="tight")
plt.savefig(f"_figures/N4_qb_vs_ansatz.eps", pad_inches=0.3, facecolor="white", bbox_inches="tight")

