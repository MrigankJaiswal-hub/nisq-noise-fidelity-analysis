# Experimental Methodology

## Circuit Design

We study a standard two-qubit Bell-state preparation circuit consisting of:
1. A Hadamard gate applied to the first qubit
2. A controlled-NOT (CNOT) gate entangling the qubits

This circuit ideally produces the maximally entangled Bell state:
\[
|\Phi^+\rangle = \frac{1}{\sqrt{2}} (|00\rangle + |11\rangle)
\]

---

## Simulation Framework

All simulations are performed using density-matrix evolution to accurately capture decoherence effects. This approach avoids statistical fluctuations associated with finite-shot sampling and enables direct computation of entanglement measures.

Noise channels are applied after each gate operation to emulate realistic hardware behavior.

---

## Noise Parameter Sweeps

Noise strength is systematically varied over a defined range to simulate increasing hardware imperfections. For each noise value:
- Multiple independent noise realizations are simulated
- Entanglement metrics are averaged
- Statistical uncertainty is estimated using standard deviation

---

## Hardware-Inspired Noise Models

Two classes of noise models are considered:

- **IBM-like Superconducting Noise:** Higher two-qubit gate error rates and shorter coherence times
- **IonQ-like Trapped-Ion Noise:** Lower gate error rates and longer coherence times

These models are parameterized using representative calibration values reported by each platform.

---

## Error Mitigation Procedure

Zero-noise extrapolation is implemented by scaling gate noise through circuit folding. Linear extrapolation is then used to estimate the zero-noise entanglement value.
