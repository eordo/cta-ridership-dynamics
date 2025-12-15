import numpy as np
from final_project.config import CENSUS_VARIABLES, ACS_SENTINEL_VALUE


def create_demographic_features(df):
    df = _clean_acs_data(df)
    df = _compute_ratios(df)
    df = _select_features(df)
    return df


def _clean_acs_data(df):
    df = df.replace(ACS_SENTINEL_VALUE, np.nan)
    df = df.rename(columns=CENSUS_VARIABLES)
    df['geocode'] = df['state'] + df['county'] + df['tract']
    df = df.drop(columns=['state', 'county', 'tract'])
    return df


def _compute_ratios(df):
    poverty_rate = df['poverty_count'] / df['poverty_total']
    ug_deg_rate =  df['educ_bacc'] / df['educ']
    grad_deg_rate = (df[['educ_mast', 'educ_prof', 'educ_doct']].sum(axis=1)
                     / df['educ'])
    unemployment_rate = df['unemployed'] / df['labor_force']
    no_vehicle_rate = ((df['owner_no_veh'] + df['renter_no_veh'])
                       / df['tenure_total'])
    commuter_rate = df['commute_transit'] / df['commute_total']
    wfh_rate = df['commute_wfh'] / df['commute_total']
    sfh_total = df['housing_sfh_detached'] + df['housing_sfh_attached']
    mfh_total = (df['total_housing'] - sfh_total
                 - df['housing_mobile'] - df['housing_other'])
    sfh_rate = sfh_total / df['total_housing']
    mfh_rate = mfh_total / df['total_housing']
    ratio_cols = {
        'poverty_rate': poverty_rate,
        'ug_deg_rate': ug_deg_rate,
        'grad_deg_rate': grad_deg_rate,
        'unemployment_rate': unemployment_rate,
        'no_vehicle_rate': no_vehicle_rate,
        'commuter_rate': commuter_rate,
        'wfh_rate': wfh_rate,
        'sfh_rate': sfh_rate,
        'mfh_rate': mfh_rate
    }
    df = df.assign(**ratio_cols)
    return df


def _select_features(df):
    return df[
        [col for col in df.columns if col not in CENSUS_VARIABLES.values()]
        + ['total_population', 'total_housing']
    ]
