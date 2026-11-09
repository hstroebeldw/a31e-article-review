A31E - GIS LAYERS FOR THE MAPS (Update 23 addition, 21 October 2026)
All layers: WGS 1984 UTM Zone 35S (EPSG 32735). Coordinates in whole metres.

Map02_stations_and_points/
  DWS_flow_dam_rain_stations.shp  The 9 DWS stations of Table 1: A3R002, A3H031, A3H030, A3H042, A3E003,
                                  A3H016, A3R003, A3H033, A3H032. Positions from the DWS verified station
                                  lists (WMA1 Limpopo-Olifants: River, Reservoir, Met), dd:mm:ss converted.
                                  NOTE: A3R002, A3H031, A3H030, A3H042 and A3E003 lie within 400 m of each
                                  other at the wall: use one symbol/label group ("Stations at the dam wall")
                                  or offset the labels with leader lines.
                                  If your Map 2 already has a station layer, keep yours and only compare.
  DWS_water_quality_sites.shp     The 7 water-quality sites (DWS NWMS). Field ON_MAP2 = "yes" for the three
                                  sites without a station code (188257, 188038, 188030); the other four sit
                                  at flow stations already on Map 2.
  Flood_points_F1_F2.shp          F1 = dam wall (position of A3R002); F2 = inflow point of the HEC-RAS reach.
  Map2_points.csv                 Same points as a CSV, if you prefer XY Table To Point.

Map09_additional_lowering/        MAIN version: wells running in both runs.
  Map9_additional_lowering_S/D.shp  ADD_DD_M (m), CLASS 0-4 (<0.5, 0.5-1, 1-2, 2-5, >5 m), PUMPED (1 = pumped cell)
  P1_45_pumped_cells(_outline).shp  the 45 pumped cells
  Map9_statistics.csv               numbers for the text (x0.96 and x0.89)
  reference_no_wells/               earlier layers without wells: reference only, do not map.

Map10_pathways/                   pathlines_S/D, endpoints_S/D (times at porosity 1.0 - do not label),
                                  P1_45_pumped_cells_outline.shp

Map11_flood/                      cells_<plan>.shp (D_CLASS 1-4), extent_<plan>.shp, depth GeoTIFFs, README.
                                  Map 11 uses cells_Q100_SDF (depth) and extent_Q50_SDF (outline) only.

NOT IN THIS FOLDER (use your own layers, as on Maps 1-8):
  A31E boundary; rivers and streams; both dams; SANLC 2022 land cover (cultivated, irrigated);
  Map 8 depth-to-water layers (S and D); SRTM 30 m GeoTIFF (for the Map 11 hillshade);
  HEC-RAS 2D flow area perimeter and the two boundary condition lines (your HEC-RAS shapefiles).
