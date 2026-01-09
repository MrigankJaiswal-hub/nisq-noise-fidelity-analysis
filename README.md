# NISQ Noise & Entanglement Fidelity Analysis ⚛️

A research-grade quantum computing project analyzing how **noise degrades entanglement** in NISQ-era quantum devices, with **hardware-inspired noise models** and **error mitigation**.

---

## 📌 Project Overview

This project studies the robustness of quantum entanglement under realistic noise using a Bell state as a test system. We analyze:

- Ideal vs noisy entanglement
- Concurrence and Negativity degradation
- Hardware-inspired noise (IBM vs IonQ)
- Error mitigation using Zero-Noise Extrapolation (ZNE)

All simulations are performed using **Qiskit Aer**.

---

## 🧪 Methodology

### 1️⃣ Ideal Bell State
- Constructed a 2-qubit Bell state
- Verified analytically using state fidelity

### 2️⃣ Noise Modeling
- Depolarizing noise
- Thermal relaxation (IBM-like)
- Global depolarization (IonQ-like)

### 3️⃣ Entanglement Measures
- **Concurrence**
- **Negativity** (partial transpose method)

### 4️⃣ Error Mitigation
- Zero-Noise Extrapolation (noise amplification + linear extrapolation)

---

## 📊 Key Results

### Ideal vs Noisy Entanglement

| Measure      | Ideal | Noisy |
|-------------|-------|-------|
| Concurrence | ~1.0  | ~0.76 |
| Negativity  | ~0.5  | ~0.38 |

✔ Negativity ≈ ½ Concurrence (theoretically consistent)

---

### Entanglement vs Noise Strength

- Both concurrence and negativity decay monotonically
- Concurrence degrades faster than negativity
- Confirms known entanglement robustness hierarchy

---

### Hardware Comparison

| Backend | Concurrence |
|-------|------------|
| IBM-like (Superconducting) | Lower |
| IonQ-like (Trapped Ion) | Higher |

✔ Trapped-ion noise preserves entanglement better

---

### Error Mitigation (ZNE)

- Noise amplified by circuit folding
- Linear extrapolation recovers lost entanglement
- Demonstrates real mitigation (not post-selection)

---

## 📁 Repository Structure

nisq-noise-fidelity-analysis/
│
├── notebooks/
│   ├── 01_ideal_circuits.ipynb
│   ├── 02_noise_models.ipynb
│   ├── 03_zero_noise_extrapolation.ipynb
│   ├── 04_entanglement_metrics.ipynb
│
│
├── src/
├── circuits.py
├── noise_models.py
├── simulation.py
├── fidelity_metrics.py
├── entanglement.py
├── mitigation.py
└── utils.py
│
├── results/
│   ├── concurrence_vs_noise.png
│   ├── negativity_vs_noise.png
│   └── hardware_comparison.png
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore




---

## 🚀 Getting Started

### Environment Setup
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
