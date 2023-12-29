```python
# quantum_computing.py

from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from config import OPEN_API_KEY

# Set your Open API Key
qiskit.IBMQ.save_account(OPEN_API_KEY)

# Load your Open API Key
qiskit.IBMQ.load_account()

# Get the least busy quantum computer
provider = IBMQ.get_provider(hub='ibm-q')
quantum_computer = provider.get_backend('ibmq_qasm_simulator')

def create_quantum_circuit(n_qubits):
    """
    Function to create a quantum circuit with n qubits
    """
    qc = QuantumCircuit(n_qubits)
    return qc

def apply_hadamard(qc, qubit):
    """
    Function to apply a Hadamard gate to a specific qubit in a quantum circuit
    """
    qc.h(qubit)
    return qc

def apply_cnot(qc, control_qubit, target_qubit):
    """
    Function to apply a CNOT gate to a specific control and target qubit in a quantum circuit
    """
    qc.cx(control_qubit, target_qubit)
    return qc

def measure_qubits(qc):
    """
    Function to measure all qubits in a quantum circuit
    """
    qc.measure_all()
    return qc

def run_circuit(qc):
    """
    Function to run a quantum circuit and return the results
    """
    transpiled_qc = transpile(qc, quantum_computer)
    qobj = assemble(transpiled_qc, quantum_computer)
    result = execute(qobj, quantum_computer).result()
    return result
```
