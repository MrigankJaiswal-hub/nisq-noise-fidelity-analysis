from qiskit.quantum_info import state_fidelity

def compute_fidelity(ideal_state, noisy_state):
    return state_fidelity(ideal_state, noisy_state)
