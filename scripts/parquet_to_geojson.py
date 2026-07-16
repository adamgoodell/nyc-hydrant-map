#!/usr/bin/env python3
"""Export PP2's hydrant_density.parquet to GeoJSON for tippecanoe.

Includes all 38 Manhattan NTAs, matching PP2's Python visualization
(choropleth_density.png, .explore()), which did not filter by ntatype.
Note this differs from PP2's analysis.sql, which scoped to ntatype='0'
(residential only) for its SQL-side queries.
"""
import geopandas as gpd

INPUT = "data/raw/hydrant_density.parquet"
OUTPUT = "data/raw/hydrant_density.geojson"

gdf = gpd.read_parquet(INPUT)
gdf = gdf.to_crs(epsg=4326)
gdf.to_file(OUTPUT, driver="GeoJSON")

print(f"Wrote {len(gdf)} features to {OUTPUT}")
print(f"Columns: {list(gdf.columns)}")
print(f"CRS: {gdf.crs}")
print(f"Bounds: {gdf.total_bounds}")
