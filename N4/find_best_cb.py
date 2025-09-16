import pickle
from onecircuit import *

"""
find_best_cb.py
Finds the best Clasical Cramér-Rao bound (CB) from random sensors saved in 
the cb_random folder, for a specified value of num_qubits, D, and M.
"""

# Variables
num_qubits = 4
D = 10
M = 2000

# Load CB
with open(f'cb_N{num_qubits}_random/N{num_qubits}_D{D}_M{M}_cbs.pkl', 'rb') as file:
    loaded_cbs = pickle.load(file)
with open(f'cb_N{num_qubits}_random/N{num_qubits}_D{D}_M{M}_sensors.pkl', 'rb') as file:
    loaded_sensors = pickle.load(file)

# Find best CB
best_cb = loaded_cbs[0]
best_index = 0
for i in range(1, len(loaded_cbs)):
    if loaded_cbs[i] < best_cb:
        best_cb = loaded_cbs[i]
        best_index = i
print(f"Best CB = {best_cb}")

# Display best circuit
best_sensor = loaded_sensors[best_index]
sensing = VariationalCircuit(best_sensor)
#sensing.print()

# Confirmation
#qb = sld_bound(best_sensor)
#cb = cls_bound(best_sensor)
#print(f"Confirmation: QB = {qb}, CB = {cb}")

# Save best QBs
with open(f'cb_N{num_qubits}_random/N{num_qubits}_D{D}_M{M}_best_cb_new.pkl', 'wb') as file:
    pickle.dump(best_cb, file)
with open(f'cb_N{num_qubits}_random/N{num_qubits}_D{D}_M{M}_best_sensor_new.pkl', 'wb') as file:
    pickle.dump(best_sensor, file)