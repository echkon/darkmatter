import pickle
import numpy as np
import matplotlib.pyplot as plt

"""
plot_combined_results.py

Plots posterior distributions, bias, and variance from Bayesian estimation
(4 qubits, F4 configuration, 1 layer).
"""

# Load data
with open("data.pkl", "rb") as file:
    data = pickle.load(file)

phase = data["phase"]
num_k_list = data["num_k_list"]
data_posterior = data["posterior"]
data_bias = data["bias"]
data_variance = data["variance"]

# (a) Posterior distributions
fig, ax = plt.subplots(figsize=(6, 4))
for i, num_k in enumerate(num_k_list):
    ax.plot(phase, data_posterior[i], label=f"k={num_k}", linewidth=2)
true_phase = 0.05
ax.axvline(true_phase, color="red", linestyle="--", label="True phase", linewidth=2)

ax.set_xlabel("Phase")
ax.set_ylabel("Posterior Probability")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

# (b) Bias
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(range(1, len(data_bias) + 1), data_bias, label="Bias", linewidth=2)

ax.set_xlabel("Number of measurements, k")
ax.set_ylabel("Bias")
ax.set_xscale("log")
ax.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

# (c) Variance
with open("../fig3/data_a.pkl", "rb") as file:
    cbs = pickle.load(file)
cb = cbs[1]  # CB for 2 'measurement' layers
with open("../fig2/data_b.pkl", "rb") as file:
    qbs = pickle.load(file)
qb = qbs[0]  # QB for 1 'preparation' layer

# Generate arrays of 1000 values
k_values = np.arange(1, 1001)
cbs = cb / k_values
qbs = qb / k_values

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(range(1, len(data_variance) + 1), cbs, label="CB/k", linewidth=2, linestyle="dashed")
ax.plot(range(1, len(data_variance) + 1), qbs, label="QB/k", linewidth=2)
ax.plot(range(1, len(data_variance) + 1), data_variance, label="Variance", linewidth=2)

ax.set_xlabel("Number of measurements, k")
ax.set_ylabel("Variance")
ax.set_xscale("log")
ax.set_yscale("log")
ax.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()