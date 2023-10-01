import numpy as np
from matplotlib import colors, cm
from matplotlib.colors import ListedColormap

color_config = ['#420a68', '#6a176e', '#932667',  '#bc3754', '#dd513a', '#f37819', '#fca50a', '#f6d746','#fcffa4', '#ffffff']

def create_norm(data):
    """
    Cria uma norma de cores para um conjunto de dados de emissão de CO2.

    Args:
        data: Um conjunto de dados de emissão de CO2.

    Returns:
        Uma norma de cores.
    """

    # Calcula os limites do mapa de cores.
    limits = np.percentile(data['emissiontons'], np.arange(0, 100, 10))

    colors_config = color_config
    cmap_config = ListedColormap(colors_config)

    # Cria uma norma de cores.
    norm = colors.BoundaryNorm(limits, cmap_config.N)

    # Calcula os ticks da barra de cores.
    ticks = np.around(limits, 2)

    return norm, ticks, cmap_config