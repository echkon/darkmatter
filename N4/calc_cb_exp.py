import pickle
from onecircuit import *

"""
calc_cb_exp.py
Computes the Classical Cramér-Rao bound (QB) for different 
number of qubits, network architectures, number of
preparation layers, and number of measurement layers.
Saves the results in the folder f"cb_{ansatz}".
"""

# Variables
ansatz = "fullgraph4"
num_qubits = 4
num_prep_layers = 1
num_meas_layers = 1
phase = [0.05]  # phase[0]: delta
alpha = 0

# Prepare sensor
with open(f'qb_{ansatz}/N{num_qubits}_L{num_prep_layers}_sensor.pkl', 'rb') as file:
    sensor = pickle.load(file)
sensor_copy = sensor.copy()
meas = [fullgraph_inv, num_qubits, num_meas_layers, []]
sensor_copy.append(meas)

# Calculate CB
num_steps = 200
sensing = VariationalCircuit(sensor_copy)
sensing.print()
sensor_copy, _ = sensing.fit(num_steps, cost_func=cls_bound, train_opt=[2])
cb = cls_bound(sensor_copy)
print(cb)

# Save CB
with open(f'cb_{ansatz}_exp/N{num_qubits}_L{num_meas_layers}_cb.pkl', 'wb') as file:
    pickle.dump(cb, file)
with open(f'cb_{ansatz}_exp/N{num_qubits}_L{num_meas_layers}_sensor.pkl', 'wb') as file:
    pickle.dump(sensor_copy, file)
