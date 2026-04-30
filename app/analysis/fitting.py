import numpy as np
from scipy.optimize import curve_fit

def gaussian(x, a, x0, sigma):
    return a * np.exp(-(x - x0)**2 / (2 * sigma**2))

def fit_gaussian(x, y):
    # basit başlangıç tahmini
    initial_guess = [max(y), x[np.argmax(y)], 1.0]
    params, _ = curve_fit(gaussian, x, y, p0=initial_guess)
    return params