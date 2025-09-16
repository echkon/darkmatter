from onecircuit import *
import numpy as np
import matplotlib.pyplot as plt
import pickle
import os

# Load sensor data
with open(f'../N4/cb_fullgraph4/N4_L2_sensor.pkl', 'rb') as file:
    sensor = pickle.load(file)
num_qubits = sensor[1][1]
true_phase = sensor[1][3][0]

num_k_list = [100, 500, 1000]
phase = np.linspace(0.001, 0.1, 100)
posterior_data = {}

# Load posteriors
for num_k in num_k_list:
    with open(f'k{num_k}/posterior.pkl', 'rb') as file:
        posterior = pickle.load(file)
    
    # Normalize the posterior
    posterior = np.array(posterior)
    posterior /= np.sum(posterior)
    
    posterior_data[num_k] = (phase, posterior)
    
# Plot posterior analysis
fig, ax = plt.subplots(figsize=(5, 5), constrained_layout=True)
for num_k in num_k_list:
    phase, posterior = posterior_data[num_k]
    ax.plot(phase, posterior, label=f'Posterior (k={num_k})', alpha=0.7)

ax.axvline(true_phase, color='red', linestyle='--', label='True Phase')
plt.grid()
plt.xlabel("Phase")
plt.ylabel("Posterior Probability")
plt.legend()
plt.tight_layout()
plt.savefig("_figures/dm/posterior.png", dpi=300)
plt.savefig("_figures/dm/posterior.eps", format='eps')

# Plot scaling analysis
with open(f'k{num_k}/bias_list.pkl', 'rb') as file:
    bias_list = pickle.load(file)
with open(f'k{num_k}/var_list.pkl', 'rb') as file:
    var_list = pickle.load(file)

num_k_list = list(range(1, len(bias_list)+1))
qb = sld_bound(sensor)
cb = cls_bound(sensor)
qb_list = []
cb_list = []
for idx in range(len(num_k_list)):
    qb_list.append(qb/num_k_list[idx])
    cb_list.append(cb/num_k_list[idx])

fig, axs = plt.subplots(2, 1, figsize=(8, 10), sharex=True)
axs[0].plot(num_k_list, bias_list, label="BIAS")
axs[0].set_ylabel('Bias')
axs[1].set_xscale("log")
axs[0].grid(True)

axs[1].plot(num_k_list, var_list, label="VAR")
axs[1].plot(num_k_list, qb_list, label="QB")
axs[1].plot(num_k_list, cb_list, label="CB")
axs[1].set_xlabel('Number of measurements, num_k')
axs[1].set_ylabel('Variance')
axs[1].set_xscale("log")
axs[1].set_yscale("log")
axs[1].grid(True)
axs[1].legend()

plt.tight_layout()
os.makedirs("_figures/dm", exist_ok=True)
plt.savefig("_figures/dm/bias_var.png", dpi=300)
plt.savefig("_figures/dm/bias_var.eps", format='eps')
