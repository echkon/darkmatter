import pickle
import numpy as np
import matplotlib.pyplot as plt

# Variables
ansatz = "fullgraph4"
num_qubits = 4
num_layers = 1
lamb=0.002
with open(f'opt/N{num_qubits}_L{num_layers}_lamb{lamb}_costs.pkl', 'rb') as file:
    costs = pickle.load(file)
with open(f'notopt/N{num_qubits}_L{num_layers}_lamb{lamb}_qb.pkl', 'rb') as file:
    notopt = pickle.load(file)
num_steps = len(costs)
iterations = list(range(0, num_steps))

print("opt", costs[-1])
print("not opt", notopt)

# Plot figures
plt.figure(figsize=(8, 5))
plt.plot(iterations, costs, label=f'dephasing, optimized')
plt.plot(iterations, [notopt]*len(iterations), label=f'dephasing, not optimized', linestyle="--")
plt.xlabel("Iteration")
plt.ylabel("Cost")
plt.title(f"Costs vs Iterations (lambda={lamb})")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save figure
plt.savefig("../_figures/cost_vs_iteration.png", dpi=300, bbox_inches="tight", facecolor="white")
plt.savefig("../_figures/cost_vs_iteration.eps", format='eps', bbox_inches="tight", facecolor="white")