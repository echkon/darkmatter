import pickle
from onecircuit import *
import matplotlib.pyplot as plt
import io
import sys
import shutil

"""
print_circuit.py
Prints the quantum circuit for different 
number of qubits, network architectures, and number of layers.
Saves the results in the folder f"qb_N{num_qubits}_{ansatz}".
"""

# Set terminal width to a very large value
shutil.get_terminal_size = lambda: (10000, 100)  # 10,000 characters wide

# Variables
num_qubits = 9
num_layers = 1
phase = [0.05]  # phase[0]: delta.
alpha = 0

# Prepare the sensor
prep = [starringgraph9, num_qubits, num_layers, []]
sens = [sensing_dm, num_qubits, alpha, phase]
sensor = [prep, sens]

# Calculate QB
num_steps = 200
sensing = VariationalCircuit(sensor)
# sensing.print()

output_buffer = io.StringIO()
original_stdout = sys.stdout
sys.stdout = output_buffer

sensing.print()

sys.stdout = original_stdout

circuit_text = output_buffer.getvalue()
output_buffer.close()

# Adjusting the text for readability (we're keeping line breaks intact)
print(circuit_text)

# Determine text size dynamically
num_lines = circuit_text.count("\n") + 1  # Count lines
max_line_length = max(len(line) for line in circuit_text.split("\n"))  # Longest line

# Adjust figure size based on text size
fig_width = min(20, max(6, max_line_length * 0.15))  # Scale width
fig_height = min(30, max(6, num_lines * 0.5))  # Scale height

# Create a figure and add text
fig, ax = plt.subplots(figsize=(fig_width, fig_height))
ax.text(0.5, 0.5, circuit_text, fontsize=10, va='center', ha='center', family='monospace')

# Remove axes
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')

# Save as EPS
fig.savefig(f"print_qc.eps", format="eps", bbox_inches='tight')

print(f"Quantum circuit saved as print_qc.eps with size ({fig_width}, {fig_height})")
