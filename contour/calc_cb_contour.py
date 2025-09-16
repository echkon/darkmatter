import pickle
import numpy as np
import os
import copy
from onecircuit import *
from concurrent.futures import ProcessPoolExecutor, as_completed

"""  
calc_qb_contour.py  
Computes the Quantum Cramér-Rao bound (QB) for different alpha and delta pairs
(4 qubits, fully connected graph ansatz, 1 layer).  
Saves the results in the folder qb_contour.  
"""  

## Check if sensor_file exists
sensor_file = "cb_fullgraph4/N4_L2_sensor.pkl"
if not os.path.exists(sensor_file):
    raise FileNotFoundError(f"Sensor file {sensor_file} not found.")

## Function to compute QB
def calc_qb(alpha, delta):
    with open(sensor_file, 'rb') as file:
        sensor = pickle.load(file)
    
    sensor_copy = copy.deepcopy(sensor)
    sensor_copy[1][2] = alpha
    sensor_copy[1][3] = [delta]
    
    cb = cls_bound(sensor_copy)
    print(f"alpha: {alpha}, delta: {delta}, CB: {cb}")

    return alpha, delta, cb

## Variables
alpha_list = np.linspace(0, np.pi, 100)
delta_list = np.logspace(-3, 0, 100)
results = []

## Process-based parallelism
with ProcessPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(calc_qb, alpha, delta) for alpha in alpha_list for delta in delta_list]

    for future in as_completed(futures):
        results.append(future.result())

## Save results
results.sort(key=lambda x: (x[0], x[1]))
with open('cb_contour/results.pkl', 'wb') as file:
    pickle.dump(results, file)
