from qiskit_aer import AerSimulator
from qiskit.quantum_info import DensityMatrix

def simulate_density_matrix(circuit, noise_model=None):
    sim = AerSimulator(noise_model=noise_model)
    result = sim.run(circuit).result()
    return DensityMatrix(result.data(0)["density_matrix"])
