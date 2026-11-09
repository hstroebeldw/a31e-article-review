A31E Return 2 - processed HEC-RAS results (UTM 35S, EPSG 32735)
Source: plan result files of the four HEC-RAS runs (Q100_SDF=p05, Q50_SDF=p06, Q100_MP=p04, Q100_SDF_SWE=p07).
Values are per mesh cell (30 m mesh, 31 155 cells): depth = maximum water surface minus lowest cell elevation.
They are not the sub-cell terrain rasters of RAS Mapper. Velocity = largest face velocity on any face of the cell.

cells_<plan>.shp   wet cells (depth >= 0.01 m). Fields: DEPTH_M, WSE_M, VEL_MS, TPEAK_H (hours from start), D_CLASS (1 = 0.01-0.5, 2 = 0.5-1, 3 = 1-2, 4 = over 2 m)
extent_<plan>.shp  flood outline (dissolved wet cells)
<plan>_depth_max.tif    10 m GeoTIFF of the same cell depths (all plans); wse and velocity for Q100_SDF only
hydrographs_<plan>.csv  inflow, outflow at the Downstream BC line, downstream stage, water stored in the 2D area (Mm3), 15 min
profiles_Q100_SDF.xlsx  River_Long, XS_1, XS_2, XS_3 sampled every 30 m (station from the first point of each line)
summary.csv, landcover_flooded.csv  results tables
