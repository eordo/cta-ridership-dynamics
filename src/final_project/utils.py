import geopandas as gpd
from pathlib import Path
from final_project.config import CRS, IMAGES_DIR


def read_geojson(filename):
    gdf = gpd.read_file(filename)
    gdf = gdf[[col for col in gdf.columns if not col.startswith(':')]]
    gdf = gdf.to_crs(CRS)
    return gdf


def save_figure(fig,
                filename,
                destination=IMAGES_DIR,
                dpi=300,
                bbox_inches='tight',
                transparent=False):
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    if not filename.endswith('.png'):
        filename += '.png'
    fig.savefig(
        destination / filename,
        dpi=dpi,
        bbox_inches=bbox_inches,
        transparent=transparent
    )
    print(f"Figure saved to: {destination / filename}")
