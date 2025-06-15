def wavelength_to_cmap(wavelength_nm):
    if wavelength_nm < 450:
        return 'plasma'
    elif wavelength_nm < 495:
        return 'Blues'
    elif wavelength_nm < 570:
        return 'Greens'
    elif wavelength_nm < 590:
        return 'YlOrBr'
    elif wavelength_nm < 620:
        return 'Oranges'
    else:
        return 'Reds'
