# Observations and Discussion

## Entanglement Degradation Trends

Both concurrence and negativity exhibit monotonic decay as noise strength increases. This behavior is consistent with theoretical expectations for depolarizing and amplitude-damping channels.

Concurrence shows slightly higher sensitivity to noise compared to negativity, particularly at intermediate noise strengths, indicating differing robustness between entanglement measures.

---

## Hardware Comparison

Superconducting-inspired noise models exhibit faster entanglement degradation compared to trapped-ion-inspired models. This trend is primarily attributed to higher two-qubit gate error rates in superconducting architectures.

Trapped-ion models preserve entanglement over a broader noise range, reflecting the benefit of longer coherence times despite slower gate execution.

---

## Effectiveness of Error Mitigation

Zero-noise extrapolation improves estimated entanglement values at low-to-moderate noise strengths. However, mitigation effectiveness diminishes at higher noise levels, where nonlinear error accumulation limits extrapolation accuracy.

This observation highlights the practical limitations of error mitigation techniques in deeply noisy regimes.

---

## Limitations and Practical Implications

The simulations rely on simplified, uncorrelated noise models and do not capture temporal drift, crosstalk, or pulse-level control errors. Despite these limitations, the results capture dominant noise mechanisms and provide actionable insight for hardware-aware algorithm design in NISQ devices.
