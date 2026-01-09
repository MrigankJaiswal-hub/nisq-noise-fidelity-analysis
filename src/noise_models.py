from qiskit_aer.noise import NoiseModel, depolarizing_error, amplitude_damping_error

def depolarizing_noise(p):
    noise_model = NoiseModel()

    error_1q = depolarizing_error(p, 1)
    error_2q = depolarizing_error(p, 2)

    noise_model.add_all_qubit_quantum_error(error_1q, ['h'])
    noise_model.add_all_qubit_quantum_error(error_2q, ['cx'])

    return noise_model


def amplitude_damping_noise(p):
    noise_model = NoiseModel()

    error_1q = amplitude_damping_error(p)
    noise_model.add_all_qubit_quantum_error(error_1q, ['h', 'cx'])

    return noise_model
