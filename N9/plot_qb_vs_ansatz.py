import pickle
import matplotlib.pyplot as plt

"""
plot_qb_vs_ansatz.py
Plots the Quantum Cramér-Rao bound (QB) for different ansatz architectures
and number of qubits (1 layer).
Determines which ansatz provides the best QB.
"""

# Variables
ansatz_list = ["L9", "S9", "SR9", "F9"]
qbs = []

# Load QB
for ansatz in ansatz_list:
    if ansatz == "L9":
        with open(f'qb_linegraph9/N9_L1_qb.pkl', 'rb') as file:
            qb = pickle.load(file)
    elif ansatz == "S9":
        with open(f'qb_stargraph9/N9_L1_qb.pkl', 'rb') as file:
            qb = pickle.load(file)
    elif ansatz == "SR9":
        with open(f'qb_starringgraph9/N9_L1_qb.pkl', 'rb') as file:
            qb = pickle.load(file)
    elif ansatz == "F9":
        with open(f'qb_fullgraph9/N9_L1_qb.pkl', 'rb') as file:
            qb = pickle.load(file)
    else:
        raise ValueError("Ansatz not found.")
    qbs.append(qb)
print(f"QBs = {qbs}")

# Plot figure
fig, ax = plt.subplots(figsize=(4, 5), constrained_layout=True)
x_positions = range(len(ansatz_list))
colors = ["#45367c", "#006c8e", "#00939d", "#3aa3a3"]
for i in range(len(ansatz_list)):
    ax.bar(x_positions[i], qbs[i], label=f"{ansatz_list[i]}", color=colors[i], width=0.4)
plt.xticks(x_positions, ansatz_list)
plt.xlabel("Ansatz")
plt.ylabel("QB")

# Save figure
plt.tight_layout()
plt.savefig(f"_figures/N9_qb_vs_ansatz.png", pad_inches=0.3, facecolor="white")
plt.savefig(f"_figures/N9_qb_vs_ansatz.eps", pad_inches=0.3, facecolor="white")
