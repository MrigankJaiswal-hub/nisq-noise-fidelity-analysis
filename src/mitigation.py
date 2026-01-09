import numpy as np

def zero_noise_extrapolation(noise_levels, observable_values):
    coeffs = np.polyfit(noise_levels, observable_values, deg=1)
    return coeffs[-1]  # extrapolated zero-noise value
