# Theory Background

## Quantum Entanglement in NISQ Systems

Quantum entanglement is a non-classical correlation between quantum systems that enables advantages in computation, communication, and sensing. For bipartite systems, entanglement plays a crucial role in protocols such as quantum teleportation, superdense coding, and variational quantum algorithms.

Current quantum hardware operates in the **Noisy Intermediate-Scale Quantum (NISQ)** regime, where limited qubit counts and significant noise prevent full error correction. In this regime, entanglement is particularly fragile due to decoherence, gate imperfections, and measurement errors.

---

## Noise Processes in Quantum Circuits

Noise in quantum processors arises from interactions between qubits and their environment, as well as imperfect control operations. In this work, we consider:

- **Depolarizing Noise:** Randomly applies Pauli errors, modeling stochastic gate imperfections.
- **Amplitude Damping:** Represents energy relaxation processes characterized by finite \( T_1 \) times.
- **Measurement Noise:** Accounts for readout errors during final state measurement.

These noise models are commonly used to approximate realistic hardware behavior in superconducting and trapped-ion systems.

---

## Entanglement Quantification

To quantify entanglement degradation, we employ two widely accepted measures:

### Concurrence
Concurrence provides a normalized measure of two-qubit entanglement derived from the eigenvalues of the spin-flipped density matrix. It ranges from 0 (separable states) to 1 (maximally entangled states).

### Negativity
Negativity is based on the partial transposition of the density matrix and detects entanglement via the Peres–Horodecki criterion. It captures entanglement through the sum of negative eigenvalues of the partially transposed state.

Using both metrics provides complementary insight into entanglement robustness under noise.

---

## Error Mitigation via Zero-Noise Extrapolation

Zero-noise extrapolation (ZNE) is an error mitigation technique that estimates ideal expectation values by intentionally scaling noise levels and extrapolating results back to the zero-noise limit. Unlike full quantum error correction, ZNE is compatible with near-term hardware and does not require additional qubits.
