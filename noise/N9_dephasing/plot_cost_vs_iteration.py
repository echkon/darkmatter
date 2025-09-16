import pickle
import numpy as np
import matplotlib.pyplot as plt

# Variables
ansatz = "fullgraph9"
num_qubits = 9
num_layers = 2
lambs = [round(x, 4) for x in np.linspace(0.0, 1.0, 11)]
# lambs = lambs[0:1]
# lambs = lambs[1:6]
lambs = lambs[6:]

# Plot setup
fig, axes = plt.subplots(3, 2, figsize=(12, 12))
axes = axes.flatten()  # Flatten to easily loop

for idx, lamb in enumerate(lambs):
    # Load data
    with open(f'opt/N{num_qubits}_L{num_layers}_lamb{lamb}_costs.pkl', 'rb') as file:
        costs = pickle.load(file)
    with open(f'notopt/N{num_qubits}_L{num_layers}_lamb{lamb}_qb.pkl', 'rb') as file:
        notopt = pickle.load(file)
    
    num_steps = len(costs)
    iterations = list(range(num_steps))
    
    print(f"lamb={lamb} | opt={costs[-1]} | not opt={notopt}")

    # Plot in subplot
    ax = axes[idx]
    ax.plot(iterations, costs, label='dephasing, optimized')
    ax.plot(iterations, [notopt] * len(iterations), label='dephasing, not optimized', linestyle="--")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Cost")
    ax.set_title(f"lamb = {lamb}")
    ax.grid(True)
    ax.legend()

plt.tight_layout()
plt.savefig("../_figures/cost_vs_iteration.png", dpi=300, bbox_inches="tight", facecolor="white")
plt.savefig("../_figures/cost_vs_iteration.eps", format='eps', bbox_inches="tight", facecolor="white")
plt.show()
