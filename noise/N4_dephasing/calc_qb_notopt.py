import numpy as np
import pickle
from onecircuit import *

# Variables
ansatz = "fullgraph4"
num_qubits = 4
num_layers = 1
phase = [0.05]  # phase[0]: delta.
alpha = 0
time = 1.0
# lambs = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
# lambs = np.linspace(0.01, 1.0, 100)
# lambs = np.linspace(1.0e-4, 1.0e-2, 100)
lambs = [round(x, 4) for x in np.linspace(0.0001, 1.0, 100)]
# lambs = [round(x, 4) for x in np.logspace(-4, 0, 100)]

for lamb in lambs:
    y = lamb2y(time, lamb)

    # Prepare sensor
    with open(f'opt/N{num_qubits}_L{num_layers}_lamb0.0_sensor.pkl', 'rb') as file:
        loaded_sensor = pickle.load(file)
    prep = loaded_sensor[0]
    sens = [sensing_dm, num_qubits, alpha, phase]
    nois = [dephasing_qc, num_qubits, time, y]
    sensor = [prep, sens, nois]

    # Calculate QB
    qb = sld_bound(sensor)
    print(qb)

    # Save results
    with open(f'notopt/N{num_qubits}_L{num_layers}_lamb{lamb}_qb.pkl', 'wb') as file:
        pickle.dump(qb, file)
    with open(f'notopt/N{num_qubits}_L{num_layers}_lamb{lamb}_sensor.pkl', 'wb') as file:
        pickle.dump(sensor, file)
