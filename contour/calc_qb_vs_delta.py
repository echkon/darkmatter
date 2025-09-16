import pickle
from onecircuit import *
import numpy as np
from concurrent.futures import ProcessPoolExecutor, as_completed

"""
calc_qb_vs_delta.py
Computes the Quantum Cramér-Rao bound (QB) for different delta
(4 qubits, fully connected graph ansatz, 3 layers).
Saves the results in the folder qb_vs_delta.
"""

# Functions
def calc_qb(num_qubits, num_layers, alpha, phase):
    
    # Prepare the sensor
    prep = [fullgraph, num_qubits, num_layers, []]
    sens = [sensing_dm, num_qubits, alpha, phase]
    sensor = [prep, sens]

    # Calculate QB
    num_steps = 200
    sensing = VariationalCircuit(sensor)
    sensing.print()
    sensor, _ = sensing.fit(num_steps, cost_func=sld_bound, train_opt=[0])
    qb = sld_bound(sensor)
    print(qb)

    return qb

# Variables
ansatz = "fullgraph4"  # best ansatz
num_qubits = 4
num_layers = 1  # best num_layers
alpha = 0
qbs = []

# Convert delta to the format required for the 'sensing_dm' function
delta_list = np.linspace(pow(10, -3), pow(10, 0), 100)
phase_list = []
for i in range(len(delta_list)):
    phase_list.append([delta_list[i]])

# Process-based parallelism
with ProcessPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(calc_qb, num_qubits, num_layers, alpha, phase) for phase in phase_list]
    
    for future in as_completed(futures):
        qb = future.result()
        qbs.append(qb)

# Save results
with open(f'qb_vs_delta/qbs.pkl', 'wb') as file:
    pickle.dump(qbs, file)
