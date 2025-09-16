import os
import pickle
from onecircuit import *
import numpy as np
from concurrent.futures import ProcessPoolExecutor, as_completed

"""
calc_qb_vs_alpha.py
Computes the Quantum Cramér-Rao bound (QB) for different alpha
(4 qubits, fullgraph, 1 layer).
Saves the results in the folder qb_vs_alpha.
"""

## Check if sensor_file exists
sensor_file = "qb_fullgraph4/N4_L1_sensor.pkl"
if not os.path.exists(sensor_file):
    raise FileNotFoundError(f"Sensor file {sensor_file} not found.")

# Variables
alpha_list = np.linspace(0, np.pi, 100)
qbs = []

# Calculate QB
with open(sensor_file, 'rb') as file:
    sensor = pickle.load(file)

for alpha in alpha_list:
    sensor_copy = copy.deepcopy(sensor)
    sensor_copy[1][2] = alpha

    qb = sld_bound(sensor_copy)
    print(f"alpha: {alpha}, QB: {qb}")

    qbs.append(qb)

# Save results
with open(f'qb_vs_alpha/qbs.pkl', 'wb') as file:
    pickle.dump(qbs, file)
