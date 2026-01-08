# Noise & Fidelity Analysis of Quantum Circuits on NISQ Devices

## Overview
This project investigates how realistic noise affects quantum circuits by comparing
ideal simulations, noisy simulations, and executions on real IBM quantum hardware.

## Circuits Studied
- Bell state circuit
- GHZ state circuit

## Noise Models
- Depolarizing noise
- Amplitude damping noise

## Tools Used
- Python
- Qiskit
- IBM Quantum

## Key Results
- Fidelity decreases rapidly with circuit depth
- Hardware results show additional decoherence beyond simulated noise

## How to Run
pip install -r requirements.txt
jupyter notebook

## Future Work
- Error mitigation
- Classical shadow tomography
- Scaling to larger qubit systems
