CRS = 26916
STATION_IDS = {
    'ohare': '72530',
    'midway': '72534'
}
STATE_FIPS = '17'
COUNTY_FIPS = '031'
CENSUS_VARIABLES = {
    # Median household income
    'B19013_001E': 'median_hh_inc',         # Median household income (real)
    # Poverty rate
    'B17001_001E': 'poverty_total',         # Total (all)
    'B17001_002E': 'poverty_count',         # At or below poverty level
    # Educational attainment
    'B15003_001E': 'educ',                  # Total (adults 25+)
    'B15003_022E': 'educ_bacc',             # Bachelors
    'B15003_023E': 'educ_mast',             # Masters
    'B15003_024E': 'educ_prof',             # Professional
    'B15003_025E': 'educ_doct',             # Doctorate
    # Unemployment rate
    'B23025_003E': 'labor_force',           # Labor force
    'B23025_005E': 'unemployed',            # Unemployed
    # Vehicle tenure
    'B25044_001E': 'tenure_total',          # Total (tenured)
    'B25044_003E': 'owner_no_veh',          # Owner-occupied, no vehicle
    'B25044_010E': 'renter_no_veh',         # Renter-occupied, no vehicle
    # Means of transportation to work
    'B08301_001E': 'commute_total',         # Total (commuting to work)
    'B08301_010E': 'commute_transit',       # Public transit (excluding taxis)
    'B08301_021E': 'commute_wfh',           # Worked from home
    # For density calculations
    'B01003_001E': 'total_pop',             # Population
    'B25024_001E': 'total_housing',         # Total housing units
    'B25024_002E': 'housing_sfh_detached',  # Detached single-family homes
    'B25024_003E': 'housing_sfh_attached',  # Attached single-family homes
    'B25024_010E': 'housing_mobile',        # Mobile homes
    'B25024_011E': 'housing_other'          # Boats, RVs, etc.
}
