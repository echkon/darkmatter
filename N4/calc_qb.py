import pickle
from onecircuit import *

"""
calc_qb.py
Computes the Quantum Cramér-Rao bound (QB) for different 
number of qubits, network architectures, and number of layers.
Saves the results in the folder f"qb_{ansatz}".
"""

# Variables
ansatz = "stargraph4"
num_qubits = 4
num_layers = 1
phase = [0.05]  # phase[0]: delta.
alpha = 0

# Prepare sensor
prep = [stargraph, num_qubits, num_layers, []]
sens = [sensing_dm, num_qubits, alpha, phase]
sensor = [prep, sens]

# Calculate QB
num_steps = 200
sensing = VariationalCircuit(sensor)
sensing.print()
sensor,costs = sensing.fit(num_steps, cost_func=sld_bound, train_opt=[0])
qb = sld_bound(sensor)
print(qb)

# Save results
with open(f'qb_{ansatz}/N{num_qubits}_L{num_layers}_qb.pkl', 'wb') as file:
    pickle.dump(qb, file)
with open(f'qb_{ansatz}/N{num_qubits}_L{num_layers}_sensor.pkl', 'wb') as file:
    pickle.dump(sensor, file)
