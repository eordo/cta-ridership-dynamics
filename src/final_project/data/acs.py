import os
import numpy as np
import pandas as pd
from census import Census
from final_project.config import (ACS_SENTINEL_VALUE, CENSUS_VARIABLES,
                                  STATE_FIPS, COUNTY_FIPS)


CENSUS_API_KEY = os.getenv('CENSUS_API_KEY')
if not CENSUS_API_KEY:
    raise RuntimeError('Census API key not found.')


def clean_acs_data(df):
    # Fill missing values and rename columns for clarity.
    df = df.replace(ACS_SENTINEL_VALUE, np.nan)
    df = df.rename(columns=CENSUS_VARIABLES)

    # Bin ages into young adult and senior age groups.
    age_cols_18_34 = [
        'male_18-19', 'male_20', 'male_21',
        'male_22-24', 'male_25-29', 'male_30-34',
        'female_18-19', 'female_20', 'female_21',
        'female_22-24', 'female_25-29', 'female_30-34',
    ]
    age_cols_85 = [
        'male_65-66', 'male_67-69', 'male_70-74',
        'male_75-79', 'male_80-84', 'male_85+',
        'female_65-66', 'female_67-69', 'female_70-74',
        'female_75-79', 'female_80-84', 'female_85+',
    ]
    df['age_18-34'] = df[age_cols_18_34].sum(axis=1)
    df['age_85+'] = df[age_cols_85].sum(axis=1)
    df = df.drop(columns=(age_cols_18_34 + age_cols_85))

    # Calculate single-family and multifamily/unit housing totals.
    sfh_total = df['housing_sfh_detached'] + df['housing_sfh_attached']
    mfh_total = (df['housing_total']
                 - sfh_total
                 - df['housing_mobile']
                 - df['housing_other'])
    df['housing_sf'] = sfh_total
    df['housing_mf'] = mfh_total
    df = df.drop(
        columns=[
            'housing_sfh_detached', 'housing_sfh_attached',
            'housing_mobile', 'housing_other'
        ],
        errors='ignore'
    )
    return df


def get_acs_data(
        fields=tuple(CENSUS_VARIABLES.keys()),
        state_fips=STATE_FIPS,
        county_fips=COUNTY_FIPS,
        year=2023
):
    c = Census(CENSUS_API_KEY)
    cen_dicts = c.acs5.state_county_tract(
        fields=fields,
        state_fips=state_fips,
        county_fips=county_fips,
        tract='*',
        year=year
    )
    cen_df = pd.DataFrame(cen_dicts)
    cen_df['year'] = year
    # Drop the provided GEO_ID and use a constructed one instead.
    cen_df['geoid'] = cen_df['state'] + cen_df['county'] + cen_df['tract']
    cen_df = cen_df.drop(columns=['state', 'county', 'tract', 'GEO_ID'])
    return cen_df


def compute_ratios(df):
    # Young adults and seniors.
    young_adult = df['age_18-34'] / df['age_total']
    senior = df['age_85+'] / df['age_total']
    # Race.
    white = df['race_nh_white'] / df['race_total']
    black = df['race_nh_black'] / df['race_total']
    asian = df['race_nh_asian'] / df['race_total']
    hispanic = df['race_hispanic'] / df['race_total']
    # Poverty rate.
    poverty = df['poverty_count'] / df['poverty_total']
    # Educational attainment by degree share.
    undergrad =  df['educ_bachelor'] / df['educ_total']
    grad = (df[['educ_master', 'educ_prof', 'educ_doct']].sum(axis=1)
            / df['educ_total'])
    # Unemployment rate.
    unemployment = df['unemployed'] / df['labor_force']
    # Proportion of households with no vehicle.
    no_vehicle = ((df['tenure_owner_no_veh'] + df['tenure_renter_no_veh'])
                       / df['tenure_total'])
    # Proportion of workers commuting vs. working from home.
    commute = df['commute_transit'] / df['commute_total']
    wfh = df['commute_wfh'] / df['commute_total']
    # Single-family and multifamily/unit housing shares.
    sfh = df['housing_sf'] / df['housing_total']
    mfh = df['housing_mf'] / df['housing_total']

    ratio_cols = {
        'young_adult': young_adult,
        'senior': senior,
        'white': white,
        'black': black,
        'asian': asian,
        'hispanic': hispanic,
        'poverty': poverty,
        'has_undergrad_degree': undergrad,
        'has_grad_degree': grad,
        'unemployment': unemployment,
        'no_vehicle': no_vehicle,
        'commuter': commute,
        'wfh': wfh,
        'sf_home': sfh,
        'mf_home': mfh
    }

    cols_to_drop = [
        'age_18-34', 'age_85+',
        'housing_sf', 'housing_mf',
        'agg_hh_income', 'agg_hh_count'
    ]
    population_total = df['population_total']
    housing_total = df['housing_total']
    avg_hh_income = df['agg_hh_income'] / df['agg_hh_count']
    df = (df
          .drop(columns=list(CENSUS_VARIABLES.values()), errors='ignore')
          .drop(columns=cols_to_drop, errors='ignore')
          .assign(population_total=population_total)
          .assign(housing_total=housing_total)
          .assign(avg_hh_income=avg_hh_income)
          .assign(**ratio_cols))
    return df
