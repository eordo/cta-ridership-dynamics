import os
import pandas as pd
from census import Census
from src.final_project.config import CENSUS_VARIABLES, STATE_FIPS, COUNTY_FIPS


CENSUS_API_KEY = os.getenv('CENSUS_API_KEY')
if not CENSUS_API_KEY:
    raise RuntimeError('Census API key not found.')


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
    return cen_df
