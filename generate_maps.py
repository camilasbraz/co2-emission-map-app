import os
from cartopy import crs as ccrs
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
import polars as pl
from matplotlib import colors, cm
from matplotlib.colors import ListedColormap

diretorio = 'data'
color_config = ['#420a68', '#6a176e', '#932667',  '#bc3754', '#dd513a', '#f37819', '#fca50a', '#f6d746','#fcffa4', '#ffffff']

print('Iniciando loop...')

for arquivo in os.listdir(diretorio):
    if arquivo.endswith(".txt") and "_TOTALS" in arquivo:
        year = arquivo.split("_TOTALS")[0].split("_")[-1]
        caminho_arquivo = os.path.join(diretorio, arquivo)

        print('Lendo arquivo:', arquivo)

        df = pl.read_csv(caminho_arquivo, separator=';', skip_rows=2)
        df.columns = list(map(lambda x: ''.join(filter(str.isalpha, x)), df.columns))
        #df = df.with_columns(pl.lit(year).alias("year"))
        emission_data = df.to_pandas()

        print('Criando geometria...')

        geometry = [Point(xy) for xy in zip(emission_data['lon'], emission_data['lat'])]
        geodata = gpd.GeoDataFrame(emission_data, crs="EPSG:4326", geometry=geometry)

        print('Criando norma de cores...')

        cmap_config = ListedColormap(color_config)
        bounds = [0.0, 0.06, 6, 60, 600, 3000, 6000, 24000, 45000, 120000]
        norm = colors.BoundaryNorm(bounds, cmap_config.N)

        print('Criando mapa de emissão de CO2...')

        fig, ax = plt.subplots(facecolor='none', subplot_kw={'projection': ccrs.Robinson()})
        ax.patch.set_facecolor('none')
        fig.set_size_inches(7, 3.5)
        ax = geodata.plot(ax=ax, column='emissiontons', transform=ccrs.PlateCarree(),
                        cmap=cmap_config, norm=norm, s=0.05, alpha=1, edgecolors='none')
        ax.set_title(f"Emissão de CO$_2$ em toneladas em {year}", fontsize=14, color='#f2f2f2')
        plt.setp(ax.spines.values(), color='none')
        plt.setp([ax.get_xticklines(), ax.get_yticklines()], color='black')
        ax.set_ylim(-8000000, 9000000)
        text_annotation = ax.text(0.9, 0.9, "github/camilasbraz",
                                size=7,
                                color='#f2f2f2',
                                transform=ax.transAxes)
        colorbar_axes = fig.add_axes([0.35, 0.1, 0.34, 0.025])
        sm = plt.cm.ScalarMappable(cmap=cmap_config, norm=norm)
        sm._A = []
        colorbar = fig.colorbar(sm, cax=colorbar_axes, orientation="horizontal", pad=0.2, format='%.0f', 
                        ticks=[0.03, 3, 33, 330, 1800, 4500, 15000, 34500, 82500],
                        drawedges=True)
        colorbar.outline.set_visible(False)
        colorbar.ax.tick_params(labelsize=5, width=0.5, length=0.5, color='#f2f2f2') 
        colorbar_tick_labels = plt.getp(colorbar.ax, 'xticklabels')  
        plt.setp(colorbar_tick_labels, color='#f2f2f2')

        print('Salvando mapa...')

        fig.savefig(f'maps/co2_map_{year}', dpi=1200, bbox_inches='tight')

print('Loop finalizado!')
