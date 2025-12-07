from meteostat import Daily
from src.final_project.config import STATION_ID


def get_weather(start, end):
    data = Daily(STATION_ID, start, end)
    df = data.fetch()
    df = df[['tavg', 'tmin', 'tmax', 'prcp', 'snow']]
    df = df.rename(columns={
        'tavg': 'avg_temp',
        'tmin': 'min_temp',
        'tmax': 'max_temp',
        'prcp': 'precipitation'
    })
    df.index.name = 'date'
    return df
