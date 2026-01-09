from qiskit.quantum_info import state_fidelity

def fidelity(dm, ideal_dm):
    return state_fidelity(dm, ideal_dm)
