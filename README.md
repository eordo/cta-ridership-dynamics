# CTA Ridership Dynamics

This is a time series analysis of daily bus and rail ridership on the Chicago Transit Authority, from January 2001 to September 2025.

_Note: This is a project-in-progress for a graduate course._

## Data

Ridership and geographical data are open data provided by the City of Chicago.
Weather data is queried through Meteostat and ultimately provided by the NOAA.
Demographic data is queried from the ACS 5-year estimates.

**Ridership**

- [CTA bus routes, daily totals](https://data.cityofchicago.org/Transportation/CTA-Ridership-Bus-Routes-Daily-Totals-by-Route/jyb9-n7fm/about_data)
- [CTA "L" stations, daily entries](https://data.cityofchicago.org/Transportation/CTA-L-Rail-Stations/3tzw-cg4m/about_data)

**Geography**

- [City boundaries](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-City-Map/ewy2-6yfk)
- [Community Area boundaries](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Community-Areas/igwz-8jzy/about_data)
- [Census Tract boundaries](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/CensusTractsTIGER2010/74p9-q2aq/about_data)
- [Bus routes](https://data.cityofchicago.org/Transportation/CTA-Bus-Routes/6uva-a5ei/about_data)
- [Bus stops](https://data.cityofchicago.org/Transportation/CTA-Bus-Stops/hvnx-qtky)
- ["L" lines](https://data.cityofchicago.org/Transportation/CTA-L-Rail-Lines/xbyr-jnvx/about_data)
- ["L" stations](https://data.cityofchicago.org/Transportation/CTA-L-Rail-Stations/3tzw-cg4m/about_data)

**Weather**

- [O'Hare daily weather history](https://meteostat.net/en/station/72530)
- [Midway daily weather history](https://meteostat.net/en/station/72534)

**Demographics**

- [ACS 5-year data](https://www.census.gov/data/developers/data-sets/acs-5year.html)

Getting the ACS data requires a US Census API key.
Save the key in a `.env` file in the project root like so:

```dotenv
export CENSUS_API_KEY=your_key_here
```
