import geopandas as gpd
from src.final_project.config import CRS


def read_geojson(filename):
    gdf = gpd.read_file(filename)
    gdf = gdf[[col for col in gdf.columns if not col.startswith(':')]]
    gdf = gdf.to_crs(CRS)
    return gdf
