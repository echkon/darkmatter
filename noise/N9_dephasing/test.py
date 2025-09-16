import pickle

with open(f'N9_L2_sensor.pkl', 'rb') as file:
    loaded_sensor = pickle.load(file)
prep = loaded_sensor[0]

print(prep)