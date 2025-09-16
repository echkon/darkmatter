import pickle
from onecircuit import *
from concurrent.futures import ProcessPoolExecutor, as_completed
import csv, ast

"""
calc_cb_random.py
Computes the Classical Cramér-Rao bound (QB) for N, D, and M.
(random ansatz, number of qubits N=4, D=10, M=2000).
Saves the results in the folder f"cb_random".
"""

# Functions
def load_cnot_pairs(file_path):
    positions = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            converted_row = [ast.literal_eval(val) for val in row]
            positions.append(converted_row)
    return positions

def calc_cb(i, num_qubits, cnot_pairs, phase):
    # Prepare sensor
    with open(f'qb_N{num_qubits}_fullgraph/N{num_qubits}_L{num_prep_layers}_sensor.pkl', 'rb') as file:
        sensor = pickle.load(file)
    sensor_copy = sensor.copy()
    meas = [random_ansatz, num_qubits, cnot_pairs[i], []]
    sensor_copy.append(meas)

    # Calculate CB
    num_steps = 200
    sensing = VariationalCircuit(sensor_copy)
    sensing.print()
    sensor_copy, _ = sensing.fit(num_steps, cost_func=cls_bound, train_opt=[2])
    cb = cls_bound(sensor_copy)
    print(cb)
    
    return sensor_copy, cb

# Variables
num_qubits = 4
num_prep_layers = 1
phase = [0.05]  # phase[0]: delta
alpha = 0
D = 10
M = 20000
sensors = []
cbs = []

# Process-based parallelism
folder_path = f"../random_ansatz/cnot_pairs_N{num_qubits}"
cnot_pairs = load_cnot_pairs(f"{folder_path}/cnot_pairs_N{num_qubits}_D{D}_M{M}.csv")

with ProcessPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(calc_cb, i, num_qubits, cnot_pairs, phase) for i in range(M)]

    for future in as_completed(futures):
        sensor, cb = future.result()
        print(cb)
        sensors.append(sensor)
        cbs.append(cb)

# Save QB
with open(f'cb_N{num_qubits}_random/N{num_qubits}_D{D}_M{M}_cbs.pkl', 'wb') as file:
    pickle.dump(cbs, file)
with open(f'cb_{num_qubits}_random/N{num_qubits}_D{D}_M{M}_sensors.pkl', 'wb') as file:
    pickle.dump(sensors, file)
