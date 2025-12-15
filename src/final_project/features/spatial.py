import geopandas as gpd
from final_project.utils import read_geojson


def interpolate_ca_aggregates(ct_gdf, ca_gdf):
    # Compute the area of all census tracts' intersections with community
    # areas.
    inter = gpd.overlay(ct_gdf, ca_gdf, how='intersection')
    inter['area_intersection'] = inter.geometry.area

    # Compute tract areas.
    ct_areas = ct_gdf[['geoid', 'geometry']].copy()
    ct_areas['area_ct'] = ct_areas.geometry.area

    # Compute the proportion of each intersection's area to total tract area.
    inter = inter.merge(ct_areas[['geoid', 'area_ct']], on='geoid')
    inter['w'] = inter['area_intersection'] / inter['area_ct']

    var_cols = [
        col for col in ct_gdf.columns
        if col not in ['ca_number', 'geoid', 'geometry', 'notes', 'year']
    ]
    for col in var_cols:
        inter[col] *= inter['w']
    ca_agg = (inter
              .groupby(['ca_number', 'ca_name'])[var_cols]
              .sum()
              .reset_index()
              .merge(ca_gdf, on=['ca_number', 'ca_name']))
    return ca_agg


def load_ca_boundaries(filename):
    ca_gdf = read_geojson(filename)
    ca_gdf = ca_gdf[['area_numbe', 'community', 'geometry']]
    ca_gdf = ca_gdf.rename(columns={
        'area_numbe': 'ca_number',
        'community': 'ca_name'
    })
    ca_gdf['ca_number'] = ca_gdf['ca_number'].astype(int)
    return ca_gdf


def load_ct_boundaries(filename):
    ct_gdf = read_geojson(filename)
    ct_gdf = ct_gdf[['geoid10', 'geometry']]
    ct_gdf = ct_gdf.rename(columns={'geoid10': 'geoid'})
    return ct_gdf
