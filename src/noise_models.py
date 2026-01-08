from qiskit_aer.noise import NoiseModel, depolarizing_error, amplitude_damping_error

def depolarizing_noise(p):
    noise_model = NoiseModel()
    error = depolarizing_error(p, 1)
    noise_model.add_all_qubit_quantum_error(error, ['h', 'cx'])
    return noise_model

def amplitude_damping_noise(gamma):
    noise_model = NoiseModel()
    error = amplitude_damping_error(gamma)
    noise_model.add_all_qubit_quantum_error(error, ['h', 'cx'])
    return noise_model
