from qiskit.quantum_info import concurrence, negativity

def compute_concurrence(density_matrix):
    return concurrence(density_matrix)

def compute_negativity(density_matrix):
    return negativity(density_matrix, qargs=[0])
