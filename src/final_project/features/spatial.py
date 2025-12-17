from dotenv import load_dotenv
load_dotenv()

import geopandas as gpd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from final_project.data import acs
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


def route_weighted_demographics(routes_gdf, ca_gdf):
    routes_gdf['total_length'] = routes_gdf['geometry'].length
    inter = gpd.overlay(routes_gdf, ca_gdf, how='intersection')
    inter['intersecting_length'] = inter['geometry'].length
    inter['w'] = inter['intersecting_length'] / inter['total_length']

    var_cols = [col for col in ca_gdf.columns
                if col not in ['ca_number', 'ca_name', 'geometry']]
    for col in var_cols:
        inter[col] *= inter['w']

    df = inter.groupby('route')[var_cols].sum()
    df = acs.compute_ratios(df)
    return df


def ses_index(df):
    X = df[
        ['avg_hh_income', 'poverty', 'has_undergrad_degree', 'has_grad_degree']
    ].copy()
    X = X.assign(log_income=np.log(X['avg_hh_income']))
    X = X.drop(columns='avg_hh_income')

    X_scaled = StandardScaler().fit_transform(X)
    X_pca = PCA().fit_transform(X_scaled)

    ses = (StandardScaler()
            .fit_transform(X_pca[:,0].reshape(-1, 1))
            .reshape(-1))
    return ses
