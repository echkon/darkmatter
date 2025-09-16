import pickle
from onecircuit import *

# Variables
num_qubits = 4
alpha = 0
phase = [0.05]

# Prepare sensor
prep = [ghz_qc, num_qubits, [], []]
sens = [sensing_dm, num_qubits, alpha, phase]
sensor = [prep, sens]

# Calculate QB
num_steps = 200
sensing = VariationalCircuit(sensor)
sensing.print()
sensor,costs = sensing.fit(num_steps, cost_func=sld_bound, train_opt=[0])
qb = sld_bound(sensor)
print(qb)

# Save GHZ state
with open(f'qb_ghz4/N4_sensor.pkl', 'wb') as file:
    pickle.dump(sensor, file)
with open(f'qb_ghz4/N4_qb.pkl', 'wb') as file:
    pickle.dump(qb, file)