from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = ROOT_DIR / 'data'
RAW_DIR = DATA_DIR / 'raw'
RIDERSHIP_DIR = DATA_DIR / 'ridership'
FEATURES_DIR = DATA_DIR / 'features'
IMAGES_DIR = ROOT_DIR / 'images'
CRS = 26916
STATION_IDS = {
    'ohare': '72530',
    'midway': '72534'
}
STATE_FIPS = '17'
COUNTY_FIPS = '031'
CENSUS_VARIABLES = {
    # Age
    'B01001_001E': 'age_total',
    'B01001_007E': 'male_18-19',
    'B01001_008E': 'male_20',
    'B01001_009E': 'male_21',
    'B01001_010E': 'male_22-24',
    'B01001_011E': 'male_25-29',
    'B01001_012E': 'male_30-34',
    'B01001_020E': 'male_65-66',
    'B01001_021E': 'male_67-69',
    'B01001_022E': 'male_70-74',
    'B01001_023E': 'male_75-79',
    'B01001_024E': 'male_80-84',
    'B01001_025E': 'male_85+',
    'B01001_031E': 'female_18-19',
    'B01001_032E': 'female_20',
    'B01001_033E': 'female_21',
    'B01001_034E': 'female_22-24',
    'B01001_035E': 'female_25-29',
    'B01001_036E': 'female_30-34',
    'B01001_044E': 'female_65-66',
    'B01001_045E': 'female_67-69',
    'B01001_046E': 'female_70-74',
    'B01001_047E': 'female_75-79',
    'B01001_048E': 'female_80-84',
    'B01001_049E': 'female_85+',
    # Race
    'B03002_001E': 'race_total',
    'B03002_003E': 'race_nh_white',
    'B03002_004E': 'race_nh_black',
    'B03002_006E': 'race_nh_asian',
    'B03002_012E': 'race_hispanic',
    # Median household income
    'B19013_001E': 'median_hh_income',      # Median household income (real)
    # Poverty rate
    'B17001_001E': 'poverty_total',         # Total (all)
    'B17001_002E': 'poverty_count',         # At or below poverty level
    # Educational attainment
    'B15003_001E': 'educ_total',            # Total (adults 25+)
    'B15003_022E': 'educ_bachelor',         # Bachelors
    'B15003_023E': 'educ_master',           # Masters
    'B15003_024E': 'educ_prof',             # Professional
    'B15003_025E': 'educ_doct',             # Doctorate
    # Unemployment rate
    'B23025_003E': 'labor_force',           # Labor force
    'B23025_005E': 'unemployed',            # Unemployed
    # Vehicle tenure
    'B25044_001E': 'tenure_total',          # Total (tenured)
    'B25044_003E': 'tenure_owner_no_veh',   # Owner-occupied, no vehicle
    'B25044_010E': 'tenure_renter_no_veh',  # Renter-occupied, no vehicle
    # Means of transportation to work
    'B08301_001E': 'commute_total',         # Total (commuting to work)
    'B08301_010E': 'commute_transit',       # Public transit (excluding taxis)
    'B08301_021E': 'commute_wfh',           # Worked from home
    # For density calculations
    'B01003_001E': 'population_total',      # Population
    'B25024_001E': 'housing_total',         # Total housing units
    'B25024_002E': 'housing_sfh_detached',  # Detached single-family homes
    'B25024_003E': 'housing_sfh_attached',  # Attached single-family homes
    'B25024_010E': 'housing_mobile',        # Mobile homes
    'B25024_011E': 'housing_other'          # Boats, RVs, etc.
}
ACS_SENTINEL_VALUE = -666666666
