from onecircuit import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import os
import pickle

def likelihood(phase, k):
    sensor[1][3][0] = phase
    circuit_qc = QuantumCircuit(sensor)
    probs = QuantumMeasurement(circuit_qc)
    return probs[k] if 0 <= k < len(probs) else 0

def bayesian_update(phase_list, k, prior):
    P_k_given_phase = [likelihood(phase, k) for phase in phase_list]
    posterior = np.array(P_k_given_phase) * prior
    return posterior

def stat_properties(f, x, true_phase):
    mean = x @ f / np.sum(f)
    bias = mean - true_phase
    var = ((mean - x) ** 2) @ f / np.sum(f)
    std = np.sqrt(var)
    return mean, bias, var, std

def gaussian(x, mean, std):
    return np.exp(-0.5 * ((x - mean) / std) ** 2) / (std * np.sqrt(2 * np.pi))

# Load sensor
with open(f'../N4/cb_fullgraph4/N4_L2_sensor.pkl', 'rb') as file:
    sensor = pickle.load(file)

num_qubits = sensor[1][1]
true_phase = sensor[1][3][0]
phase = np.linspace(0.001, 0.1, 100)
prior = norm.pdf(phase, scale=1, loc=0)
prior /= np.trapz(prior, phase)

num_k_total = 1000
checkpoints = [100, 500, 1000]

# Sample outcomes based on likelihood
probs = [likelihood(true_phase, k) for k in range(2 ** num_qubits)]
probs = np.array(probs) / np.sum(probs)
k_values = np.random.choice(list(range(2 ** num_qubits)), num_k_total, p=probs).tolist()

bias_list = []
var_list = []

for i, k in enumerate(k_values, start=1):
    posterior = bayesian_update(phase, k, prior)
    posterior /= np.trapz(posterior, phase)
    mean, bias, var, std = stat_properties(posterior, phase, true_phase)
    bias_list.append(bias)
    var_list.append(var)
    prior = posterior.copy()

    if i in checkpoints:
        output_dir = f"k{i}"
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "posterior.pkl"), "wb") as file:
            pickle.dump(posterior, file)
        with open(os.path.join(output_dir, "bias_list.pkl"), "wb") as file:
            pickle.dump(bias_list.copy(), file)
        with open(os.path.join(output_dir, "var_list.pkl"), "wb") as file:
            pickle.dump(var_list.copy(), file)
        with open(os.path.join(output_dir, "k_values.pkl"), "wb") as file:
            pickle.dump(k_values[:i], file)

        print(f"\nCheckpoint saved at num_k = {i}")
        print("Mean:", mean)
        print("Variance:", var)
        print("Standard deviation:", std)
        print("True phase:", true_phase)
        print("QB:", sld_bound(sensor))
        print("CB:", cls_bound(sensor) )
