import pickle
import matplotlib.pyplot as plt

"""
Plots the QB for different ansatz architectures 
(9 qubits, 1 'prepataion' layer).
"""

# Load QBs
with open(f'data_a.pkl', 'rb') as file:
    qbs = pickle.load(file)

# Plot figure
fig, ax = plt.subplots(figsize=(4, 5), constrained_layout=True)
ansatz_list = ["L9", "S9", "RS9", "F9"]
colors = ["#4d4080", "#0e6787", "#0e6787", "#449caa"]
x_positions = range(len(ansatz_list))
for i in range(len(ansatz_list)):
    plt.bar(x_positions[i], qbs[i], label=f"{ansatz_list[i]}", width=0.5, color=colors[i])

plt.xticks(x_positions, ansatz_list)
plt.xlabel("Configurations")
plt.ylabel("Quantum bound")
plt.tight_layout()
plt.show()
