import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar
from src.final_project.config import STATION_IDS
from src.final_project.data import noaa


def create_holiday_dummies(date_range):
    cal = USFederalHolidayCalendar()
    holidays = cal.holidays(start=date_range[0], end=date_range[-1])
    return pd.Series(
        date_range.isin(holidays).astype(int),
        name='is_holiday',
        index=date_range
    )


def create_month_dummies(date_range):
    dummies = pd.get_dummies(
        date_range.month,
        drop_first=True,
        prefix='month'
    )
    dummies.index = date_range
    return dummies.astype(int)


def create_weekend_dummies(date_range):
    return pd.Series(
        date_range.dayofweek.isin([5, 6]).astype(int),
        name='is_weekend',
        index=date_range
    )


def get_weather_features(start, end):
    ohare_weather = noaa.get_weather(STATION_IDS['ohare'], start, end)
    midway_weather = noaa.get_weather(STATION_IDS['midway'], start, end)
    df = (ohare_weather
                  .fillna(midway_weather)
                  .fillna(0))
    return df
