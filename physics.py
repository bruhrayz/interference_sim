import numpy as np

def compute_intensity(X, Y, d, wavelength, t, frequency=3e14):
    k = 2 * np.pi / wavelength
    omega = 2 * np.pi * frequency
    slit1 = np.array([-d / 2, 0])
    slit2 = np.array([d / 2, 0])
    R1 = np.sqrt((X - slit1[0]) ** 2 + (Y - slit1[1]) ** 2)
    R2 = np.sqrt((X - slit2[0]) ** 2 + (Y - slit2[1]) ** 2)
    wave1 = np.cos(k * R1 - omega * t)
    wave2 = np.cos(k * R2 - omega * t)
    total_field = wave1 + wave2
    intensity = total_field ** 2
    return intensity, intensity[-1]
