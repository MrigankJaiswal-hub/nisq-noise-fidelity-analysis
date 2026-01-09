from qiskit import QuantumCircuit

def bell_circuit(save_dm=False):
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)

    if save_dm:
        qc.save_density_matrix()

    return qc
