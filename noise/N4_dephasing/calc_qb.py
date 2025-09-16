import numpy as np
import pickle
from onecircuit import *
from multiprocessing import Pool

ansatz = "fullgraph4"
num_qubits = 4
num_layers = 1
phase = [0.05]  # phase[0]: delta.
alpha = 0
num_steps = 15
time = 1.0
# lambs = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
# lambs = [round(x, 4) for x in np.logspace(-4, 0, 100)]
lambs = [round(x, 4) for x in np.linspace(0.0001, 1.0, 100)]

def run_experiment(lamb):
    y = lamb2y(time, lamb)

    # Load sensor
    with open(f'opt/N{num_qubits}_L{num_layers}_lamb0.0_sensor.pkl', 'rb') as file:
        loaded_sensor = pickle.load(file)
    prep = loaded_sensor[0]
    sens = [sensing_dm, num_qubits, alpha, phase]
    nois = [dephasing_qc, num_qubits, time, y]
    sensor = [prep, sens, nois]

    # Run variational circuit
    sensing = VariationalCircuit(sensor)
    sensor, costs = sensing.fit(num_steps, cost_func=sld_bound, train_opt=[0], learning_rate = 1.0e-6)

    # Calculate QB
    qb = sld_bound(sensor)

    # Save results
    with open(f'opt/N{num_qubits}_L{num_layers}_lamb{lamb}_qb.pkl', 'wb') as file:
        pickle.dump(qb, file)
    with open(f'opt/N{num_qubits}_L{num_layers}_lamb{lamb}_sensor.pkl', 'wb') as file:
        pickle.dump(sensor, file)
    with open(f'opt/N{num_qubits}_L{num_layers}_lamb{lamb}_costs.pkl', 'wb') as file:
        pickle.dump(costs, file)

    return qb

if __name__ == "__main__":
    with Pool(processes=1) as pool:
        results = pool.map(run_experiment, lambs)
