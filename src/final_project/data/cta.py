import geopandas as gpd
import numpy as np
import pandas as pd
from src.final_project.config import CRS


def aggregate_ridership(df):
    total = df.groupby('date')['rides'].sum()
    start, end = total.index.min(), total.index.max()
    full_idx = pd.date_range(start, end, freq='D')
    total = total.reindex(full_idx, fill_value=np.nan)
    return total


def group_ridership(df, by):
    if by not in ('route', 'station'):
        raise ValueError('Must group by bus route or L station')
    return {k: g[['date', 'rides']] for k, g in df.groupby(by)}


def load_ridership(filename):
    df = pd.read_csv(filename, low_memory=False)
    df = df.rename(columns={'stationname': 'station'}, errors='ignore')
    df = df.drop(columns=['daytype', 'station_id'], errors='ignore')
    df['date'] = pd.to_datetime(df['date'])
    df['rides'] = df['rides'].apply(lambda x: int(x.replace(',', '')))
    return df


def read_geojson(filename):
    gdf = gpd.read_file(filename)
    gdf = gdf[[col for col in gdf.columns if not col.startswith(':')]]
    gdf = gdf.to_crs(CRS)
    return gdf
