from meteostat import Daily


def get_weather(station_id, start, end):
    data = Daily(station_id, start, end)
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
