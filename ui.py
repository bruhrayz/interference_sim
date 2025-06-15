import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider
from physics import compute_intensity
from colormaps import wavelength_to_cmap

def run_simulation():
    initial_wavelength = 500e-9
    initial_d = 50e-6
    frequency = 3e14
    grid_size = 500
    size = 0.01
    x = np.linspace(-size / 2, size / 2, grid_size)
    y = np.linspace(0, size, grid_size)
    X, Y = np.meshgrid(x, y)

    fig, (ax_main, ax_profile) = plt.subplots(2, 1, figsize=(8, 8))
    plt.subplots_adjust(left=0.25, bottom=0.25, hspace=0.4)

    initial_intensity, profile = compute_intensity(X, Y, initial_d, initial_wavelength, 0)
    initial_cmap = wavelength_to_cmap(initial_wavelength * 1e9)
    img = ax_main.imshow(initial_intensity, extent=[x.min()*1e3, x.max()*1e3, y.min()*1e3, y.max()*1e3],
                         cmap=initial_cmap, vmin=0, vmax=4, origin='lower')
    ax_main.set_title("Интерференция волн от двух щелей")
    ax_main.set_xlabel("x (мм)")
    ax_main.set_ylabel("y (мм)")

    line_profile, = ax_profile.plot(x * 1e3, profile)
    ax_profile.set_ylim(0, 4)
    ax_profile.set_xlim(x.min() * 1e3, x.max() * 1e3)
    ax_profile.set_ylabel("Интенсивность")
    ax_profile.set_xlabel("x (мм)")
    ax_profile.set_title("Интенсивность на экране (верхняя граница)")

    axcolor = 'lightgoldenrodyellow'
    ax_d = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
    ax_lambda = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)

    slider_d = Slider(ax_d, 'd (μm)', 10, 200, valinit=initial_d * 1e6)
    slider_lambda = Slider(ax_lambda, 'λ (nm)', 300, 700, valinit=initial_wavelength * 1e9)

    def update(frame):
        d_val = slider_d.val * 1e-6
        lambda_val_nm = slider_lambda.val
        lambda_val = lambda_val_nm * 1e-9
        t = frame * 1e-16
        intensity, profile = compute_intensity(X, Y, d_val, lambda_val, t)
        img.set_data(intensity)
        img.set_cmap(wavelength_to_cmap(lambda_val_nm))
        line_profile.set_ydata(profile)
        return [img, line_profile]

    ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)
    plt.show()
