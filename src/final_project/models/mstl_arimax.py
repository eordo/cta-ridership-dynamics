from pmdarima import auto_arima
from statsforecast.feature_engineering import mstl_decomposition
from statsforecast.models import AutoARIMA, MSTL
from statsmodels.tsa.api import ARIMA


def arima_fit_and_forecast(resid,
                           exog_fit=None,
                           trace=False,
                           params_dict={},
                           steps=1,
                           exog_forecast=None):
    arima = _arima_fit(resid, X=exog_fit, trace=trace, params_dict=params_dict)
    forecast = _arima_forecast(arima, steps=steps, exog=exog_forecast)
    return forecast


def compute_level_forecast(st_forecast_df, resid_forecast):
    return resid_forecast + st_forecast_df.sum(axis=1)


def compute_residual_from_decomposition(df):
    cols = ['y', 'trend'] + \
            [col for col in df.columns if col.startswith('seasonal')]
    df = df[cols]
    resid = df['y'] - df.drop(columns='y').sum(axis=1)
    resid.name = 'residual'
    return resid


def decompose_and_forecast(y, model, steps):
    freq = y.index.freqstr
    y_df = _to_sf_df(y)
    decomp_df, forecast_df = mstl_decomposition(y_df,
                                                model=model,
                                                freq=freq,
                                                h=steps)
    # Decomposition.
    decomp_df = decomp_df.set_index('ds')
    decomp_df = decomp_df.drop(columns='unique_id')
    decomp_df.index.name = 'date'
    # Forecast.
    forecast_df = forecast_df.set_index('ds')
    forecast_df = forecast_df.drop(columns='unique_id')
    forecast_df.index.name = 'date'
    return decomp_df, forecast_df


def mstl_model(season_length, trend_forecaster=AutoARIMA()):
    return MSTL(season_length=season_length, trend_forecaster=trend_forecaster)


def _arima_fit(resid, X, trace=False, params_dict={}):
    best_arima = auto_arima(resid, X=X, trace=trace, **params_dict)
    arima = ARIMA(resid, exog=X, order=best_arima.order)
    arima = arima.fit()
    return arima


def _arima_forecast(model, steps=1, exog=None):
    return model.forecast(steps=steps, exog=exog)


def _to_sf_df(y):
    y_df = (y
            .reset_index()
            .rename(columns={'date': 'ds', y.name: 'y'}))
    y_df['unique_id'] = y.name
    return y_df
