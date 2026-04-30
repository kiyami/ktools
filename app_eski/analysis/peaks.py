from scipy.signal import find_peaks

def detect_peaks(y, height=None, distance=None):
    peaks, _ = find_peaks(y, height=height, distance=distance)
    return peaks