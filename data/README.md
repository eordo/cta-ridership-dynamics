# Data

This directory contains the cleaned ridership data, both aggregate and by route and station.
It also includes the spatial and temporal features engineered for model fitting.

Raw data that cannot be queried via API (ridership data and census, city, and CTA geometries) are not included here for space considerations.
They can be downloaded from the releases and extracted to the `raw` subdirectory like so:

```
data/raw
├── census_tract_boundaries.geojson
├── city_boundaries.geojson
├── community_area_boundaries.geojson
├── CTA_bus_routes_daily_ridership.csv
├── CTA_bus_routes.geojson
├── CTA_bus_stops.geojson
├── CTA_L_lines.geojson
├── CTA_L_station_daily_entries.csv
└── CTA_L_stations.geojson
```
