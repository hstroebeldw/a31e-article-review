# Abstract

Irrigation in quaternary catchment A31E (North West Province, South Africa) appears to depend on a canal from Klein Maricopoort Dam at its upstream boundary, which carried little or no water for over a decade from 1984. This desktop study assessed how reliable that supply is against the registered scheme volume of 2.34 Mm³/a, how far groundwater within A31E could offset the shortfalls, and how both respond to climate change, and screened flood risk and contaminant pathways. A monthly water balance of the dam was built from station and reservoir records for 1936 to 2009 and run for two bounds, with and without a restriction rule derived from the records. A steady-state groundwater flow model (MODFLOW-NWT), calibrated on four static water levels, was run in two structures that differ in the depth of outflow. Over 74 years the registered volume is delivered in 59% to 87% of the months and in full in 45% to 77% of the years; the longest shortfall event lasts 146 and 20 months. The reliability depends more on the unknown restriction rule than on the demand. The mean shortfall, 0.27 to 0.48 Mm³/a, is 1.6% to 2.8% of the modelled recharge. Abstracting it under the irrigated land lowers the water level by about 1 to 2 m in one structure and 5 to 21 m in the other, and between less than 1% and about 89% of it is balanced by less discharge to rivers feeding a downstream dam. Under the median and the dry end of published projections for about 2050 (1.9 °C warmer, with 3.1% and 8.5% less rain), the reliability by time falls by 4 to 5 and 8 to 11 points and the mean shortfall rises by a quarter to two-thirds, while the discharge of groundwater to the rivers falls about as much as the recharge, by 4% to 14%. In a two-dimensional model of one reach, the 1:100-year flood (889 to 1 252 m³/s by method) passes almost unattenuated and floods about 40% of the cultivated land. In particle tracking, recharge under the irrigated land reaches the river in one structure only. Water released from the dam, unlike runoff generated within A31E, mostly exceeds the irrigation salinity target. Groundwater could offset the average shortfall in volume, but whether it would be new water, and whether it could carry the scheme through a long drought, cannot be established with the available data.

Keywords: canal supply reliability; reservoir water balance; multi-year drought; groundwater flow model; capture; climate change; design flood; particle tracking

# Catchment-Scale Hydrological Processes and Groundwater Dynamics in the A31E Quaternary Catchment, North West Province

# 1. Introduction

In semi-arid regions, irrigated agriculture depends on water that has been stored. Irrigators in a semi-arid South African catchment have coped with past droughts largely through the construction of water storage and the adoption of more efficient irrigation (Lankford *et al*., 2023). The security of an irrigation supply therefore rests on how reliably a dam can deliver, which is described by how often the supply fails, how quickly it recovers and how severe a failure is (Hashimoto *et al*., 1982). In the Marico area of the North West Province, irrigation was the largest water use at the level of development of the year 2000, at 32 million cubic metres per year (Mm³/a) against 12 Mm³/a for rural use, and 26 Mm³/a of it was drawn from surface water, along the Groot Marico and Klein Marico rivers and below dams such as Marico-Bosveld and Klein Maricopoort (DWAF, 2004:ii, 52).

Understanding how water is distributed at a finer scale requires examining South Africa's quaternary catchments, which provide a framework for assessing water availability and planning sustainable use. A quaternary catchment is a fourth-order catchment within a hierarchical classification system in which the primary catchment is the major unit (DWS, s.a.e). In South Africa, the quaternary catchment serves as the fundamental hydrological unit for managing water resources, and 1 946 such catchments have been demarcated (DWS, s.a.e). It is also the basic building block of the national water-resources study (Bailey & Pitman, 2016a:1, 13).

In semi-arid regions, quaternary catchments are replenished by seasonal rainfall, but river flow and groundwater recharge do not respond to this rainfall in simple proportion. Rainfall distribution is uneven and typically occurs as short, intense storms (Nabinejad & Schüttrumpf, 2023). Where about 500 mm of rain falls per year, a decrease of 10% in rainfall may reduce perennial surface drainage by half (De Wit & Stankiewicz, 2006), and recharge begins only once rainfall exceeds a threshold (Cuthbert *et al*., 2019). Dry years also tend to come in runs: of the eight most severe droughts at the two-year scale in southern Africa south of 10°S between 1901 and 1999, six ended in 1983, 1984, 1992, 1993, 1995 and 1996 (Rouault & Richard, 2005), and during long droughts in south-eastern Australia runoff fell below what the earlier relationship between rainfall and runoff predicted (Saft *et al*., 2015). During episodic flood events, water from river channels and floodplains can infiltrate the ground and recharge aquifers, often more effectively than slow percolation of rainfall through the soil, although this recharge is constrained by the high evaporation rates and limited precipitation typical of semi-arid environments (Meredith *et al*., 2015). Groundwater stored in aquifers sustains river flow during dry periods as baseflow (Xie *et al*., 2024); in the semi-arid Kaap catchment of South Africa, groundwater was found to supply 64 to 98% of total runoff (Camacho Suarez *et al*., 2015). Consequently, water availability in a quaternary catchment is strongly influenced by rainfall seasonality, by the sequence of wet and dry years and by interactions between surface water and groundwater systems.

Groundwater is a crucial water resource in many semi-arid and arid regions, often serving as the main or sole water source (Lubczynski, 2006:225), because it buffers the effects of rainfall variability (Calow *et al*., 2010). In countries such as Botswana, for example, groundwater provides the entire water supply (Lubczynski, 2006:225). In South Africa, it contributes approximately 15% of the total volume of water consumed nationally (DWAF, cited by Knüppe, 2011:69), highlighting its importance in areas with limited surface water. Despite efforts to develop groundwater resources in these water-scarce regions, much of their potential remains underutilised (Knüppe, 2011:68). In the Marico area the two sources serve different users: groundwater supplied 11 of the 12 Mm³/a of rural use and more than half of urban use, but only 6 of the 32 Mm³/a used for irrigation (DWAF, 2004:52). Groundwater is widely used but locally constrained, and sustainable management is essential, as it can only be withdrawn at a rate balanced by natural recharge; exceeding this rate lowers groundwater levels and threatens the reliability of supply, as has occurred in the dolomite aquifers of the North West Province (Cobbing, 2018). Its use for irrigation is further limited by what a borehole can yield, since yields above 5 L/s are not widespread in Africa (MacDonald *et al*., 2012).

The quaternary catchment A31E, located in South Africa's North West Province, is a semi-arid catchment in which this dependence on stored surface water takes a particular form. The catchment receives seasonal and variable rainfall, and the largest part of its registered water use is not groundwater but water that appears to be supplied by canal from Klein Maricopoort Dam, which stands at its upstream boundary (DWAF, 2004:50; DWS, s.a.g). A failure of this surface supply therefore has direct implications for the resilience of water users in the catchment, and it raises the question of whether groundwater within A31E could carry them through such a failure.

## 1.1 Research problem

Irrigated agriculture in quaternary catchment A31E appears to depend largely on water that does not originate within the catchment. Klein Maricopoort Dam stands at the upstream boundary of A31E, so that the water it stores is generated in the catchments above it and enters A31E through a canal. Of the 3.38 Mm³/a of water use registered in A31E, 2.34 Mm³/a (69%) is registered as scheme use on 442 ha, at registered positions within about 15 km of the dam wall, whereas 0.285 Mm³/a is registered from boreholes, 0.265 Mm³/a of it at positions inside the catchment boundary (DWS, s.a.g). Registered volumes are entitlements and not measured abstraction, and the register does not name the scheme. That these records represent the users of the canal is therefore inferred from the canal scheme that the Department lists for the dam and from the land mapped as irrigated below it (DFFE, 2024; DWS, 2024). If this inference holds, the largest registered water use in the catchment relies on a single surface-water source that lies outside it.

The records of the dam show that this source has failed for extended periods. Between October 1983 and September 1995 the dam stood below 25% of its capacity in 139 of 144 months, and the canal carried a mean of 0.25 Mm³/a in the eleven complete hydrological years between 1984 and 1995, against a median of 2.02 Mm³/a over 72 complete years of record (DWA, 2012; DWS, s.a.c, station A3H031). A hydrological year runs from October to September and is named after the calendar year in which it begins. The inflow did not recover when rainfall did. Rainfall in WR2012 rainfall zone A3B, which covers A31E and both catchments above the dam, averaged 99% of its long-term mean in 1986–1995, whereas the WR2012 patched observed flow into the dam averaged 1.37 Mm³/a against a median of 3.94 Mm³/a for 1936–2009 (Bailey & Pitman, 2016a). The supply therefore responds to rainfall over several years and not within a single season, which makes the duration of a shortage as important as its depth. For this dam the Department reports a yield of 1.4 Mm³/a, without a stated period, method or assurance, and it placed very low confidence in the hydrological information for the Marico, for which no systems analysis had been done (DWAF, 2004:50, 83). This planning figure and the registered volume are quantities of different kinds and neither is a measured delivery, so that it is still not known how often, for how long and by how much deliveries fall below the registered volume.

It is equally uncertain whether groundwater within A31E could serve as an alternative source during such periods. At catchment scale groundwater appears lightly used, with an estimated recharge of 17.336 Mm³/a against a use of 0.81 Mm³/a (DWS, 2021). A favourable balance of volumes does not, however, show that groundwater can be abstracted where and when it is needed. Mapped borehole yields in A31E are low, each borehole inside the catchment has a single recorded water level, measured between 1910 and 1994, only four of these levels are recorded as static, and no pumping-test results or water-level time series exist (DWS, s.a.d). The only gauged stream inside A31E, which had flowed in every dry-season month on record from 1966 to 1983, was dry in 42 of the 50 months from February 1984 to March 1988 (DWS, s.a.c, station A3H016). This suggests that groundwater storage inside the catchment declined in the same drought that emptied the dam, so that the alternative source may be weakest when it is most needed.

Climate change adds a further uncertainty. Warming is projected over the South African interior with considerably more confidence than any change in rainfall (DEA, 2013). Higher temperatures raise evaporative demand, which increases evaporation from the reservoir and the water requirement of irrigated crops (Allen *et al*., 1998) and is projected to reduce soil moisture over southern Africa (Douville *et al*., 2021). Droughts are projected to become more frequent and longer over large parts of the region (Trisos *et al*., 2022), although an increase in rainfall over parts of the interior cannot be excluded (Engelbrecht, 2019:37). For 2041–2060, the climate models assessed in the IPCC Atlas project for its reference region of eastern southern Africa (ESAF), in which A31E lies, a warming of about 1.5 to 2.9 °C above the mean climate of hydrological years 1937 to 2009. Over the same period they project a change in annual rainfall of about −8.5% to +3%, with a median near −3%. These ranges are the 10th to 90th percentiles of the models under scenarios of intermediate and high future emissions (SSP2-4.5 and SSP5-8.5), calculated from the regional datasets of the Atlas (Gutiérrez *et al*., 2021; Iturbide *et al*., 2020). All the models project a warming, whereas the change in rainfall is small in the median and uncertain in sign. The problem addressed by this study is therefore that the reliability of the surface-water supply conveyed into A31E, the extent to which groundwater within the catchment could offset shortfalls in that supply, and the sensitivity of both to climate change have not been established. This leaves water users and the responsible authorities without a quantified basis for drought planning.

## 1.2 Research questions

The study is guided by the following main research question: How reliable is the canal supply from Klein Maricopoort Dam to irrigators in quaternary catchment A31E under the historical sequence of wet and dry years, to what extent could groundwater within A31E offset the shortfalls that arise when the dam is drawn down, and how would both change under plausible climate conditions for about 2050?

Five supporting questions follow from it:

1. How have the recorded inflow, the storage and the canal deliveries of Klein Maricopoort Dam behaved over the period of record, and how often, for how long and by how much have deliveries fallen below the registered scheme volume?
2. How does water generated within A31E itself reach Kromellenboog Dam, what do the gauged record of the Wilgeboomspruit and the records of the two dams show about its response to drought, and what part does it play in the water balance between the two dams?
3. How reliably can the dam supply the registered scheme volume when its water balance is simulated over the historical record, and how sensitive is this reliability to the assumed demand?
4. What do the available records, including the drying of a gauged stream in the 1980s, indicate about the occurrence, recharge and storage of groundwater within A31E, and what can a groundwater flow model built on these records show about abstraction intended to offset a surface-water shortfall?
5. How would the warmer and probably drier conditions projected for about 2050, represented by the median and the dry end of published projections for the region, alter the reliability of the canal supply and the availability of groundwater?

## 1.3 Aim and objectives

The aim of this study is to assess the reliability of the surface-water supply conveyed into quaternary catchment A31E from Klein Maricopoort Dam, to evaluate the extent to which groundwater within the catchment could offset shortfalls in that supply, and to determine how both may respond to climate change by about 2050, in order to support drought planning and sustainable water-resource management in the catchment.

The objectives of the study are:

1. To compile and critically review the existing hydrological, geohydrological and water-use information for A31E, and to identify the gaps in this information.
2. To characterise the hydrology and groundwater conditions of A31E from the available records, to identify the pressures and risks affecting its water resources, and to develop a conceptual model of how water enters, moves through, is stored in, is used in and leaves the catchment.
3. To simulate the water balance of Klein Maricopoort Dam and its canal over the historical record, with the recorded inflow taken as the condition at the upstream boundary, and to quantify the reliability of supply against the registered scheme volume.
4. To assess, by means of a groundwater flow model of A31E used to compare cases, the extent to which groundwater abstraction within the catchment could offset shortfalls in the canal supply, and to state the limits that the available data place on this assessment.
5. To assess the potential effects of climate change by about 2050 on inflow, evaporation, water demand and recharge, and through these on the reliability of the canal supply and the availability of groundwater.
6. To provide evidence-based recommendations, including priorities for data collection, to support planning and management by the Department of Water and Sanitation, the North West Premier's Office and AGES.

This article addresses these objectives through a desktop-based assessment of quaternary catchment A31E. By consolidating existing hydrological, geohydrological and environmental information, the study seeks to improve understanding of water movement, storage and vulnerability within A31E and to highlight issues that require further investigation. The potential influence of future climate change on the surface supply and on groundwater is assessed with two cases drawn from published projections. Flood risk along one reach of the Klein Marico River, and the pathways along which contaminants could move, are assessed at the level of a screening. The transport of contaminants themselves is not modelled. The insights gained are intended to support more informed groundwater and catchment management in the North West Province, particularly for the Department of Water and Sanitation, the North West Premier's Office and the consulting partner AGES.

# 2. Study Area

## 2.1 Location and the supply system

Quaternary catchment A31E lies in the North West Province of South Africa, east of the town of Zeerust, and covers about 602 km² according to the Water Resources of South Africa 2012 study, or WR2012 (Bailey & Pitman, 2016a). It drains to the Marico River and forms part of the upper Limpopo River basin (Jury, 2016), and it falls within the Limpopo-Olifants Water Management Area, the unit in which water resources are now administered (DWS, 2023). Map 1 shows the catchment, its neighbours and the two dams that bound it.

**[Map 1 here]**
*Map 1: Locality of quaternary catchment A31E, showing the Klein Marico River, Klein Maricopoort Dam at the upstream boundary, Kromellenboog Dam at the outlet, the upstream catchments A31D and A31C, Zeerust and the main roads. Inset: position in the North West Province.*

The Klein Marico River enters A31E at the wall of Klein Maricopoort Dam, also called Kalk Dam, and leaves it through Kromellenboog Dam at the north-eastern corner. The reservoir of the upper dam and the whole area that drains to it lie outside the catchment, in A31D and A31C, while Kromellenboog Dam lies inside it. A31E is therefore the land between the two dams, which agrees with the catchment areas that the Department gives for the two dams, 1 157 km² and 1 762 km², a difference of 605 km² (DWS, s.a.c). Because the boundary runs through the wall of the upper dam, none of the runoff generated within A31E can reach Klein Maricopoort Dam. This applies to the western arm of the catchment as well, which makes up a quarter of its area: it drains through the Doringrivier, which joins the Klein Marico River 4.2 km below the wall. The water stored in the upper dam therefore comes entirely from outside A31E, whereas the runoff of A31E itself flows to Kromellenboog Dam. The Department lists Klein Maricopoort Dam under A31D and gives its purpose as irrigation (DWAF, 2004:50), and it describes Kromellenboog Dam as operated together with Marico-Bosveld Dam for an irrigation scheme in the downstream catchment A31F (DWAF, 2004:57). On this description, the water stored in the lower dam serves users outside A31E.

The canal leaves the dam at its wall, where station A3H031 measures the volume that enters it (Map 2). The Department lists an irrigation scheme for the dam that is supplied "from the canal system" (DWS, 2024); the register of water use does not name the scheme (Section 2.7). Besides the canal and the spillway, the reservoir record contains a further outflow, which from 1987 corresponds to the flow gauged in the river just below the wall at station A3H030 and is read here as a release to the river. It averaged 0.33 Mm³/a over hydrological years 1987 to 2009 and rose with the level of the dam (DWA, 2012; DWS, s.a.c).

Klein Maricopoort Dam was raised in September 1966, and its latest survey, of 1982, gives a capacity of 7.07 Mm³ at full supply over a water surface of 136.80 ha (DWA, 2012). The capacity at full supply is the volume that the dam holds when it is full to the lip of its spillway. Kromellenboog Dam held 8.96 Mm³ over 224.45 ha at its survey of 1998 (DWA, 2012). The Department's weekly reports give slightly different capacities, 7.3 and 8.7 Mm³ (DWS, 2025); the surveyed values are used here because each is tied to a survey date and a surface area. The capacity of the upper dam equals about three years of the volume registered for the irrigation scheme below it (7.07 ÷ 2.34 Mm³/a). Once the dam's mean evaporation loss (Section 2.2) and the mean release to the river are added, it equals about 1.9 years of use (7.07 ÷ 3.74 Mm³/a). This is too little storage to carry the scheme through a drought lasting several years, which is the central concern of this study.

## 2.2 Climate

The Department describes the climate of the Marico and its neighbouring catchments as generally semi-arid (DWAF, 2004:i, 18), with rainfall that is "strongly seasonal with rainfall occurring as thunderstorms in summer" (DWAF, 2004:18). Rainfall in this study is counted by hydrological year, which runs from October to September, so that each rainy season falls within one year (Bailey & Pitman, 2016a). The mean annual precipitation of A31E is 597 mm in the WR2012 study. This value comes from the rainfall series of rainfall zone A3B, a group of neighbouring quaternary catchments that share one rainfall record in that study (Bailey & Pitman, 2016a:14).

Rainfall varies strongly from year to year. Over hydrological years 1967 to 2008, the rain station at Klein Maricopoort Dam, station A3E003, recorded between 314 mm (2006) and 900 mm (1980), and its mean over the 41 complete years was 583 mm/a, against 594 mm/a for zone A3B over the same years (Bailey & Pitman, 2016a; DWS, s.a.c). The two series agree on average and rise and fall together, but in single years the station received between 0.54 and 1.30 times the zone rainfall (Figure A). The zone series is therefore used for the long record. Over 1920 to 2009 it ranged from 314 to 1 106 mm per year, and the six years from 1981 to 1986 all fell below the long-term mean, the longest such run in the record, with 1982 to 1985 receiving only 65% of it (Bailey & Pitman, 2016a). For a dam of the size described in Section 2.1, a run of dry years of this length exhausts the stored water before the next wet year refills it.

**[Figure A here]**
*Figure A: Yearly rainfall at Klein Maricopoort Dam (DWS station A3E003, complete hydrological years only) and in WR2012 rainfall zone A3B, hydrological years 1967–2008.*

The rainy season is short, and evaporation is far larger than rainfall. At the station at the dam, 93% of the rain falls between October and April, and the monthly totals peak from December to February (Figure B; DWS, s.a.c). This is consistent with the regional pattern, in which rainfall over the upper Limpopo rises sharply in late summer, from January to March (Jury, 2016). Irrigated crops in A31E therefore need water through a dry winter of five months, during which the river is fed only by stored water and by whatever groundwater reaches it. Evaporation at the dam is measured with a Symons pan (S-pan), whose readings are converted to open-water evaporation with pan factors (Bailey & Pitman, 2016a:14). The pan recorded a mean of 2 005 mm/a over 42 complete hydrological years between 1967 and 2014, more than three times the rainfall, and pan evaporation exceeded rainfall in every month of the year, even in January, when the rain is greatest (Figure B; DWS, s.a.c). The WR2012 study gives a mean annual evaporation of 1 901 mm for the evaporation zone of A31E (Bailey & Pitman, 2016a).

**[Figure B here]**
*Figure B: Average monthly rainfall and S-pan evaporation at Klein Maricopoort Dam (DWS station A3E003), hydrological years 1967–2014.*

For the dam, evaporation is therefore a loss of the same order as the water it supplies: the reservoir record gives a mean evaporation of 1.07 Mm³/a over its whole length, 1936 to 2010, and about 2.0 Mm³/a in years when the dam stood nearly full (DWA, 2012). Evaporation from small agricultural reservoirs is often overlooked in water accounting (Aminzadeh *et al*., 2024). Here it must be part of any water balance of the dam.

## 2.3 Topography, drainage and monitoring stations

A31E falls from 1 567 m on its southern boundary to 1 038 m at Kromellenboog Dam, a relief of 529 m, and 90% of its area lies between 1 091 m and 1 466 m (measured in GIS on the elevation model of Map 2). The high ground lies in the south, and the valley of the Klein Marico River runs from west to east across the north of the catchment. Over the 24.7 km from the wall of Klein Maricopoort Dam to Kromellenboog Dam, the river falls about 104 m, or about 4 m per km. The water surface of the upper dam stands at about 1 150 m. All the land mapped as irrigated in the strip below the dam lies lower than that, between 1 093 m and 1 140 m (measured in GIS; Section 2.7). The irrigated land is therefore placed where a canal leaving the dam at its wall could reach it by gravity, which agrees with the inference that this land is supplied from the dam.

**[Map 2 here]**
*Map 2: Topography, main rivers and monitoring sites of A31E, with the area of the HEC-RAS model along the Klein Marico River. The stations at the Klein Maricopoort Dam wall (A3R002, A3H030, A3H031, A3H042 and A3E003) lie within 400 m of one another; only some are labelled.*

Four streams drain A31E (Map 2). The Klein Marico River, mapped as perennial, runs the length of the valley. The Doringrivier drains the western arm and joins it 4.2 km below the dam wall. A southern tributary, named the Waterkloofspruit in the register of water use, joins it 13.7 km below the wall. The Wilgeboomspruit, mapped as non-perennial, rises in the south and reaches the river at the head of Kromellenboog Dam. "Perennial" and "non-perennial" are classes of the mapped river network, not measurements of flow.

The WR2012 study estimates the naturalised runoff of A31E at 7.21 Mm³/a (Bailey & Pitman, 2016a). Naturalised runoff is a modelled quantity: it is the flow that the catchment would yield if it had no dams, abstraction or afforestation (Bailey & Pitman, 2016a:18). As none of it can reach the upper dam (Section 2.1), it can be stored only in Kromellenboog Dam and cannot add to the supply of the canal.

The records used in this study are listed in Table 1, and the stations are marked on Map 2. The inflow to Klein Maricopoort Dam is not measured by a river gauge. It is calculated from the dam's own water balance, from the change in storage and the recorded outflows, and the missing months were filled by the WR2012 study, which calls the result patched observed flow (Bailey & Pitman, 2016a:8). Two consequences follow for the study. A complete inflow record is not thereby a measured one. And the only record of runoff generated inside A31E is that of station A3H016 on the Wilgeboomspruit, which measures a catchment of 39 km², about 6.5% of A31E, and ends in August 1992 (DWS, s.a.c). Any statement about the runoff of A31E as a whole rests on modelled values or on a difference between the balances of the two dams. How complete and how good each record is, is set out with the data in the Methodology (Section 5.1).

*Table 1: Stations and records used in this study, with the period of each monthly record and the share of months that have a value (Bailey & Pitman, 2016a; DWA, 2012; DWS, s.a.c).*

| Station | What is measured | From | To | Months | With a value (%) |
|---|---|---|---|---|---|
| A3R002 | Spill over the wall of Klein Maricopoort Dam | 1936/06 | 2026/06 | 1 081 | 97.1 |
| A3R002 | Storage in the dam (reservoir record) | 1936/06 | 2010/11 | 894 | 98.5 |
| A3R002 | Inflow to the dam (WR2012 patched observed flow) | 1936/10 | 2010/09 | 888 | 100.0 |
| A3H031 | Volume in the canal | 1936/06 | 2026/05 | 1 080 | 97.4 |
| A3H030 | River below the dam (low flows only) | 1987/02 | 2011/05 | 292 | 98.6 |
| A3H042 | River below the dam | 2012/01 | 2026/06 | 174 | 60.3 |
| A3E003 | Rainfall at the dam | 1967/09 | 2025/02 | 690 | 92.0 |
| A3E003 | S-pan evaporation at the dam | 1967/10 | 2025/02 | 689 | 95.4 |
| A3H016 | Flow in the Wilgeboomspruit (39 km²) | 1965/12 | 1992/08 | 321 | 87.5 |
| A3R003 | Spill over the wall of Kromellenboog Dam | 1955/02 | 2026/07 | 858 | 99.4 |
| A3H033 | Volume in the Kromellenboog canal | 1955/02 | 2026/07 | 858 | 97.2 |
| A3H032 | River below Kromellenboog Dam | 1979/12 | 2026/07 | 560 | 94.3 |
| Zone A3B | WR2012 rainfall (not a station) | 1920/10 | 2010/09 | 1 080 | 100.0 |

## 2.4 Geology

A31E is underlain by rocks of the Pretoria Group, which are cut by intrusions of diabase and partly covered by surface deposits (Map 3; Michaluk & Keyser, 1991; Walraven, 1981). Eriksson *et al*. (1995), who use the earlier name Transvaal Sequence for the Transvaal Supergroup, describe the Pretoria Group as part of that succession, made up of clastic sedimentary rocks and volcanics. Two of its formations underlie 71.6% of the catchment. The Timeball Hill Formation covers 48.6%: its Klapperkop Quartzite Member, of quartzite with wacke, siltstone and shale, covers 24.0%, and the rest of the formation, of mudrock and quartzite with hornfels and slate, covers 24.6%. The Hekpoort Formation, of andesitic lava with tuff and agglomerate, covers 23.0%. Five smaller formations, the Boshoek, Dwaalheuwel, Daspoort, Strubenkop and Silverton formations, together cover 4.1%, and diabase covers 1.5%. Surface deposits cover 22.5%; the map does not describe them further, and only 0.2 km² of them is mapped as river sand and alluvium. The remaining 0.4% is the open water of Kromellenboog Dam (areas measured in GIS).

**[Map 3 here]**
*Map 3: Geology of A31E in four rock groups, labelled with the formations of the Pretoria Group, with the mapped faults and diabase dykes (Michaluk & Keyser, 1991; Walraven, 1981).*

For groundwater it is the kind of rock that matters, and Table 2 sets out the mapped units by rock group. Quartzite and sandstone form the high ground, mostly in the south. The volcanic rocks lie in the north and north-east, and the mudrock, shale and hornfels mostly in the south. The surface deposits follow the valleys of the Klein Marico River and the Doringrivier.

*Table 2: The rock groups of A31E, the mapped units in each and their share of the catchment (Michaluk & Keyser, 1991; Walraven, 1981; shares measured in GIS). Open water covers the remaining 0.4%.*

| Rock group | Mapped units | Rocks described on the map | Share of A31E |
|---|---|---|---|
| Quartzite and sandstone | Timeball Hill Formation: Klapperkop Quartzite Member and one further quartzite unit; Boshoek, Dwaalheuwel and Daspoort formations | Quartzite and quartzitic sandstone, with minor siltstone and shale | 31.8% |
| Volcanic rocks, diabase and tuff | Hekpoort Formation; diabase | Andesitic lava, tuff and agglomerate; diabase | 24.4% |
| Surface deposits | Surface deposits | Not described further on the map | 22.5% |
| Mudrock, shale and hornfels | Timeball Hill Formation: its other units; Strubenkop and Silverton formations | Mudrock, shale, hornfels and slate | 20.9% |

The type of rock matters because groundwater occurrence depends primarily on geology, on the weathering of the rock and on effective rainfall (MacDonald *et al*., 2012:2). On the hydrogeological map of this region, sandstone and quartzite are placed in the fractured mode of groundwater occurrence, which describes aquifers associated with fractures, fissures and joints, and shale and volcanic rocks such as andesite in the intergranular and fractured mode, in which groundwater is held in the spaces between grains as well as in fractures (DWAF, s.a.). The rocks of A31E follow this pattern. Of the area of quartzite and sandstone, 88% is mapped as a fractured aquifer, whereas 96% of the volcanic rocks and 80% of the mudrock, shale and hornfels are mapped as intergranular and fractured aquifers (measured in GIS). The high ground in the south is therefore likely to store little groundwater outside its fractures, which agrees with the very low storativity that the national assessment models for the fractured zone of A31E (Section 2.5).

The map also shows 94 fault segments, with a combined length of 57.3 km, and 13 diabase dykes, with a combined length of 16.9 km (measured in GIS). In this study no borehole yield, log or pumping test in A31E was tied to any of them, so their bearing on groundwater cannot be assessed here.

The surface deposits matter most for the research question, because 91.6% of the land mapped as irrigated lies on them, although they cover only 22.5% of the catchment (Table 7). The highest borehole yields in Africa come from thick unconsolidated or poorly consolidated sediments (MacDonald *et al*., 2012:5). The surface deposits of A31E, however, are not mapped as a separate aquifer: 71% of their area is mapped as intergranular and fractured and the rest as fractured, and 68% of it lies in the lower mapped yield class (Section 2.5). Their thickness, their make-up and whether they hold usable groundwater are not known. The National Groundwater Archive, the Department's database of groundwater observations (Section 2.5), lists lithological logs for 387 boreholes inside A31E (DWS, s.a.d), but the logs were not examined in this study, and no pumping test is recorded. On the present evidence they cannot be treated as a separate aquifer, and this gap is carried into the recommendations on data collection (Section 8.2).

## 2.5 Hydrogeology

The hydrogeological map assigns each area to a mode of groundwater occurrence, called an aquifer type, and to a class of borehole yield (Barnard, 1999; DWAF, s.a.). Two aquifer types occur in A31E. Intergranular and fractured aquifers cover 59.8% of the catchment and fractured aquifers 40.2% (Map 4; measured in GIS). Karst aquifers, in which half of the boreholes yield more than 5 L/s (DWAF, s.a.), do not occur in A31E. This sets A31E apart from the dolomite aquifers of the North West Province, which are among the most important in the country (Cobbing, 2018).

**[Map 4 here]**
*Map 4: Aquifer types and mapped borehole-yield classes in A31E (Barnard, 1999), with the four boreholes that have a static water level (DWS, s.a.d). The yield classes are mapped medians, not measured yields.*

The yield class is a mapped range of the median yield of the boreholes in an area, in litres per second (L/s), and it is not the yield of any particular borehole (DWAF, s.a.). In A31E the class 0.5–2.0 L/s covers 75.3% of the catchment and the class 0.1–0.5 L/s covers 24.7%. The lower class lies on the lower ground, in and around the river valley, and three-quarters of the land mapped as irrigated (75.1%) lies on it (Table 7). Counted at the registered positions of the irrigation scheme, only 30.0% of the registered volume falls in the lower class. The difference arises because half of those positions are registered on the higher ground, which lies in the higher class and above the level of the dam (Section 2.7). Where irrigation actually takes place, groundwater is therefore mapped in the lower class.

The scale of the difficulty can be shown with a simple calculation, which indicates scale only. The registered scheme volume of 2.34 Mm³/a equals 2 340 000 m³ ÷ 31 536 000 s, or about 74 L/s pumped without pause throughout the year. At the upper and lower limits of the lower class, 0.5 and 0.1 L/s, this would take about 150 to 740 boreholes pumping all year (74 ÷ 0.5 = 148; 74 ÷ 0.1 = 742). At these yields a borehole meets the 0.1 to 0.3 L/s that a community handpump needs (MacDonald *et al*., 2012:5). The Department likewise judged that groundwater in the Marico can meet domestic supplies "but not bulk water requirements for purposes such as irrigated agriculture" (DWAF, 2004:55–56). That judgement concerns the whole Marico sub-area, including its dolomite, and not the aquifers of A31E in particular.

The properties of the aquifers are known only as regional, modelled values (Table 3). They are taken from the national Groundwater Resource Assessment, known as GRAII, as the mean of its 1 km grid cells inside the catchment (DWS, s.a.b). According to it, the weathered upper zone holds about 91% of the groundwater stored in A31E, although it is only about 25 m thick, because its storativity is some seventy times that of the fractured rock below. The water that boreholes can draw on is therefore stored mainly near the surface, and shallow sources are the first to fail when a drought lowers groundwater levels (Calow *et al*., 2010).

*Table 3: Groundwater terms used in this study and the modelled regional values for A31E (DWS, s.a.b; means of 1 km grid cells).*

| Term | Meaning | Value for A31E |
|---|---|---|
| Transmissivity | How easily the full thickness of an aquifer passes water, in m² per day | 22.81 m²/d |
| Storativity | The volume of water an aquifer releases per square metre of its area when its water level falls by 1 m | Weathered zone 0.00998; fractured zone 0.00014 |
| Thickness | Thickness of the weathered zone and of the fractured zone below it | 25.36 m and 182.14 m; their bases lie 47.50 m and 207.50 m below the surface |
| Recharge | The part of rainfall that reaches the groundwater | 4.84% of rainfall, about 29 mm/a |

The National Groundwater Archive, the Department's database of groundwater observations, holds 425 boreholes inside A31E (DWS, s.a.d). For 266 of them it records a water level, but each of these boreholes has a single level only, measured between 1910 and 1994, so that no water-level series exists anywhere in the catchment. Four of the levels are recorded as static water levels, which is the level at which water stands in a borehole that is not being pumped (Table 4). Three of the four were measured in 1990 and 1994, during the drought of 1984 to 1995, when Klein Maricopoort Dam stood at 12% to 14% of its capacity (DWA, 2012). The status of the other 262 levels is not recorded, so it is not known whether they are undisturbed levels or were measured during or soon after pumping. Most of their positions were read from 1:50 000 maps, and boreholes drilled at different times often share one position: the 266 boreholes lie in 55 groups within 50 m of each other. These 262 levels are therefore not used to calibrate the groundwater model; they serve as an independent comparison in the Results (Section 6.5). The depth to water is 9.24 m to 30.00 m at the four static levels and 0.91 m to 84.0 m at the other levels, with a median of 19.4 m. None of the four static levels lies in the western arm, although 23 of the other levels do, and only one lies on surface deposits in the lower yield class, the setting of most of the irrigated land. For 109 of these boreholes the archive records a yield measured when water was struck during drilling, with a median of 0.3 L/s. A strike yield is not a yield that a borehole can sustain, and no pumping test is recorded. With single levels and no water-level series or pumping tests, the behaviour of groundwater in A31E over time cannot be read from boreholes. The only indirect evidence, the drying of the Wilgeboomspruit in the 1980s, is examined in the Results (Section 6.2).

*Table 4: The four boreholes inside A31E with a static water level, with the date of the level (DWS, s.a.d), and the mapped classes in which they lie (measured in GIS).*

| Borehole | Date of level | Depth to water (m) | Rock group | Aquifer type | Mapped yield class | Soil group |
|---|---|---|---|---|---|---|
| 2526AD00180 | 11 May 1994 | 30.00 | Volcanic rocks, diabase and tuff | Intergranular and fractured | 0.5–2.0 L/s | B/C |
| 2526CA00602 | 9 July 1990 | 9.24 | Quartzite and sandstone | Fractured | 0.5–2.0 L/s | B/C |
| 2526CA00864 | 10 July 1990 | 20.23 | Surface deposits | Intergranular and fractured | 0.1–0.5 L/s | B/C |
| 2526CB00135 | 25 November 1974 | 10.97 | Quartzite and sandstone | Fractured | 0.5–2.0 L/s | C |

## 2.6 Soils

Soils are grouped here according to the hydrological soil groups of the Soil Conservation Service (SCS) of the United States, which rank soils by their potential to produce runoff when thoroughly wet (USDA-NRCS, 2009:7-2). In South Africa the four main groups, A to D, are extended to seven by three transitional groups, A/B, B/C and C/D, and the groups are used mainly to estimate design-flood volumes and peaks through a runoff index known as the curve number (Schulze & Schütte, 2023). A South African group such as C/D lies between C and D. It is not the "dual" group of the American handbook, where C/D describes a soil that behaves as C when drained and as D when not (USDA-NRCS, 2009:7-3). Table 5 sets out the groups that occur in A31E.

**[Map 5 here]**
*Map 5: Hydrological soil groups of A31E according to the SCS classification as applied in South Africa (Table 5).*

*Table 5: SCS hydrological soil groups: what each group means and its share of A31E (Schulze & Schütte, 2023; USDA-NRCS, 2009:7-2–7-3; shares measured in GIS). Groups A and D do not occur in A31E and are shown for reference.*

| Group | Runoff potential when thoroughly wet | Typical soil | Where it lies in A31E | Share of A31E |
|---|---|---|---|---|
| A | Low | Less than 10% clay and more than 90% sand or gravel; water is transmitted freely | Does not occur | – |
| B | Moderately low | 10–20% clay and 50–90% sand | One patch near Kromellenboog Dam | 1.2% |
| B/C | Between B and C | Transitional | The middle of A31E and the western arm | 38.7% |
| C | Moderately high | 20–40% clay and less than 50% sand | The high ground in the south | 31.5% |
| C/D | Between C and D | Transitional | The north and north-east, along the river valley | 28.7% |
| D | High | More than 40% clay; water movement through the soil is restricted or very restricted | Does not occur | – |

Groups C and C/D, with moderately high to high runoff potential, cover 60.2% of A31E, and the soils with the highest runoff potential that occur, group C/D, lie on the lowest ground along the river valley. The cause lies in the clay content: the more clay a soil holds, the more slowly water moves through it, so that a wet soil sheds more of the rain that falls on it (USDA-NRCS, 2009:7-2). The groups describe runoff potential under wet conditions for flood estimation. They do not measure how much rain becomes recharge in an ordinary year. In a climate where evaporative demand exceeds rainfall in every month (Section 2.2), soils are seldom thoroughly wet, and the measured flow of the Wilgeboomspruit at station A3H016 shows how little rain left its catchment as streamflow: about 53 mm/a, or 7.6% of the rainfall, in the six complete years from 1966 to 1980 (Bailey & Pitman, 2016a; DWS, s.a.c). The irrigated land lies mostly on group B/C (Table 7).

## 2.7 Land cover, irrigation and water use

Land cover is shown on Map 6 from the South African National Land Cover 2022 (DFFE, 2024). A land-cover class is the result of classifying satellite images: it is mapped and not surveyed on the ground, and it describes one period, 2022. Natural woodland and grassland cover 87% of A31E, and the natural vegetation belongs to three vegetation types, Dwarsberg-Swartruggens Mountain Bushveld, Moot Plains Bushveld and Zeerust Thornveld. Cultivated land of every kind covers 10.2%, more than half of it fallow land and old fields, and land mapped as irrigated covers only 168 ha, or 0.3% (calculated in GIS from DFFE, 2024). Built-up land also covers 0.3%, so that the catchment contains no large urban demand of its own. Because most of the catchment remains under natural cover, the demand for water is concentrated on a small cultivated area, and it is there that the question of supply arises.

**[Map 6 here]**
*Map 6: Land cover of A31E in 2022 (DFFE, 2024). The land cover is classified from satellite images and is not surveyed on the ground.*

A registered water use is an entitlement that a user has declared and that the Department has entered in its national register of water use, the Water Use Authorisation and Registration Management System, or WARMS (DWS, s.a.g). The register records what may be used, not what was abstracted, and every registration in A31E still awaits a finding on its lawfulness. The register divides use by the resource from which water is taken (Table 6). "Scheme" is the register's own category and is not explained in it.

*Table 6: Registered water use in A31E by resource type (DWS, s.a.g; register as exported on 9 May 2024). Registered volumes are entitlements, not measured abstraction.*

| Resource type | Records | Registered volume (Mm³/a) | Share of volume (%) |
|---|---|---|---|
| Scheme | 76 | 2.34 | 69.3 |
| River or stream | 14 | 0.751 | 22.2 |
| Borehole | 29 | 0.285 | 8.4 |
| Total | 119 | 3.38 | 100.0 |

Nearly all the registered use (98.9%) is for irrigation (DWS, s.a.g). The 76 scheme records stand on only 47 different positions, all between 0.55 km and 14.6 km from the wall of Klein Maricopoort Dam and none within 7 km of Kromellenboog Dam (measured in GIS). These positions must be read with care. Half of the records, carrying 47.6% of the registered scheme volume, lie at about river level, between 1 093 m and 1 142 m and at most 2.4 km from the river. The other half lie between 1 159 m and 1 319 m on higher ground, mostly north of the river, 18 to 199 m above the nearest point of the river and above the level of the dam (measured in GIS). A canal carries water downhill, so a position higher than the dam cannot be a field that the canal supplies by gravity. The register most probably records a reference point of the registered property rather than the position of the field, although the register does not say how its positions were fixed and pumping from the canal cannot be ruled out. The registered positions therefore show where the registrations are pinned, not where the water is used.

The land mapped as irrigated is the better guide to where irrigation took place in 2022. Of its 168 ha, 162 ha lie in fifteen patches in the strip below the dam, all lower than the dam's water surface, and 86% of the irrigated land lies within 1 km of a registered scheme position (DFFE, 2024; measured in GIS). Two small patches in the south lie near registered river abstractions. Three quantities thus describe irrigation from the dam, and they are of different kinds. The register lists 442 ha and 2.34 Mm³/a, which is an entitlement. The land cover maps 168 ha of irrigated land, 145 ha of it under centre pivots, which is a satellite classification of a single year and may miss fields irrigated by flood or furrow. And station A3H031 measured 1.89, 2.19 and 2.16 Mm³ entering the canal in hydrological years 2022, 2023 and 2024, before any losses along the canal (DWS, s.a.c); the total for 2023 includes one month coded as a permanent gap and is a minimum. These quantities cannot be combined in one calculation. Two conclusions follow, and no more. The irrigated land of A31E lies within about 15 km of Klein Maricopoort Dam, in the strip where the scheme is registered. And the registered area cannot be read as the area actually irrigated. Because this study measures shortfalls against the registered volume, its results describe the security of an entitlement and not the water actually used by crops.

Table 7 sets out what lies beneath irrigation in A31E. Column (a) is the land mapped as irrigated in the strip below the dam, which shows where irrigation took place in 2022. Column (b) is all 76 registered scheme records, weighted by their registered volume, which shows where the registrations are pinned. Column (c) gives the whole of A31E for comparison. Columns (a) and (b) differ because half of the registered positions lie on higher ground. Column (a) is therefore the one that bears on how far groundwater beneath the irrigated land could stand in for the canal, and it is used for that purpose in Sections 2.4 to 2.6.

*Table 7: Mapped rock group, aquifer type, yield class and soil group under the land mapped as irrigated, at the registered scheme positions, and over A31E as a whole (measured in GIS).*

| Mapped class | (a) Land mapped as irrigated, share of area | (b) All 76 scheme records, share of registered volume | (c) A31E, share of area |
|---|---|---|---|
| **Rock group** | | | |
| Surface deposits | 91.6% | 38.0% | 22.5% |
| Volcanic rocks, diabase and tuff | 7.7% | 41.7% | 24.4% |
| Mudrock, shale and hornfels | 0.4% | 5.1% | 20.9% |
| Quartzite and sandstone | 0.2% | 13.2% | 31.8% |
| **Aquifer type** | | | |
| Intergranular and fractured | 99.8% | 85.6% | 59.8% |
| Fractured | 0.2% | 12.3% | 40.2% |
| **Mapped yield class** | | | |
| 0.1–0.5 L/s | 75.1% | 30.0% | 24.7% |
| 0.5–2.0 L/s | 24.9% | 67.9% | 75.3% |
| **Soil group** | | | |
| B/C | 83.2% | 45.6% | 38.7% |
| C/D | 16.8% | 52.4% | 28.7% |

*Soil groups C and B (31.5% and 1.2% of A31E) underlie neither the irrigated land nor the scheme positions. In column (b), two scheme records (2.1% of the registered volume) fall just outside the boundary, so that column adds up to less than 100%. In column (c), open water makes up the remaining 0.4% of the rock groups.*

Water quality is assessed in this study only as a screening along the two paths of water (Sections 5.12 and 6.10), but one feature of the river matters already for reading its flow. The Department has described return flows from Zeerust and from irrigation that are "being discharged into the Klein Marico River" (DWAF, 2004:86), and noted that their nutrient and salt content limits their re-use (DWAF, 2004:57). Since Zeerust and the irrigation of A31D lie above the dam, these return flows probably reach the river upstream of Klein Maricopoort Dam, so that part of the recorded inflow to the dam may be return flow and not runoff. The Department has monitored water quality at seven sites in A31E between 1966 and 2023 (DWS, s.a.f). Their records are screened against the national water quality guidelines in Sections 5.12 and 6.10, without trend testing or a full solute balance.

# 3. Literature foundation

## 3.1 How the reliability of a supply is measured

The performance of a water-supply system is usually judged by more than the average volume it delivers. Hashimoto *et al*. (1982:14) proposed three criteria for this purpose. Reliability describes how often the system is in a satisfactory state. Resiliency describes how quickly it returns to a satisfactory state once it has failed. Vulnerability describes how severe a failure is when it occurs (Hashimoto *et al*., 1982:16–17). All three depend on a threshold that separates a satisfactory delivery from an unsatisfactory one, so the choice of threshold is as important as the record to which it is applied. In this study a failure is a period in which the canal from Klein Maricopoort Dam delivers less than the registered scheme volume. The three criteria then answer the questions of the research problem directly: how often deliveries fall short, for how long, and by how much (Section 1.1).

Reliability of the supply is not the same as resilience of the irrigators who depend on it. Lankford *et al*. (2023) showed that in a semi-arid catchment the irrigated area, the efficiency of irrigation and the water held in storage together determined how well irrigated agriculture came through drought. Farmers who face a shortfall may plant a smaller area or apply less water, so the volume they use can fall with the supply. This study therefore measures the supply against a fixed registered volume. It does not attempt to measure how the farms of A31E adjusted to a shortfall.

## 3.2 Why a small dam can remain low for several years

With storage of less than two years of use (Section 2.1), Klein Maricopoort Dam can carry the scheme through one dry season or one dry year, but not through a run of dry years in which inflow stays below demand. Its record shows such a period, from 1983 to 1995 (Section 1.1). The causes of that period are taken up in the conceptual model (Section 4.1). Two points bear on how it must be modelled. First, because the relationship between rainfall and runoff can shift during a multi-year drought (Section 1; Saft *et al*., 2015), a relationship calibrated on wetter years may overestimate inflow in precisely the years that determine reliability. Second, the inflow to the dam stayed low for years after rainfall had recovered (Section 1.1). This suggests that part of the inflow depends on a store that responds over several years, such as groundwater in the catchments above the dam, or that the use of water above the dam increased. That is an inference: the records of the dam do not show where its inflow comes from. Le Maitre and Colvin (2008) showed that the contribution of groundwater discharge to rivers can be assessed from monthly flow statistics and flow seasonality, which is the scale of the records used in this study.

## 3.3 Evaporation from the reservoir

Evaporation from small agricultural reservoirs is expected to increase as the climate warms (Aminzadeh *et al*., 2024). That study concerns reservoirs outside South Africa, so its projected increases cannot be transferred to Klein Maricopoort Dam, but the loss it describes is large here (Section 2.2). The loss depends on the surface area of the water, which is why the reservoir record shows about twice the mean loss in years when the dam stood nearly full (Section 2.2). A water balance that leaves evaporation out, or holds it constant, would therefore overstate how long the stored water lasts after a wet season. The open-water evaporation applied to the dam is derived from S-pan readings with pan factors (Section 2.2), and this conversion is one source of uncertainty in the balance.

## 3.4 Registered use, demand and delivery

The registered volume against which deliveries are measured is an entry in the national register of water use (Section 2.7). For the scheme below Klein Maricopoort Dam the register allows nearly the same volume per hectare throughout: 75 of the 76 records carry 5 300 m³/ha and one carries about 5 400 m³/ha (DWS, s.a.g). The registered volume thus follows from the registered area and not from the crops grown on it. The volume measured at the head of the canal at station A3H031 is a different quantity: it is what entered the canal, before any losses along it. The Department noted, for the canal system of the Marico Bosveld scheme, that "With no proper measurements, it is difficult to quantify the conveyance losses" (DWAF, 2004:105). That passage does not name the canal from Klein Maricopoort Dam, and no record of losses along that canal was found. Neither quantity can be set equal to the area mapped as irrigated (Section 2.7). The registered volume is used as the threshold because it is the volume the scheme is entitled to receive, whereas the measured canal volumes show what was actually released into the canal.

## 3.5 Groundwater as a fallback in hard-rock terrain

Calow *et al*. (2010:246) argue that groundwater security during drought depends on three things together: the water stored in an aquifer, access to it through wells and boreholes, and the demand placed on it. A source that is reliable for domestic supply may therefore fail under the larger and more concentrated demand of irrigation. In A31E it is access that appears most limiting: the land mapped as irrigated lies mostly on surface deposits of unknown thickness, in the lower mapped yield class (Sections 2.4 and 2.5).

A comparable study in hard-rock, semi-arid terrain is that of Ebrahim *et al*. (2019) in the Hout catchment, Limpopo Province. There agricultural pumping was not metered and had to be estimated from satellite vegetation indices, and the model was calibrated over 2008–2012 and validated over 2013–2015. Groundwater use for irrigation in A31E is likewise unmetered, and only four boreholes inside the catchment have a static water level (Section 2.5). The role of groundwater in this study is therefore limited to comparing cases, to show the direction and relative size of the effect of abstraction intended to make up part of a canal shortfall. It is not a full assessment of groundwater development.

## 3.6 Modelling with few data

Where measured records are sparse, the WR2012 study provides two kinds of long monthly series: naturalised flows for every quaternary catchment, and patched observed flows, in which gaps in a measured record are filled (Bailey & Pitman, 2016a:1, 8, 18). Dlamini *et al*. (2023) used the WEAP model to assess the impact of climate change on surface water availability in the Buffalo River catchment, and Ebrahim *et al*. (2019) built an integrated groundwater model with calibration and validation periods of only five and three years. Such periods show the cost of short records: a model calibrated over a few years may not represent a drought longer than its calibration period. For Klein Maricopoort Dam, the monthly reservoir record covers 1936 to 2010 and includes the long dry period of the 1980s and 1990s (Table 1). The simplest approach that can be defended is therefore one that uses this record directly. The choice of model is set out in the Methodology (Section 5.2).

## 3.7 Climate change and the supply

The projections used in this study are those assessed by the Intergovernmental Panel on Climate Change (IPCC) in its Sixth Assessment Report. For regional analysis the IPCC divides the land into reference regions. Southern Africa is split into a western region (WSAF) and an eastern region (ESAF) (Iturbide *et al*., 2020). A31E lies in ESAF, close to its boundary with WSAF. For each region the Atlas of the report provides the results of two sets of models (Gutiérrez *et al*., 2021):
- the global climate models of the sixth phase of the Coupled Model Intercomparison Project (CMIP6);
- the regional models of the Coordinated Regional Climate Downscaling Experiment for Africa (CORDEX-Africa), which recalculate the climate of a global model on a finer grid over the continent.

The regional models are run under the earlier scenario RCP4.5, which, like SSP2-4.5, describes intermediate emissions.

Projections for southern Africa point towards a later start of the summer rains. Howard and Washington (2020) traced projected drying in spring and early summer to a decline in tropical lows and to a later seasonal breakdown of the Congo Air Boundary, the zone where moist air from the Congo basin meets drier air to its south. In their analysis, the models that project the largest increase in the Congo Air Boundary also project the most drying, so the size of the change differs widely between models.

The regional datasets show this spring signal over ESAF more clearly than any change in annual rainfall. Against the baseline of the Atlas, 1995–2014, the CMIP6 models under SSP2-4.5 give a median change of about −10% in the rain of September to November for 2041–2060, and 91% of them are drier. The CORDEX-Africa models under RCP4.5 give about −6%, with 90% of them drier (calculated from Gutiérrez *et al*., 2021; Iturbide *et al*., 2020, 2022). The IPCC's own assessment names southern Africa among the few regions in which a decrease in precipitation is expected to emerge from natural variability by mid-century, with medium confidence (Ranasinghe *et al*., 2021:1770). It also projects an increase in agricultural and ecological drought in southern Africa, with medium to high confidence (Ranasinghe *et al*., 2021:1771).

Projections downscaled for South Africa give a less uniform picture. The Green Book downscaled six global models of the previous phase, CMIP5, to a grid of about 8 km over South Africa with the conformal-cubic atmospheric model (Engelbrecht, 2019:9–10). It projects that by 2021–2050 the warming may exceed 3 °C over the northern parts of the country under high emissions (RCP8.5, which the report calls low mitigation) (Engelbrecht, 2019:12). Under the same scenario it projects more rain over the central interior and the east coast, and generally drier conditions in the western interior and the north-east in most of its runs (Engelbrecht, 2019:37). The global and the downscaled ensembles thus agree on strong warming but differ on rainfall over the interior. This is why an increase in rainfall at A31E cannot be excluded (Section 1.1).

For the upper Limpopo, Jury (2016) found little trend in observed river flow over 1959–2014, while the climate models he examined projected a decline. Because perennial surface drainage responds more than proportionally to a change in rainfall where about 500 mm falls per year (Section 1), even a modest drying could reduce the inflow to Klein Maricopoort Dam by a larger fraction. A later start to the rains would also lengthen the period in which irrigation draws on stored water before the dam is refilled. Both statements are inferences from these studies and not findings of them.

The wettest tenth of the CMIP6 models gives little more annual rain than the record, about +0.5% to +3% for 2041–2060 (calculated from Gutiérrez *et al*., 2021; Iturbide *et al*., 2020), so that a wetter outcome would lie close to the Reference run of this study. The climate cases of this study are therefore drawn from the median and the dry end of the projections (Sections 1.2 and 5.5).

## 3.8 What is known about the supply from Klein Maricopoort Dam

The only planning assessment found for the dam is the Department's strategy report for the Marico area, whose yield for the dam and whose own judgement of the hydrology behind it are given in Section 1.1 (DWAF, 2004). The report added that the hydrological information of the Marico had not been updated since 1988 and that the droughts of 1992 had not been taken into account (DWAF, 2004:83), and the systems model it proposed did not include Klein Maricopoort Dam (DWAF, 2004:84). At the level of the whole Marico sub-area, the report found a deficit of about 6 Mm³/a at a 1:50-year assurance of supply for the development of 2000, if the requirements of the Ecological Reserve were taken into account. The Department defines assurance of supply as "the reliability at which a specific quantity of water can be provided"; a 1 in 50 year risk of failure means that, on average, the quantity is not provided in one year out of fifty (DWS, s.a.a). It considered the sub-area "in balance" while the Reserve was not being implemented (DWAF, 2004:53, 93). It listed A31E among the upper catchments that "are in deficit" (DWAF, 2004:93), but at the scale of planning and not as a water balance of A31E. No statement was found in it of how often the supply from Klein Maricopoort Dam failed, of an assurance of supply for the dam on its own, or of the drought of the 1980s and 1990s at the dam.

## 3.9 Design floods and the pathways of contaminants

Flood risk is assessed from a design flood, the peak flow of a stated return period, such as the flood exceeded on average once in 100 years. Design floods in South Africa are estimated by three groups of methods (Smithers, 2012:634):
- statistical analysis of observed floods;
- deterministic methods, which convert a design rainfall into a flood;
- empirical methods, based on the largest floods recorded in a region.

Statistical analysis is the most direct. It fits a probability distribution to the largest flood peak of each year, and it is appropriate only where that record is long enough and good enough and the flood regime has not changed over it (Smithers, 2012:635–636). The records of A31E held in this study are monthly volumes, which contain no peak, so the design flood rests on the other two groups.

The Standard Design Flood (SDF) is a deterministic method intended for consistent design across the country. It is a form of the Rational Method, in which the peak flow is the product of a runoff coefficient, the intensity of the design rainfall and the catchment area. Its runoff coefficients were calibrated against the floods gauged in 29 catchments, grouped into regions (Alexander, cited by Smithers, 2012:639; SANRAL, 2013:3-43). Tested at 84 sites, the SDF exceeded the statistical estimates by 60% on average, and it is regarded as conservative (Smithers, 2012:639). Its results are therefore checked against two empirical methods:
- The Midgley and Pitman formula estimates the peak of a given return period of up to 100 years from the catchment area, the mean annual rainfall, a catchment parameter of slope and length, and a constant for the veld type of the region (Midgley & Pitman, cited by SANRAL, 2013:3-61–3-62).
- The Regional Maximum Flood (RMF) is an envelope drawn over the largest flood peaks recorded in each region of southern Africa against catchment area. It is an upper limit and carries no return period (Kovacs, 1988; Smithers, 2012:637; SANRAL, 2013:3-65).

Contaminants are approached through the source–pathway–receptor model. In this model, water is at risk from a contaminant only where a source releases it, a pathway carries it, and a receptor receives it, such as a borehole, a river or the users of a dam. A link is shown only when all three are established (Mbae *et al*., 2024).

The pathway through the ground can be traced in a groundwater flow model by particle tracking. The program MODPATH follows imaginary particles through the flows that MODFLOW has calculated between the cells of a model. To give a time of travel, it divides each flow by the area through which it passes and by the porosity of the material (Pollock, 2016:2–3). Because the particles follow the calculated flow of water and nothing else, particle tracking shows where water from a source goes and roughly how long it takes. It does not show how a dissolved substance spreads, reacts or is held back along the way. It therefore serves as a screening of pathways and not as a model of contaminant transport.

The literature reviewed therefore provides the criteria to measure the reliability of a supply (Hashimoto *et al*., 1982). It explains why multi-year droughts and reservoir evaporation govern a small dam, it gives a projected range of climate change for the region, and it provides methods by which floods and the pathways of contaminants can be screened where few records exist. It does not provide, for Klein Maricopoort Dam, a measure of how often, for how long and by how much deliveries to the canal fall below the registered volume. Nor does it show how these would change under the climate of about 2050, or whether groundwater in A31E could make up part of a shortfall. This study addresses that gap.

# 4. Conceptual model

## 4.1 The system and where its water enters

The system studied is the land between two dams, together with the upper dam that supplies it (Figure G). Water enters it in two ways that do not mix above the lower dam: as river flow from the catchments upstream, which is caught in Klein Maricopoort Dam at the boundary of A31E, and as rain on A31E itself (Section 2.1). The first feeds the canal and the irrigated land. The second can reach neither. This separation governs the rest of the account.

**[Figure G here]**
*Figure G: Schematic section of A31E along the Klein Marico River, from the wall of Klein Maricopoort Dam to Kromellenboog Dam, showing the water that enters from outside A31E (orange) and the water from rain on A31E itself (blue). Quantities are means for hydrological years 1987–2009; not to scale.*

The inflow to Klein Maricopoort Dam is taken as it is recorded, as the condition at the upstream boundary. It is not gauged (Section 2.3). When the balance of the dam is closed with the station records, it averaged about 3.3 Mm³/a over hydrological years 1987 to 2009 (DWA, 2012; DWS, s.a.c). It arrives with the rains: 64% of it came in the five months from December to April (Bailey & Pitman, 2016a; hydrological years 1981 to 2009 without 2008). From hydrological year 1982 to 1994 it stayed below its long-term median of 3.94 Mm³/a for thirteen years in succession, although rainfall in zone A3B was above its mean again in each year from 1987 to 1990 (Figure E; Bailey & Pitman, 2016a). Two explanations are possible, and both lie outside A31E. The catchments above the dam include a dolomite aquifer whose springs declined to almost nil in 1986 and stayed low for almost a decade, until the rains of 1996 (Pyburn, 2015:28, 44); if part of the river's flow comes from that aquifer, the inflow would follow groundwater storage over several years and not the rain of one season. Alternatively, more water may have been used above the dam: Pyburn (2015:4), reviewing earlier work, reports that a well field commissioned there in 1974 caused a spring to stop flowing ten years later, during a period of low rainfall. The records of the dam do not decide between the two. Whatever its cause, the low inflow is contained in the recorded sequence, and the catchments above the dam are not studied further.

**[Figure E here]**
*Figure E: Yearly rainfall in WR2012 rainfall zone A3B (upper panel) and yearly inflow to Klein Maricopoort Dam as WR2012 patched observed flow (lower panel), hydrological years 1981–2009, with the long-term mean rainfall (1920–2009) and the median inflow (1936–2009). Hydrological years 1994 and 2008 (grey) rest on patched months that the storage record of the dam contradicts (Bailey & Pitman, 2016a; DWA, 2012).*

## 4.2 Through the upper dam and along the canal

Water that reaches the dam is joined by the rain that falls on its surface, about 0.42 Mm³/a, and is held in a reservoir of 7.07 Mm³ (Section 2.1). It leaves by four routes. Over hydrological years 1987 to 2009, evaporation took 1.23 Mm³/a, a third of all the water that entered. The canal took about 1.2 Mm³/a, measured at station A3H031. A further 0.87 Mm³/a spilled over the wall, and 0.33 Mm³/a was released to the river below it; the small remainder, 0.11 Mm³/a, was a gain in storage (Table 8; DWA, 2012; DWS, s.a.c). No supply to Zeerust appears in the record. The release to the river is the least certain of these routes. Before 1987 the record carries it as a fixed entry of 44 to 48 Ml per month, which is not a measurement. From 1987 it is gauged at station A3H030, and there it rises with the level of the dam: its median was 3 Ml per month when the dam stood below 25% of capacity and 54 Ml per month when it stood at 95% or more (months without spill, 1987 to 2010). The fixed entry probably overstates the release, and with it the calculated inflow, in the years before 1987 when the dam was low.

*Table 8: Water balance of Klein Maricopoort Dam from the records, in Mm³/a, for hydrological years 1987–2009 and two parts of that period (Bailey & Pitman, 2016a; DWA, 2012; DWS, s.a.c). The inflow is the remainder that closes the balance.*

| Term | 1987–2009 (23 years) | 1987–1995 (9 years) | 1996–2009 (14 years) | Status |
|---|---|---|---|---|
| **Inflow from the river** | **3.33** | **1.23** | **4.67** | Remainder |
| Rain on the water surface | 0.42 | 0.24 | 0.53 | Calculated by the Department (rain × area) |
| Evaporation | 1.23 | 0.74 | 1.55 | Calculated by the Department (pan × area) |
| Canal (A3H031) | 1.20 | 0.30 | 1.78 | Measured |
| Spill (A3R002) | 0.87 | 0.00 | 1.43 | Measured |
| Release to the river (A3H030) | 0.33 | 0.07 | 0.49 | Measured |
| Unaccounted losses | 0.01 | 0.01 | 0.01 | Entry in the record |
| Change in storage | +0.11 | +0.36 | −0.05 | Measured (0.51 → 3.08; 0.51 → 3.71; 3.71 → 3.08 Mm³) |
| *For comparison: inflow column of the record* | 3.19 | 1.24 | 4.45 | Calculated by the Department; 16 months not calculated |
| *For comparison: WR2012 patched flow* | 3.80 | 1.43 | 5.33 | 16 patched months; 3.39 and 4.74 without 2008 |

Of the four routes, only the canal carries water to the irrigated land. The volume gauged at its head averaged 1.97 Mm³/a over the thirteen complete hydrological years between 1997 and 2014, and water entered it in every month, between 0.12 and 0.22 Mm³ per month on average (DWS, s.a.c). Beyond the gauge nothing is measured. The canal therefore ends, in this model, in three unknowns: how much is lost along it, which fields it serves beyond the land mapped as irrigated in 2022, and how much of the water applied returns to the river or sinks to the groundwater. For that reason the volume entering the canal, the registered volume and the mapped irrigated area are kept apart throughout (Section 3.4). Whatever does return to the river joins the water described next and flows to the lower dam. None of it can return to the upper dam.

## 4.3 Rain on A31E, groundwater and the lower dam

Most of the rain that falls on A31E does not become streamflow (Section 2.6). What does run off the slopes is gathered by the Doringrivier, the Waterkloofspruit and the Wilgeboomspruit, enters the Klein Marico River below the wall of the upper dam, and ends in Kromellenboog Dam. It is measured at one place only. Station A3H016 on the Wilgeboomspruit recorded a mean of 1.27 Mm³/a in its twelve complete hydrological years between 1966 and 1990, with yearly totals from zero in 1985 to at least 4.60 Mm³ in 1966 (DWS, s.a.c). For A31E as a whole, the only figure is the modelled naturalised runoff of 7.21 Mm³/a (Section 2.3). Along the way the register allows 0.751 Mm³/a to be taken from the river and its tributaries, 0.454 Mm³/a of it from the Klein Marico River itself (DWS, s.a.g); what is actually taken is not measured.

A smaller part of the rain reaches the groundwater. The national assessment models this recharge at about 29 mm/a (Table 3), which over the catchment equals the 17.336 Mm³/a of the Reserve determination (Section 1.1). The water is stored mainly in the weathered zone, and beneath the valley it lies under surface deposits of unknown thickness (Sections 2.4 and 2.5). That it moves from the high ground towards the valleys is an inference: the water level in the one borehole on the southern high ground stands more than 200 m higher above sea level than in the three boreholes near the valley (DWS, s.a.d), but these are four single levels, measured between 1974 and 1994. Groundwater leaves by three routes, none of them measured. Boreholes are registered for 0.285 Mm³/a (Table 6). Discharge to the streams is estimated at 2.00 Mm³/a in the Reserve determination (DWS, 2021), and the only sign of it in the records is the behaviour of the Wilgeboomspruit described in Section 1.1. That too is an inference, because there is no borehole near the gauge and it is not known whether water is abstracted above it. The rest of the estimated recharge, some 14 Mm³/a, is unaccounted for: it may be taken up by vegetation, it may leave the catchment underground, or the recharge may be overestimated. No record in hand decides this.

Kromellenboog Dam receives what both paths deliver (Figure H). Its own balance gives an inflow of about 6.2 Mm³/a over hydrological years 1987 to 2009 (DWA, 2012; DWS, s.a.c). Of this, 1.2 Mm³/a came down the river from the upper dam as spill and release. The remaining 5.0 Mm³/a, or 81%, is the net contribution of the reach between the dams: the runoff of A31E and any return flow from the irrigated land, less what is taken from the river and lost along it. The records cannot separate these parts. The remainder is of the same order as the modelled naturalised runoff of A31E for the same years, 6.87 Mm³/a (Bailey & Pitman, 2016a). From the lower dam the water leaves A31E: 2.2 Mm³/a evaporated, about 2.5 Mm³/a entered its canal for the scheme downstream (Section 2.1), and 2.1 Mm³/a spilled.

**[Figure H here]**
*Figure H: Conceptual model of the water system of A31E, from the inflow at Klein Maricopoort Dam to the outflow at Kromellenboog Dam, with the quantity of each flow. Quantities are means for hydrological years 1987–2009 unless another period is given; "unknown" marks a pathway for which no record exists.*

## 4.4 How the system behaves in normal, wet and dry years

In a year of ordinary inflow the upper dam roughly holds its level. In hydrological year 2000 it received 4.6 Mm³ from the river and 0.8 Mm³ as rain; it lost 2.0 Mm³ to evaporation, delivered 2.28 Mm³ to the canal and released 0.8 Mm³ to the river, and its storage rose by 0.2 Mm³ (DWA, 2012; DWS, s.a.c). With a somewhat lower inflow the balance turns negative: in 2003 an inflow of 3.2 Mm³ against a canal volume of 3.0 Mm³ and evaporation of 1.5 Mm³ lowered the storage by 1.1 Mm³. At a delivery near the registered volume the dam thus loses water in any year whose inflow is not above the median, and it depends on wetter years to recover. In a wet year most of the water cannot be kept. In 2001 the dam received 15.3 Mm³ and spilled 11.1 Mm³ of it, because it was already full; spill occurred in five of the 29 hydrological years from 1981 to 2009.

The drought shows the other side. Inflows of 2.14 Mm³ in hydrological year 1982 and 0.59 Mm³ in 1983, against canal volumes of 3.30 and 1.76 Mm³ and evaporation of 2.28 and 1.15 Mm³, took the dam from 99% of capacity in December 1982 to 22% in March 1984, a fall of fifteen months. It then stayed low for twelve years (Section 1.1). Over hydrological years 1987 to 1995 the dam received 1.2 Mm³/a from the river, half of what entered it evaporated, and the canal carried 0.30 Mm³/a. Within A31E the drought was shorter and shallower. The Wilgeboomspruit stopped in February 1984 but flowed again from April 1988, eight years before the upper dam recovered. Over 1987 to 1995 Kromellenboog Dam received 3.9 Mm³/a, of which 98% came from the reach between the dams, and its canal carried about 3 Mm³/a. Set against their areas, the catchments above the upper dam (1 157 km²) delivered about 1.1 mm/a in those years, and the reach between the dams (605 km²) about 6.3 mm/a, under the same zone rainfall of 598 mm/a. The failure of the canal supply was therefore a failure of the water that comes from outside A31E. The catchment's own runoff continued, but it enters the river below the canal and could not replace it. The upper dam recovered only with the rains of 1995 and 1996: it rose from 10% in December 1995 to 65% in February 1996 and was full in May 1997.

The parts of the system thus respond on two time scales. Rainfall, runoff, evaporation and demand follow the season: pan evaporation ranges from about 100 mm in June to about 220 mm in December and January, and the canal carries most in September, October, February and March. The storage of the dam, the inflow from upstream and, by inference, the groundwater that feeds the streams respond over several years. It is the slow parts that decide whether the canal can deliver.

## 4.5 Sources, pathways and receptors of contaminants, and floods

The account above also shows the routes along which dissolved substances would travel. They are set out here in the source–pathway–receptor form of Section 3.9: where a substance can enter the water, by which route it moves, and who or what receives it. Contaminant transport itself is not modelled. The pathways are screened in Sections 5.12 and 6.10.

Three sources can be identified from the records. The first lies outside A31E. Return flows from Zeerust and from irrigation above the dam probably reach the river upstream of Klein Maricopoort Dam (Section 2.7), and the Department also names the mines around Zeerust as a source of return flow, noting that the increased nutrient and salt content of this return flow limits its re-use (DWAF, 2004:57). The second is the irrigated land below the dam. Canal water is applied there, and the part not used by crops carries the salts it brought with it, together with anything applied to the fields, either back to the river or down to the groundwater. The third is the rest of the catchment, which had a population of 936 in 2011 (DWS, 2021:156) and in which built-up land covers only 0.3% (Section 2.7), so that it contains no large urban source of its own.

No other point source inside A31E, such as a feedlot, a mine or a waste site, is recorded in the datasets used in this study.

These sources reach A31E along the two paths of the conceptual model (Figure G). Path 1 carries the water from outside A31E. Substances that enter with the inflow are held in Klein Maricopoort Dam, where evaporation removes a third of the water that enters (Table 8) but not the salts dissolved in it, and they then travel by the canal to the fields, and by the spill and the release down the river to Kromellenboog Dam. Path 2 is that of the rain on A31E. It begins on the land surface and runs either over the ground to the streams or down to the groundwater with the recharge.

The two paths meet on the irrigated land, because canal water from path 1 is applied there and what crops do not use enters path 2. Below the fields, groundwater can discharge to the river only where the water table stands above the river bed. Where it stands deeper, the river cannot receive it, and the water leaves the water table by other routes, such as evaporation and uptake by plants. This is the question that separates the two structures of the groundwater model (Section 5.7). The route from the fields is therefore traced in both structures by particle tracking, and the water of the two paths is compared along the river with the Department's records (Section 5.12).

Four receptors follow from the paths.
- **The users of the canal** receive path-1 water directly. For them, the salt content of that water matters as water for irrigation.
- **Groundwater under the irrigated land**, which this study assesses as a backup to the canal (Section 1.1), receives whatever passes through the surface deposits, whose thickness is unknown (Section 2.4). No series of groundwater quality exists to show what it receives. For the whole of A31E, the Reserve determination gives only a median electrical conductivity of 17.7 mS/m from seven samples (DWS, 2021:163). Electrical conductivity (EC) is a measure of the salts dissolved in water.
- **The river between the dams.** The Reserve determination places an ecological flow site, Mar_EWR5, on this reach. It gives the river a present ecological state of C and sets C as the category to be maintained (DWS, 2021:130). Category C describes a moderately modified river, in which natural habitat and biota have been lost or changed to some degree (Kleynhans & Louw, 2007:A2-11).
- **Kromellenboog Dam** receives both paths and serves the irrigation scheme in A31F (DWAF, 2004:57).

How easily water from the land surface reaches the groundwater is indicated by Map 7. The DRASTIC method rates seven factors: the depth to water, net recharge, aquifer media, soil media, topography, the impact of the vadose zone and the hydraulic conductivity of the aquifer. It combines them into one index of the potential for groundwater pollution (Aller *et al*., 1987:17). The vadose zone is the unsaturated ground between the surface and the water table. The national map from which Map 7 is drawn classes the index as low (below 90), moderate (90 to 140) and high (above 140) (DWAF, cited by Esterhuyse, 2017). Of its 544 grid cells inside A31E, 96.7% fall in the low class and 3.3% in the moderate class, along the northern edge and in the north-eastern corner; none is high, the highest index being 124. Over most of A31E the index therefore gives little sign of an easy route from the land surface to the groundwater. The index is, however, drawn on a coarse national grid from regional estimates, it describes the ground and not what is done on it, and its method is intended for areas larger than 100 acres, about 40 ha, as a screening tool (Aller *et al*., 1987:1–2). It is not a measurement, and it says nothing about the surface deposits in particular, whose thickness is unknown (Section 2.4).

**[Map 7 here]**
*Map 7: Aquifer vulnerability of A31E according to the DRASTIC index (Aller et al., 1987), in the classes of the national map: low (below 90), moderate (90–140) and high (above 140) (DWAF, cited by Esterhuyse, 2017). No part of A31E falls in the high class. The index is mapped on a 1 km national grid and is not a measurement.*

Floods follow the same two paths as the water. A flood from the catchments upstream enters A31E as spill over the wall of Klein Maricopoort Dam, the tributaries add floods from A31E itself, and Kromellenboog Dam receives both. The Department identified the spillway of Klein Maricopoort Dam as "a major risk" and the spillway capacity of Kromellenboog Dam as "a major risk factor" (DWAF, 2004:170–171). A flood is also a pathway in its own right. Water that spreads over the valley floor crosses the cultivated land beside the river (Section 2.7) and can carry soil and whatever lies on it to the river. How far a design flood would spread over the reach below the Doringrivier is assessed at screening level in Sections 5.11 and 6.9.

# 5. Methodology

The canal supply is assessed with a monthly water balance of Klein Maricopoort Dam (Sections 5.2 to 5.5), and groundwater with a screening balance of volumes and a groundwater flow model used to compare cases (Sections 5.6 to 5.9). Flood risk along one reach of the Klein Marico River and the pathways of contaminants are assessed at screening level (Sections 5.11 and 5.12). Both rest on the conceptual model of Section 4, which sets out what each must represent. Only monthly records are used.

## 5.1 Records and their quality

The records are those of Table 1, and they come from three custodians. The station records of the Department of Water and Sanitation give one volume or depth per month, each with a quality code (DWS, s.a.c). The reservoir record of the dam gives, for every month from June 1936 to November 2010, the storage, the outflows, the volumes of evaporation and rain that the Department calculated for the water surface, and the inflow that it calculated from these (DWA, 2012). The WR2012 study supplies the rainfall of zone A3B and the patched observed inflow (Bailey & Pitman, 2016a). The groundwater records are described in Section 5.8. The catchment datasets other than the station and reservoir records, namely the WR2012 series for A31E, the regional groundwater values, the register of water use and the borehole records, were accessed through the Hydrogeological Repository; each is cited to its custodian.

A quality code states how the Department processed a monthly value. Table 9 gathers the codes into five groups, from values accepted as recorded ("good") to months without a usable value ("gap or missing"). "Estimated or derived" covers values that were not recorded directly, and "minimum or above rating" marks a month in which the flow exceeded what the gauge can measure, so that the true volume is at least the value shown.

*Table 9: Share of the months of each station record in each group of DWS quality codes, over the whole period of the record given in Table 1 (calculated from DWS, s.a.c). A code that is not in the Department's list covers a further 0.3% of the months of A3R002 and 4.7% of those of A3R003.*

| Record | Months | Good (%) | Edited or checked, not yet audited (%) | Estimated or derived (%) | Minimum or above rating (%) | Gap or missing (%) |
|---|---|---|---|---|---|---|
| A3R002, spill | 1 081 | 84.2 | 7.5 | 3.9 | 0.0 | 4.2 |
| A3H031, canal | 1 080 | 75.6 | 9.3 | 10.2 | 0.0 | 5.0 |
| A3H030, river below the dam | 292 | 71.9 | 11.0 | 2.1 | 12.3 | 2.7 |
| A3H042, river below the dam | 174 | 26.4 | 27.0 | 0.0 | 0.0 | 46.6 |
| A3E003, rainfall | 690 | 83.3 | 8.1 | 0.0 | 0.0 | 8.6 |
| A3E003, S-pan evaporation | 689 | 37.2 | 10.4 | 43.5 | 0.0 | 8.9 |
| A3H016, Wilgeboomspruit | 321 | 79.4 | 0.0 | 0.0 | 1.9 | 18.7 |
| A3R003, spill | 858 | 82.6 | 8.5 | 2.1 | 0.0 | 2.1 |
| A3H033, Kromellenboog canal | 858 | 79.8 | 10.6 | 1.5 | 0.1 | 7.8 |
| A3H032, river below Kromellenboog Dam | 560 | 67.7 | 17.1 | 1.6 | 0.4 | 13.2 |

Three features of Table 9 shape the method. The spill and canal records at the upper dam are mostly good, which is why the canal record can serve to derive and test a restriction rule (Section 5.3). The pan record is the weakest, with 43.5% of its months estimated, so the water balance uses the mean pan depth of each calendar month (Section 5.2). And station A3H030 below the dam measures low flows only, so that its months of spill give a minimum. Station A3H042 lies after the period of the water balance and is not used in it. A code does not show that a value is right, and the records were therefore also compared with one another.

Four rules follow from that comparison and are applied throughout. First, a value printed beside a gap code is a part-month and not a monthly total, and such months are treated as gaps. Table 1 counts them among the months with a value, which is why its shares are higher than those of Table 9. Second, a yearly total is counted only for a hydrological year in which every month has a value without a gap code; six years of the canal record are left out for this reason (1983, 1994, 2002, 2012, 2013 and 2023). Third, three periods are doubtful although their codes are good: the calculated inflow of hydrological years 1975 to 1980, which totals 296 Mm³ against 186 Mm³ at Kromellenboog Dam downstream, the spill record of October 1977 to September 1979, and the canal record of January 2018 to May 2021, which repeats one flow rate (DWA, 2012; DWS, s.a.c). The Department has not confirmed these readings. Fourth, the thirteen months in which the reservoir record carries a storage of zero under a missing-value flag are gaps and not an empty dam. The reservoir record and the WR2012 series carry flags of their own, for which no legend was obtained, and they are not part of Table 9.

One further point concerns the drought itself. The canal volumes of September to November 1983 and February 1984 to July 1989 carry the code "height derived from flow" (DWS, s.a.c), so the first five and a half years of the long shortfall are recorded as derived values.

## 5.2 Monthly water balance of Klein Maricopoort Dam

A monthly water balance of Klein Maricopoort Dam and its canal was built in Microsoft Excel (Microsoft 365) from the station and reservoir records. It is a mass balance of one reservoir with a restriction rule, the form that Adeloye *et al*. (2016) use to calculate reliability, resilience and vulnerability for a single dam. A simpler storage–yield calculation leaves out evaporation, which took a third of the water that entered this dam (Table 8), and has no restriction rule, so it cannot give the duration or depth of a shortfall. A river-system model such as that applied by Dlamini *et al*. (2023) adds components for which no record exists here: the system is one dam and one canal.

In each month the storage at the end equals the storage at the start, plus the inflow from the river and the rain on the water surface, minus evaporation, the release to the river, the canal delivery and the spill. The balance runs in Mm³ over the 888 months from October 1936 to September 2010, the period in which the inflow, the storage and the canal are all recorded. The present dam, with its capacity of 7.07 Mm³, is applied to every year, although the dam was raised in 1966 (Section 2.1). The results therefore describe the present dam and the present registered volume under the inflows of the past; they are not a reconstruction of history. The run starts from a storage of 3.92 Mm³, the 55.5% of its capacity that the dam held on 1 October 1936. Table 10 sets out how each term is obtained.

*Table 10: The terms of the monthly water balance of Klein Maricopoort Dam and how each is obtained.*

| Term | Obtained each month as | Record |
|---|---|---|
| Inflow from the river | The remainder that closes the dam's recorded balance (843 months); rebuilt from the station records (27); WR2012 patched value (18) | DWA (2012); DWS (s.a.c); Bailey & Pitman (2016a) |
| Water-surface area | Read from a storage–area curve of eleven points, at the storage of the start of the month | DWA (2012) |
| Rain on the water surface | Rainfall of zone A3B in that month × area | Bailey & Pitman (2016a) |
| Evaporation | Mean S-pan depth of the calendar month × pan factor × area | DWS (s.a.c), station A3E003; DWA (2012) |
| Release to the river | Read from a table of the mean gauged release in nine bands of storage | DWS (s.a.c), station A3H030 |
| Canal delivery | Registered volume of the month × the share allowed by the restriction rule (Section 5.3), limited to the water above the lowest usable storage | DWS (s.a.c), station A3H031; DWS (s.a.g) |
| Spill | Whatever exceeds 7.07 Mm³ at the end of the month | DWA (2012) |

**The inflow.** The inflow of a month is the remainder of the dam's own balance: the change in storage plus all outflows and evaporation, less the rain. Where an outflow entry is missing, the balance was closed with the station records, and where the storage or the spill is not recorded, the WR2012 patched value was used (Table 10). The patched series was not used throughout because several of its patched months contradict the storage record: it gives 11.61 Mm³ for January to March 2009, for example, while the storage rose by 2.73 Mm³ and nothing spilled (Bailey & Pitman, 2016a; DWA, 2012). The doubtful years 1975 to 1980 stay in the sequence, so that storage remains continuous, and every result is given with and without them.

Because the inflow is a remainder, an error in a recorded outflow passes into it. From October 1966 to January 1987 the record carries the release to the river as a fixed entry of 44 to 48 Ml per month, which probably overstates the release when the dam was low (Section 4.2). A second, adjusted inflow series was therefore built, in which this entry is replaced by the release that the gauge later measured at the same storage; it lowers the inflow of hydrological years 1983 to 1986 from 0.98 to 0.66 Mm³/a. Before 1966 the dam had another wall, and no adjustment can be defended. The series as recorded is the primary one, and the adjusted series is run as a check.

Over all 74 years the series has a median of 3.71 Mm³/a, against 3.94 Mm³/a for the WR2012 patched flow quoted in Section 1.1.

**Area, evaporation and rain.** No table of the water-surface area below full supply was available, so the area was derived as the slope of the relation between the gauge reading and the contents of the dam in the reservoir record since the survey of 1982. At full supply it returns the surveyed 136.80 ha within 0.2 ha (DWA, 2012). At a quarter of its capacity the dam still exposes nearly half of its full surface, which is why evaporation remains a large loss in a drought. The area is taken at the start of each month, as in the reservoir module of the WR2012 model (Bailey & Pitman, 2016b:10).

Evaporation is calculated from the twelve mean monthly depths of the S-pan at the dam shown in Figure B, which total 1 993.8 mm/a (the mean of the 42 complete years is 2 005 mm/a; Section 2.2). The WR2012 model likewise uses "a set of twelve monthly pan values and associated pan factors" (Bailey & Pitman, 2016c:xvi). A pan factor converts the depth lost from the pan into the smaller depth lost from open water. The published table of monthly factors for the S-pan (Midgley *et al*., cited by Parsons & Vermeulen, 2017:44) could not be consulted, so the factors were back-calculated from the Department's own evaporation volumes for this dam: each is the median, for one calendar month, of the evaporation volume divided by the pan depth and the area, from October 1982 to September 2010. They range from 0.82 to 0.89 and give an open-water evaporation of 1 687 mm/a, or 2.31 Mm³/a from a full dam. Applied to the twelve mean depths, they give 2.6% more evaporation than the Department's column over the same period, which lies inside the range of ±10% tested in Section 5.4. Rain on the water surface is the monthly rainfall of zone A3B (Section 2.2) times the area; it gives 5.7% more rain than the Department's column, on a term of about 0.4 Mm³/a.

**Demand.** The canal is asked to deliver the registered scheme volume of 2.34 Mm³/a (Section 2.7). The canal record supports this as the present level of demand: in the 40 months of 1987 to 2009 in which the dam stood at 85% or more, the canal carried 7.59 Mm³ against 7.73 Mm³ registered for those months (DWA, 2012; DWS, s.a.c). The registered volume is divided over the year in the pattern of Figure C.

**[Figure C here]**
*Figure C: Average monthly volume in the canal from Klein Maricopoort Dam (DWS station A3H031), hydrological years 1997–2014 without 2010.*

Figure C shows that the demand has no season of rest: water entered the canal in every month, and about a third of the yearly volume (32%) is asked for from June to September, when almost no inflow arrives (Section 4.1). The dam must therefore carry the scheme through every winter on the water stored in summer. The pattern has not always been the same. In full-dam months of 1966 to 1986 the canal carried 57% of its yearly volume from June to September. The present pattern is applied to all years, like the present dam, and the older one is tested as a sensitivity case. The same volume is asked for every year, although real demand rises in dry years; this is a stated simplification. Two further demands are run: 2.73 Mm³/a, the irrigation demand that the WR2012 study assigns to the dam, as the upper case, and a series from 0.5 to 3.0 Mm³/a in steps of 0.25, which gives a curve of reliability against demand. The shortfall of a month is the registered volume of that month less the simulated delivery, measured at the head of the canal, and is called a shortfall against the registered volume throughout.

**The other outflows.** The release to the river is read from a table of the mean release gauged at station A3H030 in nine bands of storage (Figure I, upper panel, in Section 5.3). A table was preferred to a fitted curve because it is not known what the release is, whether an outlet, a compensation release or leakage, so that no form of curve can be justified. The table returns the recorded total within 0.2%, and a table built from the even years returns 0.96 of the total of the odd years. The canal receives nothing once the storage reaches 0.166 Mm³, the lowest storage on record, because the level of the outlet is not known. No supply to Zeerust is included, as none is recorded (Section 4.2).

Two checks were made on the construction. With the recorded outflows and the Department's own evaporation and rain volumes, the balance returns the recorded storage within 0.002 Mm³ in each of the 843 months, which shows only that it is built correctly. The whole balance was also recalculated independently for every run, with no difference in any month.

## 5.3 Test of the restriction rule

No operating rule of the scheme could be obtained. What the canal receives when the dam is low was therefore derived from the records, as Coerver *et al*. (2018) do for reservoirs whose rules are unknown. The rule is a table that gives, for the storage at the start of a month, the share of that month's registered volume that the canal receives. It has seven zones, with limits at 7, 14, 21, 35, 57 and 85% of the full capacity. The share of a zone is the canal volume delivered, divided by the volume asked for, summed over all months whose starting storage lay in that zone. Nothing is optimised.

The record of the raised dam was split in two. The rule was fitted on hydrological years 1966 to 1974 and 1981 to 1986 (178 months with both a storage and a canal record; the doubtful years are left out) and tested on hydrological years 1987 to 2009. The split falls at 1987 because from that year every outflow of the dam is measured and one surveyed capacity applies, the canal carried the registered volume when the dam was full, and each period holds the whole range of storage. In the earlier period the canal carried more than the present registered volume, so its shares are measured against that period's own full-dam deliveries.

**[Figure I here]**
*Figure I: Upper panel: monthly release to the river below Klein Maricopoort Dam (DWS station A3H030) against the storage at the start of the month, 1987–2010 (259 months without spill), with the mean of each storage band. Lower panel: share of the registered volume that the canal received in each storage zone, in the fit period (hydrological years 1966–1974 and 1981–1986), in the test period (1987–2009) and in both together (the rule used).*

The lower panel of Figure I shows that the two periods have the same shape: below 14% of capacity the canal received almost nothing in either, and above that the share rises with storage. In the middle zones the earlier period delivered more. Restriction thus began earlier and went deeper after 1987, or less water was wanted; the records cannot tell these apart (Section 5.4). A rule taken from one period will not hold exactly in the other, and the test measures by how much.

The comparison with the records was made in three steps, of which only the third is a test. The first is the arithmetic check of Section 5.2. In the second, the canal stays as recorded while the other terms come from the rules of Table 10, which shows whether those rules reproduce the storage record. In the third, the canal is driven by the registered volume, the pattern of Figure C and the rule of the fit period, and the simulated monthly storage, monthly canal volume and yearly canal volume are compared with the record of the test period.

Three measures of fit are used (Moriasi *et al*., 2007:887–888). The Nash–Sutcliffe efficiency (NSE) compares the errors of the model with the spread of the record around its own mean: 1 is a perfect fit, and 0 means that the model is no better than that mean. The RSR is the root-mean-square error divided by the standard deviation of the record, so that 0 is a perfect fit. The percent bias (PBIAS) is the recorded total less the simulated total, as a percentage of the recorded total. Moriasi *et al*. (2007:891) regard a simulation as satisfactory when the NSE is above 0.50, the RSR is 0.70 or less and the PBIAS lies within ±25%. These values were set for monthly streamflow from catchment models, and applying them to reservoir storage and canal deliveries is a choice of this study; Coerver *et al*. (2018) do judge simulated reservoir releases by the NSE. It was decided before the test that monthly storage and yearly canal volume must meet all three values. Monthly canal volume was expected to be weaker, because the balance asks for the same volume in the same calendar month of every year while real demand moves with the rain.

The test has limits. The inflow itself cannot be tested, because it was calculated from the storage record that the balance is compared with. The area curve, the pan factors and the release table come from the test period, so only the rule and the demand are tested independently. And passing a split test of this kind is "a necessary, rather than a sufficient, condition" for a model to be adequate (Klemeš, 1986).

After the test, the rule was fitted once more on both periods together, and this rule is used in all further runs. From the lowest zone to the highest its shares are 0.036, 0.116, 0.298, 0.666, 0.782, 1.000 and 1.000. No share may exceed 1.00, and the share of the top zone, 0.993 from the records, was set to 1.00, because a lower value would count every month with a full dam as a failure.

## 5.4 Reliability, resilience and vulnerability; the two bounds

The supply is judged by the criteria of Hashimoto *et al*. (1982) introduced in Section 3.1, calculated with the formulas of Adeloye *et al*. (2016) (Table 11). A month fails when the simulated delivery is below 99% of the registered volume of that month; the margin of 1% keeps rounding from counting as failure.

*Table 11: The criteria by which the canal supply is judged (Adeloye et al., 2016; Hashimoto et al., 1982:16–17). D is the registered volume of a month and C the simulated delivery.*

| Criterion | Calculated as | What it says |
|---|---|---|
| Reliability by time | Months without failure ÷ all months | How often the registered volume is delivered |
| Reliability by volume | Sum of C ÷ sum of D | What share of the registered volume is delivered |
| Yearly reliability | Hydrological years with at least 99% of the yearly volume ÷ all years | In how many years the scheme receives its volume |
| Resilience | Number of shortfall events ÷ number of failure months | The inverse of the mean length of an event |
| Vulnerability | Mean of (D − C) ÷ D over the failure months | How deep a shortfall is on average |

A shortfall event is an unbroken run of failure months, described by its first month, its length, its total shortfall and its mean shortfall as a share of the registered volume. The number of months with less than half the registered volume is counted as well, because a restriction rule produces many small shortfalls and few deep ones. The yearly reliability is the figure closest to the assurance of supply defined in Section 3.8, but it is a frequency counted in one record and not a probability from a risk analysis. Every criterion is calculated over all 74 years and over the 68 years without 1975 to 1980.

Kjeldsen and Rosbjerg (2004) found the estimation of these criteria from a single historical series "problematic" and recommend long synthetic series. Synthetic series would need a stochastic model of an inflow whose behaviour in the drought is unexplained (Section 4.1). They are not used here, and the limit is stated with the results.

**The two bounds.** The records cannot tell a month in which the canal was restricted from a month in which less water was wanted, so a rule derived from them may restrict more than the scheme's managers did. Every run is for that reason made twice. In the run with the rule, the canal receives the share of Section 5.3; this is the lower bound of reliability. In the run without restriction, the canal receives the full registered volume for as long as water stands above the lowest usable storage; this is the upper bound. The two bound how often the supply fails, not how deep a failure is: a rule that restricts early spreads a shortage over many months of partial delivery, whereas an unrestricted canal delivers in full until the dam is empty and then receives nothing. The bounds are therefore always reported together.

**Sensitivity.** One input is changed at a time from the Reference run while all others are kept fixed (Pianosi *et al*., 2016:215), which does not show how inputs act together. The inputs are the demand (Section 5.2); the second inflow series; open-water evaporation ±10%, because the yearly pan totals vary by 9%; capacity −10%, because the surveys of 1976 and 1982 differ by 12% and none has been made since; the release to the river halved and raised by half; the rule of each single period; the older seasonal pattern; a lowest usable storage of 0 and of 0.5 Mm³; and a full and an empty dam at the start.

## 5.5 Climate cases

The effect of climate change is assessed with two cases for about 2050, set against the Reference run (Table 12). Case M represents the median of the published projections, and case D their dry end. Both are taken from the projections for 2041–2060 over the region ESAF (Sections 1.1 and 3.7), expressed against the mean climate of hydrological years 1937 to 2009. This is the climate of the record on which the Reference run rests.

*Table 12: The climate cases for about 2050 and their grounding in the projections for ESAF, 2041–2060, against the mean climate of hydrological years 1937–2009 (calculated from Gutiérrez et al., 2021; Iturbide et al., 2020). Each factor multiplies the value of the Reference run. Rain on the dam is as recorded in every case. The recharge factors apply to the groundwater model (Section 5.9).*

| Case | What it represents | Warming | Annual rain | Inflow | Evaporation depth and demand | Recharge |
|---|---|---|---|---|---|---|
| Reference | The climate of the record | – | – | 1.00 | 1.00 | 1.00 |
| M | Median of the models under SSP2-4.5 | +1.9 °C | −3.1% | 0.93 | 1.064 | 0.96 |
| D | Median warming with the 10th percentile of the projected rainfall | +1.9 °C | −8.5% | 0.80 | 1.064 | 0.89 |

Case D keeps the median warming because the projected warming is narrow in range, whereas the rainfall is uncertain even in sign (Section 1.1). D therefore isolates the effect of a drier outcome. The rainfall of D is the 10th percentile of the models under SSP2-4.5, the value below which a tenth of them lie. Under SSP5-8.5 the same percentile is −7.9%.

The changes in climate were converted into the factors of Table 12 in three ways.

**Inflow.** The inflow factor follows from the rainfall elasticity of the inflow, the percentage change in streamflow for a change of one per cent in rainfall (Sankarasubramanian *et al*., 2001:1772–1773). It was estimated with the non-parametric estimator of Sankarasubramanian *et al*. (2001:1775), which is the median over all years of the yearly change in flow relative to its mean, divided by the yearly change in rainfall relative to its mean. The estimator was applied to the WR2012 patched observed inflow to Klein Maricopoort Dam and the rainfall of zone A3B (Bailey & Pitman, 2016a). It gives 2.5 over the 74 years from 1936 to 2009, and 2.0 over the 68 years without 1975 to 1980. A change of −3.1% in rainfall therefore gives about −7% in inflow. A change of −8.5% gives −17% to −21%, of which −20% is used for case D. The low inflow of 1982 to 1994 was not caused by low rainfall (Section 4.1), so this elasticity is an approximate scaling and not a property of the catchments above the dam.

**Recharge.** The recharge factor follows from the finding that long-term recharge across Africa rises with long-term rainfall to a power of about 1.34 to 1.39 (MacDonald *et al*., 2021). This gives about −4% in case M and about −11% in case D. The relation uses differences between places to stand for a change over time.

**Evaporation depth and demand.** Warming raises the water requirement of irrigated crops and the evaporation from the dam through the same evaporative demand (Section 1.1), so the evaporation depth takes the same factor as the demand. A step of 3.2% to 4% per °C lies within the "about 1.5–4% °C⁻¹" projected for potential evapotranspiration (Scheff & Frierson, 2014). Applied to 1.9 °C, it gives the factor of 1.064. That range was derived for a reference crop and not for open water. Cullis and Phillips (2019:25) likewise scale supply by the change in runoff and demand by the change in potential evaporation.

In each case every month's inflow and evaporation depth, and the yearly demand, are multiplied by the factors of Table 12, and everything else stays as it is. A shortfall is then measured against the registered volume raised by the demand factor of the case. Each case is run for both bounds and on both inflow series.

Three properties of this method govern how the cases are read:
- **A uniform factor keeps the recorded sequence of wet and dry years.** Droughts become deeper, but not longer or more frequent, although more frequent and longer droughts are what is projected for the region (Section 1.1).
- **It cannot represent a later start of the rains.** The clearest rainfall signal in the projections is a decrease of about a tenth in the rain of September to November (Section 3.7). That decrease would lengthen the period in which the canal draws on the dam before the first inflow, which a factor applied to every month cannot reproduce.
- **It probably understates the reduction in long droughts.** In long droughts runoff tends to fall below what the earlier relationship between rainfall and runoff predicts: of 73 significant shifts found in south-eastern Australia, 68 were towards less runoff (Saft *et al*., 2015).

For all three reasons, the cases probably understate the loss of reliability in the driest years, which are the years that decide it.

## 5.6 Screening balance of volumes

Before a flow model is used, the size of the shortfall is set against the groundwater of A31E in a balance of volumes, the form in which the Reserve determination assesses groundwater in each quaternary catchment (DWS, 2021). The determination gives three volumes for A31E. The recharge is 17.336 Mm³/a, a modelled value. The groundwater part of the Reserve, the quantity set aside by law for basic human needs and for aquatic ecosystems, is 1.26 Mm³/a. Current groundwater use is estimated at 0.81 Mm³/a, of which 0.285 Mm³/a is registered (DWS, s.a.g). The remainder is about 15.3 Mm³/a.

Three volumes from the water balance of the dam are set against these, each for both bounds:
- the mean shortfall against the registered volume, which is one minus the reliability by volume over 74 years, times the registered volume and the demand factor of the case;
- the rate during the longest shortfall event of the Reference run, which is its total shortfall divided by its length;
- the whole registered volume, as the upper limit.

Each is expressed as a share of the recharge and as a continuous rate in litres per second, which is compared with the strike yields that the National Groundwater Archive records for boreholes inside A31E (Section 2.5). This comparison indicates scale only: a strike yield is not a yield that a borehole can sustain, a recorded zero may mean that no yield was recorded, and the boreholes were not drilled where a scheme would need them.

The balance can show whether the shortfall is small against the modelled recharge of the whole catchment. It cannot show that the water can be taken where and when it is needed, and it treats the recharge as water that is free to take. That assumption does not hold. The land mapped as irrigated in the strip below the dam, 162.5 ha, receives about 0.05 Mm³/a of recharge at the modelled rate, so that any abstraction of the size of the shortfall must draw its water from well beyond the fields. Water pumped over a long period is also balanced mostly by "capture", that is, by less groundwater discharge elsewhere: in the aquifer systems reviewed by Konikow and Leake (2014), capture accounted for about 0.85 of long-term withdrawals. Only a flow model can show which discharge is reduced, and for this reason objective 4 calls for one.

## 5.7 Groundwater model: structure S and structure D

**Choice of method.** Analytical solutions for the drawdown and the loss of streamflow near a pumped borehole need the transmissivity, the storage and the distance to the stream (Leake & Barlow, 2013), none of which is measured in A31E, and a transient model such as that of Ebrahim *et al*. (2019) needs water-level series and storage values, which A31E lacks (Section 2.5). The model is therefore run at steady state: it calculates the one state in which the water entering the aquifer equals the water leaving it, which stands for a long-term mean. Cases are then compared with one another, as Woldeamlak *et al*. (2007) did for wetter and drier conditions and Jovanovic *et al*. (2017) for low and high abstraction.

By the Australian groundwater modelling guidelines, a model with few, poorly distributed water levels and a steady-state calibration only belongs to Class 1, the lowest class of confidence (Barnett *et al*., 2012:20–21). The uses that the guidelines list for this class include understanding flow processes under hypothetical conditions and developing coarse relationships between extraction and impact. That is what objective 4 asks, and no more is claimed.

**The model.** The model was built and calibrated in GMS 10.9.6 and run with MODFLOW-NWT (Niswonger *et al*., 2011). This version of MODFLOW solves the flow equation with a Newton method that keeps a cell in the calculation when its water level falls. The results are differences between cases, so the water budget of every run must close; it closes to 0.00% in all of them. Every run used the same settings: a head tolerance of 0.0001 m, a flux tolerance of 10 m³/d, up to 3 000 outer iterations and the solver option for complex problems. Table 13 sets out the model.

*Table 13: The groundwater model of A31E: what is common to the two structures and what differs.*

| Feature | Structure S | Structure D |
|---|---|---|
| Area and grid | A31E: 15 142 active cells of 199.4 m by 198.9 m (600.5 km²), in 145 rows and 222 columns | The same |
| Layer | One layer; top at the land surface of the elevation model of Map 2, bottom 207.5 m below it; transmissivity changes with the saturated thickness | The same |
| Recharge | 29.2 mm/a on every cell, 17.53 Mm³/a in all | The same |
| Outer edge | Closed | The same |
| River drains | The four named rivers of Map 2: 575 drain entries in 531 cells; conductance 10 m²/d per metre of channel | The same |
| Stream drains | All other mapped streams, 555.6 km: 4 239 drain entries in 3 395 cells; conductance 10 m²/d per metre of channel | The same |
| Ground drain | In every active cell, 0.05 m²/d per m²; 1 m below the land surface | The same, but 15.27 m below the land surface |
| Hydraulic conductivity | Two zones: surface deposits (3 479 cells) and bedrock (11 663 cells); estimated with PEST (Section 5.8) | The same zones; estimated again with PEST, on the same targets and within the same limits |

A cell is active when its centre lies inside A31E. The single layer takes its thickness from the depth to the base of the fractured zone in the national assessment (Table 3), which is a modelled mean and not a measured thickness. The recharge is that of the same assessment and agrees with the 17.336 Mm³/a of the Reserve determination within about 1%. The hydraulic conductivity, in metres per day, describes how easily the rock passes water; multiplied by the saturated thickness it gives the transmissivity of Table 3. Two zones of conductivity follow the geology of Map 3: the surface deposits form one zone, and all other rock groups form the bedrock zone. No groundwater enters or leaves the model across its closed outer edge.

Water leaves the model only through drains. A drain removes water from a cell whenever the water level stands above the level of the drain, at a rate proportional to the height of the water level above it, and it never adds water (Harbaugh, 2005). Three groups are used. The river drains follow the four rivers of Section 2.3: the Klein Marico River from 300 m below the dam wall to Kromellenboog Dam, the Doringrivier, the Waterkloofspruit and the Wilgeboomspruit. Their level was set at points along each river (its ends, its junctions and each crossing of a 20 m contour) as the lowest land surface beside the channel, with straight lines between the points. It lies a median of 5.2 m below the top of the cell. The stream drains follow all other mapped streams, at the land surface along the stream line, a median of 3.3 m below the top of the cell. All of these channels join the Klein Marico River above Kromellenboog Dam. The ground drain lies under every cell and stands for seepage, springs, evaporation and uptake by plants from the water table, taken together. It is needed because the bedrock passes too little water sideways to carry the recharge of a whole hillside to the streams.

**The two structures.** The two structures differ in one input, the depth of the ground drain, and in the conductivities that follow from it. In structure S the ground drain lies 1 m below the land surface, an assumed depth. In structure D it lies 15.27 m below the land surface. This is the median depth to water of 112 water levels of the National Groundwater Archive in A31E and its neighbouring catchments (DWS, s.a.d). The value was taken from this regional set so that the comparison with the levels inside A31E (Section 5.8) is not circular. An outflow at that depth is physically possible: the maximum rooting depth of tropical grassland and savanna averages 15.0 m worldwide (Canadell *et al*., 1996), and natural woodland and grassland cover 87% of A31E (Section 2.7). That such uptake takes place in A31E is not shown.

Both structures are needed because the records contradict each of them in a different respect (Section 6.5). Structure S holds the water table within a few metres of the surface in the valleys, where the levels recorded in boreholes lie far deeper. Structure D sends almost no groundwater to the streams, less than any estimate of baseflow. The real catchment lies between the two, and the records cannot place it. The guidelines state that "Multiple conceptual models should be developed where a single conceptual model cannot be identified based on the available data" (Barnett *et al*., 2012:26). The two structures are therefore run through the same cases and are always reported together, as the two bounds of the groundwater result.

## 5.8 Calibration and comparison with the archive levels

**Targets.** A model is calibrated by adjusting its parameters until the simulated water levels agree with measured ones. The targets are the four static water levels of Table 4. The observed head of a borehole is its ground level, read from the elevation model of Map 2, less the recorded depth to water. A residual is the observed head less the simulated head, so that a negative residual means that the measured water table lies deeper than the model's.

Each target carries a calibration interval of 10 m at 95% confidence (a standard deviation of 5.1 m), which states how well an observed head is taken to be known and was set from the records and not from the fit. The ground levels come from an elevation model with cells of about 20 m, at positions that for most boreholes were read from 1:50 000 maps, and single water levels in boreholes that share one map position differ by about 11 m, as a standard deviation.

**Estimation.** Only the two conductivities were estimated. The recharge was held at its regional value, because recharge and hydraulic conductivity are correlated in a calibration: Knowling and Werner (2016) concluded that estimating steady-state recharge in this way “may be impractical for real-world settings”. The estimation was made with PEST, a program that changes the parameters step by step until the objective function, called phi, is as small as it can be made (Doherty & Hunt, 2010); phi is the sum of the squared residuals, each divided by the square of the standard deviation of its target. Both conductivities were estimated as logarithms, between limits of 0.03 and 3.0 m/d for the surface deposits and 0.0005 and 0.05 m/d for the bedrock.

For structure S, initial estimates of 0.508 m/d for the surface deposits and 0.0032 m/d for the bedrock were refined with PEST. PEST changed them by 15% and 9%, to 0.430 and 0.0029 m/d, and lowered phi by 0.2%. The four levels thus constrain the two conductivities only weakly, and the values cannot be regarded as determined by them.

Structure D was calibrated on equal terms: the same four targets, interval, parameters, limits and PEST settings. Two PEST runs were made, one starting from the values of S and one with the bedrock conductivity at a quarter of that value, to show whether the outcome depends on the starting point. The run with the lower phi was to be taken; where the two runs end at the same phi with a parameter at its limit, that parameter is reported as a limit and not as an estimate.

**What the fit can and cannot show.** The fit is reported as the mean residual and the root mean square of the residuals, for all four boreholes and without borehole 2526AD00180, always together. No value is claimed as acceptable: a common target, a root mean square of 5% or 10% of the range of observed heads, is meaningful only where it is known to be achievable (SKM, 2013:17), and the range of 286 m is here the relief of the catchment.

The fit is set beside a benchmark, the simplest possible guess: a water table that lies 15.27 m below the ground everywhere. A model that fits the levels no better than this guess has not shown that the levels inform its parameters.

The fit is not a validation. All four levels were used to fit two parameters, so none remains independent, and a formal verification is advised only where a large quantity of data exists (SKM, 2013:18). Three of the four levels were also measured in 1990 and 1994, when Klein Maricopoort Dam stood at 12% to 14% of its capacity (Section 2.5), so the targets may lie below the long-term mean that a steady-state model represents.

**The other archive levels.** The archive holds 262 further water levels inside A31E, whose status is not recorded (Section 2.5). They are not used in the calibration but are compared with both structures afterwards, as the only water levels left by which either can be judged. The observed head is formed in the same way as for the targets, and the simulated head is interpolated at the borehole. Four things are reported, each beside the benchmark: the residuals by borehole; the residuals by location group, because the 262 levels lie in 52 groups of boreholes within 50 m of each other, which share a map position and a model cell; the mean residual in four bands of ground level; and the number of boreholes with a water level shallower than 5 m, measured against simulated.

This comparison is not a validation either. The scatter of the levels inside the groups, about 11 m, is a floor below which no model with cells of 200 m can fit them, and some levels may have been measured during or soon after pumping, which would make them too deep and favour structure D unfairly.

## 5.9 Groundwater cases and what is read from them

**Base case and check.** The base case of each structure is the calibrated model without wells. Registered borehole use was run once as a check and not as a case. It takes the 28 borehole records registered inside A31E, 0.265 Mm³/a at 27 registered positions (DWS, s.a.g), as constant rates. A registered position is not a borehole and a registered volume is not abstraction. The run shows only whether registered use would move the simulated heads at the four targets.

**Abstraction cases.** As with the curve of reliability against demand, a series of rates is run and not one case per shortfall: 0.25, 0.5, 1.0, 2.0 and 2.34 Mm³/a. Every volume of Section 5.6 lies on this curve. The mean shortfall is the volume that fits a steady-state model best, because both are long-term averages.

The model cannot show how many boreholes are needed or where, so the abstraction is placed by a geometric rule and spread evenly over the cells (Table 14). Placement P1 is the 45 cells whose centre lies on land mapped as irrigated in the strip below the dam, 41 on surface deposits and 4 on bedrock. Placement P2 is the 474 cells of surface deposits within 1 km of that land, and tests whether spreading the abstraction changes the result. Placement P3 is the 410 bedrock cells within the same 1 km.

*Table 14: The runs made with each structure. P1, P2 and P3 are the placements of the abstraction; rates in Mm³/a.*

| Run | S | D |
|---|---|---|
| Base case, without wells | Yes | Yes |
| Registered borehole use (check) | Yes | Yes |
| P1 at 0.25, 0.5 and 1.0 | Yes | Yes |
| P1 at 2.0 | No | Yes |
| P1 at 2.34 | Yes | Yes |
| P2 at 0.5 | Yes | Yes |
| P2 at 2.34 | Yes | No |
| P3 at 0.5 | Yes | No |
| Recharge × 0.96 and × 0.89, without wells | Yes | Yes |
| Recharge × 0.96 and × 0.89, with P1 at 0.5 | Yes | Yes |
| The conductivities of S in structure D, without wells and with P1 at 0.5 | – | Yes |

**What is read from each case.** Four results are read, each against the base case of the same structure and the same recharge.
1. **The rate pumped.** MODFLOW-NWT reduces the rate of a well once the water level in its cell falls into the lowest 5% of the layer (Niswonger *et al*., 2011), so the rate pumped is taken from the water budget and not from the rate entered.
2. **The drawdown.** This is the head of the base case less the head of the case: its mean and its largest value in the pumped cells, and the area in which it exceeds 1 m and 5 m.
3. **The number of pumped cells in which the water level falls more than 47.5 m below the land surface.** This is the depth that the national assessment gives for the base of the weathered zone (Table 3; DWS, s.a.b), in which most of the groundwater is stored (Section 2.5). The number is reported as a count for comparing cases and never as a prediction.
4. **The change in the outflow of each group of drains, as a share of the rate pumped.** At steady state these shares add up to 100%; they show which discharge the abstraction captures. A reduction in the river or stream drains is water that would otherwise have flowed down these channels to Kromellenboog Dam. Because drains only remove water, the model cannot show a pumped valley drawing water out of the river itself.

A steady-state result is the state reached if the abstraction continued at that rate without end. For abstraction that runs only during a drought the drawdown is therefore an upper limit, since a pumped borehole first draws on storage. The loss of streamflow is the final amount, which in reality would arrive later and continue after pumping stops (Leake & Barlow, 2013). The model cannot say how long either takes.

**Recharge cases.** The recharge is multiplied by the factors of cases M and D, 0.96 and 0.89 (Table 12), and each level is run without wells. The change in heads and in the outflow of each group of drains is the result for groundwater availability under objective 5. Each level is also run with 0.5 Mm³/a abstracted under the irrigated land (placement P1). The drawdown of that abstraction is read against the run without wells at the same recharge, as in the base case. The additional lowering of the water table caused by the lower recharge is read from the two runs with the abstraction, one at the base recharge and one at the reduced recharge (Map 9). Both factors follow from the projected change in rainfall (Section 5.5).

**What four water levels cannot decide.** Two further comparisons show how far the result depends on values that the calibration does not fix. First, if the recharge, both conductivities and all drain conductances are multiplied by one factor, every head stays the same and every flow is scaled, so the scaled model fits the four levels exactly as well as the calibrated one. Because the abstraction is not scaled, the model with half the recharge and conductivity at 0.5 Mm³/a is read from the run at 1.0 Mm³/a, and the model with double from the run at 0.25 Mm³/a, without further runs. Second, structure D was run once with the conductivities of S, to separate what the depth of the outflow decides from what the conductivities decide.

## 5.10 Limitations of the methods

**The water balance of the dam.** Every result of the water balance moves with the inflow, which cannot be tested, and the cause of the low inflow of 1982 to 1994 is not known (Section 4.1), so it is not known how often such a period recurs.

The demand carries three assumptions. That the scheme records are the users of the canal is an inference (Section 1.1). The same volume is asked for in every year, although demand rises in dry years, so shortfalls in those years are understated. And the shortfall is measured at the head of the canal; at the fields it is larger by the losses along the canal, which are not recorded (Section 3.4).

In hydrological years 1983 to 1986 the pan stood 7% to 13% above its mean, so evaporation in dry years may be understated by up to about 10%, and if the basin has silted up since the survey of 1982, storage is overstated. Both are bounded by the sensitivity cases of Section 5.4. The restriction rule is assumed to stay the same in the climate cases, although managers would adapt it, and the demand factor assumes the same crops on the same area. A monthly step does not show failures shorter than a month.

Five items could not be obtained and are carried into the recommendations on data collection (Section 8.2):
- the legend of the flags in the reservoir record;
- an operating rule of the scheme;
- the published table of pan factors;
- the table of the 1982 basin survey;
- what the release entry before 1987 represents.

**The groundwater model.** The model shows the direction and the relative size of an effect. It has no time, it cannot show how many boreholes would be needed, where, or what they would yield, and it cannot show whether the surface deposits under the irrigated land are an aquifer.

Its inputs carry assumptions that the records cannot test. The recharge is spread evenly, so recharge concentrated along streams is not represented. The surface deposits carry their conductivity through the full 207.5 m of the layer, although their thickness is unknown (Section 2.4). The closed edge and the drains leave out any groundwater that crosses the boundary and any leakage from the river, the canal, the irrigated land or Klein Maricopoort Dam, so the model understates the water available outside a drought. The abstraction is spread over cells of 200 m, and the water level in a real borehole falls further than the mean of its cell. In the western arm, a quarter of A31E, there is no static water level, and the results there rest on the structure of the model alone.

Some planned runs were not made (Table 14). P1 at 2.0 Mm³/a in structure S is read between the runs at 1.0 and 2.34 Mm³/a. Runs that change one conductivity, one drain conductance or the depth of the outflow at a time are covered in part by the scaled pair, by the run of D with the conductivities of S, and by the two structures themselves. No result of this study rests on a run that was not made.

**The flood model.** The result describes the screening of one reach and not a flood line. No series of flood peaks was in hand, so no design flood could be estimated by statistical analysis, and none of the three methods could be tested against a recorded flood at this site. The SDF is not calibrated for dolomitic catchments, in which the flood may be less than half of the SDF (SANRAL, 2013:3-45), and the spread between the methods is a measure of this uncertainty. The terrain dates from February 2000, its cells are wider than the river channel and its vertical error is of the order of metres, so depths in and beside the channel are approximate. The values of Manning's n were not calibrated, as no flood has been recorded in the reach. The largest floods reach the boundary of the model over about 0.5 km on the northern side of the reach, where the flooded area may be understated.

Two simplifications act in opposite directions. The attenuation of the flood in Klein Maricopoort Dam is ignored, as if the dam were full when the flood arrives, which makes the flood larger. The Waterkloofspruit, which joins the river 13.7 km below the wall and so within the modelled reach (Section 2.3), is not added as an inflow, which makes the flood below its junction smaller. The triangular hydrograph is a design shape and not a recorded one, and all results are means over cells of 15 to 30 m. The spillway of Klein Maricopoort Dam was being rehabilitated in January 2011, when the work on it was reported as 60% complete (News24, 2011); its state since then is not known.

**Pathways and water quality.** Particle tracking inherits every limitation of the groundwater model, runs at steady state and follows only the moving water. Its times rest on an assumed porosity and are orders of magnitude, not ages, and the particles start evenly in the cells under the fields, not where water actually drains below them. The water-quality records cover different periods, three of the sites along the reach have only one to three samples, and no series of groundwater quality exists. The guidelines are yardsticks for the use of the water and for its ecosystems, not tests of pollution, and the mixing check uses flows and EC values from different periods.

## 5.11 Design floods and the flood model

The flood risk of one reach of the Klein Marico River was assessed with design floods routed through a two-dimensional hydraulic model. The reach begins at point F2, below the junction of the Doringrivier, and runs 15.7 km downstream; Map 2 shows the area of the model. It was chosen because the irrigated land of A31E lies along it (Section 2.7). The model area contains 8.04 km² of land mapped as cultivated (DFFE, 2024).

**The catchment.** The catchment above F2 covers 1 357.26 km² (measured in GIS). It includes the catchment of Klein Maricopoort Dam above its wall (F1) and that of the Doringrivier (F3) (Table 14a). Its longest watercourse is 94.12 km long. Its slope between 10% and 85% of that length, the "10-85 slope" used by the manual (SANRAL, 2013:3-46), is 5.36 m/km. The length of the main watercourse from F2 to the point nearest the centre of the catchment is 27.38 km. Rocks of the Malmani Subgroup, which is dolomite, underlie 46.4% of it (Walraven, 1981; Michaluk & Keyser, 1991; measured in GIS).

*Table 14a: The catchments of the flood points: area and the share underlain by dolomite of the Malmani Subgroup (Walraven, 1981; Michaluk & Keyser, 1991; measured in GIS).*

| Point | Where | Catchment (km²) | Dolomite share |
|---|---|---|---|
| F1 | Wall of Klein Maricopoort Dam | 1 162.09 | 54.2% |
| F3 | Doringrivier at its junction | 162.65 | 0% |
| F2 | Klein Marico River below the junction (inflow to the model) | 1 357.26 | 46.4% |

**The design flood.** Three methods of the manual were applied, as it requires that the SDF always be used and compared with the other applicable methods (SANRAL, 2013:3-4). The SDF served as the main estimate (SANRAL, 2013:3-43–3-47). The catchment lies in SDF basin 1 (SANRAL, 2013:3-44), with runoff coefficients of 10% for the 1:2-year flood and 40% for the 1:100-year flood (SANRAL, 2013:3B-2). The time of concentration, the time a flood takes to travel from the far end of the catchment to the outlet, is 16.4 h from the length and slope of the main watercourse (SANRAL, 2013:3-46). Over that duration the point rainfall of the 1:100-year storm is 161.8 mm, and the area reduction factor, which lowers a point rainfall to the mean over the catchment, is 84.4%. Peaks were calculated for return periods of 2 to 100 years.

The Midgley and Pitman formula served as a check (SANRAL, 2013:3-61–3-62). It was applied with the mean annual precipitation of 597 mm of rainfall zone A3B, which covers A31E and both catchments above the dam (Section 1.1), and with the constant of the Bushveld region. The RMF served as an upper limit (Kovacs, 1988; SANRAL, 2013:3-65–3-66). It was calculated for Kovács regions K3 and K4, because at the scale of the regional map the catchment lies on the boundary between them (SANRAL, 2013:3-67).

Dolomite matters for the choice among them. The manual warns that in dolomitic catchments the flood runoff may be less than half of the SDF (SANRAL, 2013:3-45). For the RMF it allows a lower regional constant where a catchment is very permeable or dolomitic (SANRAL, 2013:3-66). The SDF is therefore treated as the conservative case, and the Midgley and Pitman formula as the lower alternative.

**The hydrograph.** The SDF gives a peak only. For the flood model, each peak was given the triangular hydrograph that the manual prescribes for the SDF, with a rise lasting one time of concentration and a fall lasting two (SANRAL, 2013:3-45, 3-47). A base flow of 5 m³/s was added, and the hydrograph was entered at 15-minute steps. The 1:100-year SDF flood then carries 111.3 Mm³.

Two simplifications act in opposite directions. The attenuation of the flood in Klein Maricopoort Dam is ignored, as if the dam were full when the flood arrives, which makes the flood larger. The Waterkloofspruit, which joins the river 13.7 km below the wall and so within the modelled reach (Section 2.3), is not added as an inflow, which makes the flood below its junction smaller.

**The flood model.** The design floods were routed through the reach with HEC-RAS 7.0.1 (USACE HEC, s.a.a), in an unsteady two-dimensional model. "Unsteady" means that the flow changes with time as the hydrograph passes. "Two-dimensional" means that the water may spread in any direction over the valley floor and is not confined to fixed cross-sections. Table 14b sets out the model.

*Table 14b: The two-dimensional flood model of the Klein Marico River below F2.*

| Feature | Set-up |
|---|---|
| Terrain | Shuttle Radar Topography Mission elevation model, 30 m cells, February 2000 (Farr *et al*., 2007) |
| Model area | 24.3 km²; 31 155 cells, 30 m wide, refined to 15 m along the river |
| Roughness | Manning's n by land-cover group of the South African National Land Cover 2022 (DFFE, 2024): woodland 0.075, open bush 0.058, grassland 0.036, cultivated 0.040, fallow 0.032, built-up 0.100, bare 0.022, open water 0.035; a 40 m strip along the channel 0.040 |
| Upstream boundary (F2) | Inflow hydrograph; energy slope 0.00346 from the terrain |
| Downstream boundary | Normal depth, slope 0.00423 |
| Equations | Diffusion wave; shallow-water equations (Eulerian–Lagrangian method) as a check |
| Time | Computation step 10 s (5 s with the shallow-water equations); results every 15 minutes; 60 hours simulated |

Manning's n describes how strongly the land surface resists the flow: the higher the value, the slower and deeper the water. The values were chosen within the ranges published for floodplains and channels (Chow, cited by USACE HEC, s.a.b) and for classes of land cover (USACE HEC, s.a.a). Woodland and open bush lie at the low end of these ranges, and bare ground lies 0.001 below the lowest value given for barren land. The diffusion-wave equations are the default of HEC-RAS. Its manual advises testing whether the full shallow-water equations are needed, and treating them as the more accurate result where the two differ significantly (USACE HEC, s.a.a). The 1:100-year SDF flood was therefore run with both.

Four plans were run: the 1:50-year and the 1:100-year SDF floods, the 1:100-year Midgley and Pitman flood, and the 1:100-year SDF flood with the shallow-water equations.

The RMF and the smaller return periods were not routed. The volume of water was conserved to within 0.002% in every plan.

**What is read.** For every cell of the model, the largest depth, water level and velocity and the time of the peak are read. For the reach as a whole, the peak flow entering and leaving it is read, with the reduction and delay of the peak between the two, together with the area flooded, the areas flooded deeper than 1 m and 2 m, and the area of cultivated land that is flooded, from the land cover of 2022 (DFFE, 2024).

Velocities of up to 15 m/s at two places are numerical errors on steep cells and are not reported.

## 5.12 Pathways and water quality

**Particle tracking.** The pathway of path 2 from the irrigated land (Section 4.5) was traced with MODPATH version 7 (Pollock, 2016) in the base case of each groundwater structure, without wells. Particles were tracked forward, nine in each of the 45 model cells under the land mapped as irrigated, 405 in all, each starting at the water table.

MODPATH follows each particle through the flows that MODFLOW-NWT has calculated between the cells. It converts these flows into velocities by dividing by the area of each cell face and the porosity of the material (Pollock, 2016:3). The effective porosity, the share of the rock through which water actually flows, is not known in A31E. It was therefore entered as 1.0, so that every time of travel can be scaled afterwards by multiplying it by the chosen porosity. Times are reported for an effective porosity of 0.10, for the surface deposits in which 41 of the 45 cells lie; a value of 0.01 for the fractured bedrock would make them ten times shorter. A value of 0.10 lies within the ranges published for fine sand, silt and clay, and a value of 0.01 lies within the total porosity given for fractured crystalline rock, the closest published entry for the fractured quartzite, shale and andesite of A31E (Woessner & Poeter, 2020); neither has been measured in A31E. In a cell where a drain removes only part of the water, a weak sink, MODPATH needs a decision whether a particle stops or passes through (Pollock, 2016:19). Both options were run and gave identical results.

For each particle three things are read: whether it ends in a cell where a river or stream drain discharges or where only the ground drain discharges, the length of its path, and its time of travel.

The times are those of the moving water alone. They include no dispersion, retention or decay of a dissolved substance, so they indicate the order of time in which water recharged under the fields reaches its end point, and no more.

**Water quality along the two paths.** The water of the two paths was compared with the analyses of the Department's National Water Management System at the seven sites of A31E (DWS, s.a.f; Table 14c). Path 1, the water from outside A31E, is sampled below Klein Maricopoort Dam and at three sites along the reach, and path 2, the runoff generated inside A31E, in the Wilgeboomspruit. Kromellenboog Dam receives both. For the groundwater of A31E, only the median of seven samples in the Reserve determination is available (DWS, 2021:163).

*Table 14c: The DWS water-quality sites used, in order along the Klein Marico River, with the period of each record and the number of samples with an electrical conductivity (DWS, s.a.f).*

| Site | What it samples | Path | Period | Samples |
|---|---|---|---|---|
| A3H030 | River at the weir below Klein Maricopoort Dam | 1 | 1989–1993 | 56 |
| A3H042Q01 | River below Klein Maricopoort Dam | 1 | 2012–2023 | 81 |
| 188257 | River at Kalkdam, Enzelsberg road | 1 | 2005–2007 | 3 |
| 188038 | River at Nooitgedacht | 1 | 2004–2005 | 3 |
| 188030 | River at Dammenbrug | 1 | 2004 | 1 |
| A3R003Q01 | Kromellenboog Dam near the wall | 1 and 2 | 1966–2023 | 248 |
| A3H016Q01 | Wilgeboomspruit | 2 | 1971–1991 | 54 |

Seven quantities were compared along the river, and six of them against a guideline value (sulphate has none in the screening):
- electrical conductivity (EC), a measure of the salts dissolved in water;
- sulphate, chloride and sodium;
- the sodium adsorption ratio (SAR), the proportion of sodium to calcium and magnesium, which governs how irrigation water affects the structure of a soil;
- inorganic nitrogen, the sum of nitrate, nitrite and ammonium as nitrogen; where ammonium was not analysed, nitrate and nitrite alone;
- phosphate as phosphorus.

For each site the median and the share of samples above a guideline value were calculated. A value that the laboratory reported below its detection limit is taken at that limit. All detection limits lie below the guideline values, so such a value never counts as an exceedance. Only surface samples are used at Kromellenboog Dam. Each share above a guideline is a share of the samples in which that quantity was analysed.

The guideline values are those of the South African Water Quality Guidelines. For irrigation they are the upper limits of the target water quality range (DWAF, 1996a): an EC of 40 mS/m (p. 155), an SAR of 2.0 (p. 134), and 100 mg/L of chloride (p. 48) and 70 mg/L of sodium (p. 144), the last two being the limits for crops whose foliage is wetted by sprinkler irrigation; for water applied to the soil the chloride limit is 140 mg/L (p. 48). For aquatic ecosystems they are the boundaries of the trophic classes, which describe how nutrient-rich a water is and which the guideline defines for the average summer concentration (DWAF, 1996b:84): 0.5 and 2.5 mg/L of inorganic nitrogen (DWAF, 1996b:84) and 0.025 mg/L of inorganic phosphorus (DWAF, 1996b:97). The guideline sets no fixed target range for either and leaves it to be set for each site (DWAF, 1996b:84).

The share of single samples above a class boundary is therefore a screening indication, not a trophic classification. A value above a guideline shows that the water could affect its use or its ecosystem. It does not by itself show contamination.

The records of the sites cover different periods, so two comparisons are made on common ground. First, the river below the upper dam and Kromellenboog Dam are compared over the common period 2012 to 2023, when both were sampled. Second, a mixing check is made. Kromellenboog Dam receives about 19% of its inflow from the upper dam (Table 15). If its water is a mixture of that inflow and the water of the reach, the EC of the reach's water follows from the EC of the dam and of the river below the upper dam, and that value is set against the EC of the Wilgeboomspruit and of the groundwater. The flows are from 1987 to 2009 and the EC values from 2012 to 2023, and evaporation from the dam raises its EC, so the check shows consistency and not a measured mixture.

No trend testing or full solute balance is done.

# 6. Results

The results follow the supporting research questions of Section 1.2. Sections 6.1 and 6.2 are read from the records. Sections 6.3 and 6.4 are results of the water balance of the dam, and Sections 6.5 to 6.8 add the groundwater model and the climate cases. Sections 6.9 and 6.10 give the screening of flood risk and of the pathways of contaminants.

## 6.1 The records: inflow, storage and canal deliveries

**Inflow.** Over the 68 hydrological years from 1936 to 2009 without the doubtful years, the calculated inflow to Klein Maricopoort Dam has a mean of 5.96 Mm³/a and a median of 3.22 Mm³/a. It ranges from 0.02 Mm³ in 1991 to 43.5 Mm³ in 1943. The mean is nearly twice the median because a few very wet years carry it, and in such years most of the water spills (Section 4.4). The median therefore says more about what the dam can store and deliver. The dry years lie together: the inflow stayed below the median for thirteen years in succession, from 1982 to 1994. The lowest mean of ten years in a row, 1985 to 1994, is 0.84 Mm³/a: for ten years the river brought about a third of the registered volume, before any evaporation.

**Storage.** Figure D shows what this did to the dam. The raised dam stood full from 1975 to 1982, fell to a fifth of its capacity within fifteen months (Section 4.4) and stayed there for twelve years without emptying completely: the lowest storage of those years was 2.3% of capacity, in hydrological year 1992. After 1996 it went through three cycles of filling and drawdown. Of the 516 months with a reading between October 1966 and September 2010, the dam stood at 85% or more in 29%, and in 31% it stood below 21% of capacity, the zones in which the canal received less than a third of the registered volume (Section 5.3).

**[Figure D here]**
*Figure D: Upper panel: monthly storage in Klein Maricopoort Dam as a percentage of the capacity at the time, June 1936 to November 2010 (DWA, 2012). Lower panel: yearly volume in the canal, hydrological years 1936–2024 (DWS station A3H031), with the registered scheme volume of 2.34 Mm³/a. Years that are not counted (a missing or gap-coded month, or a doubtful year) are drawn in grey.*

**Canal deliveries.** The lower panel of Figure D answers how often, for how long and by how much deliveries fell below the registered volume. Of the 44 hydrological years of the raised dam, 1966 to 2009, 38 can be counted; three are incomplete (1975, 1976 and 2008) and three hold gap-coded months (1983, 1994 and 2002). In 24 of the 38, or 63%, the canal carried less than the registered volume. The mean canal volume of the 38 years is 1.70 Mm³/a. In the shortfall years the mean shortfall is 1.35 Mm³, which is 58% of the registered volume, and in 1985 the canal carried nothing at all. The longest unbroken run of shortfall years is ten, from 1984 to 1993, with between 0.00 and 0.59 Mm³ in the canal each year. This is a minimum. The year 1994, which cannot be counted, recorded 0.28 Mm³ in its eleven valid months, and 1995 and 1996 were shortfall years again, with 0.41 and 0.73 Mm³. When the canal record is followed to 2024, 27 of 42 countable years show a shortfall (64%). Hydrological year 2010, with 10.57 Mm³, is left out as unexplained.

At a monthly step, over the 501 months with a valid canal volume between October 1966 and September 2010, the canal delivered 51% of the registered volume, and the longest run of shortfall months is 165. The yearly counts are the firmer ones, because the monthly comparison applies the pattern of Figure C to all years (Section 5.2).

Two things qualify these counts, and they are the reason for the two bounds of Section 5.4. In a drought a canal volume shows what was available, not what was wanted. And in five of the 24 shortfall years (1974, 1977, 1979, 2000 and 2001) the dam did not fall below 75% of its capacity at any time, yet the canal carried 0.06 to 0.55 Mm³ less than the registered volume: less water was taken, not less available. The record alone therefore overstates how often the supply failed, an effect that the water balance of Section 6.4 removes by asking for the registered volume in every year.

## 6.2 Water generated inside A31E and the reach between the dams

Water generated within A31E reaches Kromellenboog Dam below the canal (Section 4.3), and its size follows from the balances of the two dams (Table 15). Over hydrological years 1987 to 2009, 5.01 of the 6.21 Mm³/a that Kromellenboog Dam received, or 81%, did not come from the upper dam and is the net contribution of the reach between the dams. This remainder is the runoff of A31E and any return flow from the irrigated land, less what is taken from the river and lost along it; the records cannot separate these. Return flow cannot exceed the 1.23 Mm³/a recorded at the head of the canal, part-months included (1.20 Mm³/a in Table 8), so at least 3.8 Mm³/a of the remainder is runoff of A31E, net of river abstraction.

*Table 15: Water balance of the reach of A31E between the two dams, in Mm³/a (DWA, 2012; DWS, s.a.c; Bailey & Pitman, 2016a). The inflow to Kromellenboog Dam is the remainder of that dam's own balance.*

| Term | 1987–2009 | 1987–1995 | 1996–2009 |
|---|---|---|---|
| Inflow to Kromellenboog Dam | 6.21 | 3.87 | 7.71 |
| From Klein Maricopoort Dam (spill and release) | 1.19 | 0.07 | 1.92 |
| Remainder: net contribution of the reach | 5.01 | 3.80 | 5.80 |
| Remainder as a share of the inflow | 81% | 98% | 75% |
| For comparison: naturalised runoff of A31E (modelled) | 6.87 | 7.42 | 6.51 |
| Rainfall of zone A3B (mm/a) | 604 | 598 | 608 |

The remainder behaves like runoff. It is positive in each of the 21 years for which it can be calculated; the storage of the lower dam is not recorded on 1 October 1993, so 1992 and 1993 have no value. It ranges from 0.07 Mm³ in 1991, the driest year of the period with 314 mm of rain, to about 19 Mm³ in 1999. Its yearly values have a rank correlation of 0.76 with the zone rainfall, where 1 would mean that the two series rank the years in exactly the same order. With the WR2012 patched flow in place of the dam balance the correlation is 0.85 over 22 years. Single years are uncertain: for 1999 the two estimates of the inflow differ by 8 Mm³.

The response to drought is the main result of this section. In the drought years 1987 to 1995 the reach delivered two-thirds of what it delivered in the years that followed, under almost the same rainfall, while the inflow to Klein Maricopoort Dam from the catchments upstream fell to a quarter (Tables 8 and 15). The water generated inside A31E thus fell far less in the drought than the water from outside it, and it supplied 98% of the inflow to the lower dam. The modelled naturalised runoff does not show this reduction: it is higher in the drought years than afterwards, and in the drought it is about twice the remainder.

**[Figure F here]**
*Figure F: Monthly rainfall in WR2012 rainfall zone A3B (upper panel) and monthly flow of the Wilgeboomspruit at DWS station A3H016 (lower panel), December 1965 to August 1992. Breaks in the line are gaps in the record.*

The one gauged stream inside A31E shows how sharp the response could be in a single small catchment (Figure F). From December 1965 to January 1984 the Wilgeboomspruit has 162 valid months, with a mean flow of 0.18 Mm³ per month and a single zero, and in the 67 valid months from May to September it never stopped. From February 1984 to March 1988 it was dry in 42 of 50 months, and in 19 of the 20 months from May to September. From April 1988 to the end of the record in August 1992 it flowed again, with a zero in 7 of 49 valid months, but at a third of its former mean. The four complete hydrological years 1984 to 1987 average 0.25 Mm³/a, against 2.07 Mm³/a in the six complete years between 1966 and 1980.

The upper panel of Figure F shows that the rain did not stop when the stream did: monthly totals above 100 mm occur in each rainy season from 1984 to 1988. A stream that had flowed through every dry season for eighteen years therefore lost its dry-season flow for four years, and regained it eight years before the upper dam recovered. That this flow comes from groundwater is an inference (Section 1.1). The gauge measures 39 km², and it does not stand for the reach as a whole. In hydrological year 1985 the stream was dry in all twelve months, yet 8.2 Mm³ reached Kromellenboog Dam, of which the fixed release entry of the upper dam explains 0.6 Mm³. No record in hand explains the rest.

## 6.3 Test of the water balance

With the canal as recorded and all other terms from the rules of Table 10, the water balance reproduces the monthly storage of 1987 to 2009 closely: the NSE is 0.996 and the PBIAS −0.3%. The area curve, the pan factors and the release table therefore return the storage record when the canal is known. Table 16 gives the test itself, in which the canal is driven by the registered volume and the rule of the fit period.

*Table 16: Test of the water balance, hydrological years 1987–2009, against the values regarded as satisfactory (NSE above 0.50, RSR of 0.70 or less, PBIAS within ±25%; Moriasi et al., 2007:891). A positive PBIAS means that the simulated total is the lower one.*

| Compared with the record | Values | NSE | RSR | PBIAS | Meets all three |
|---|---|---|---|---|---|
| Monthly storage | 276 months | 0.86 | 0.37 | +7.4% | Yes |
| Yearly canal volume | 20 complete years | 0.60 | 0.64 | −22.4% | Yes |
| Monthly canal volume | 265 months | 0.38 | 0.79 | −17.2% | No |

**[Figure J here]**
*Figure J: Simulated and recorded monthly storage of Klein Maricopoort Dam, hydrological years 1987–2009 (test of the restriction rule; recorded storage from DWA, 2012).*

Monthly storage meets all three values. Figure J shows that the simulated storage follows the record through the low years to 1995 and through both refillings. It departs from the record in three places, each traceable to the canal. From 1996 to 1999 it lies below the record, because the rule resumes deliveries as soon as the storage allows, whereas the recorded canal stayed low. From 2003 to 2005 it lies above the record, because the canal then carried more than the registered volume (3.01 Mm³ in 2003), which the balance never delivers. After 2008 it again lies well below the record.

**[Figure K here]**
*Figure K: Simulated and recorded yearly canal volume, hydrological years 1987–2009, with the registered volume of 2.34 Mm³/a. Recorded volumes are shown for complete years only (DWS station A3H031).*

The yearly canal volume also meets the three values, but narrowly on bias: over the 20 complete years the balance delivers 1.48 Mm³/a against a recorded 1.21 Mm³/a, which is 22% more. Figure K shows where the difference lies. In the drought years 1987 to 1993 the two agree closely, and the difference arises in the recovery. In 1995 and 1996 the balance delivers 1.70 and 2.10 Mm³, while the canal carried 0.41 and 0.73 Mm³ although the dam had refilled to a mean of 48% and 72% of capacity, and it arises again in 2005 to 2007. After the long drought the canal therefore took up water more slowly than the dam could supply it. The balance cannot represent this, and it corresponds to the lower shares of the test period in Figure I.

The monthly canal volume does not meet the values, as expected (Section 5.3). The count of shortfalls is nevertheless close. Of the 265 months with a valid canal volume, 216 show a shortfall in the record and 192 in the balance, and 179 of these are the same months. Of the 20 complete years, 17 show a shortfall in both, though not the same 17. The test thus supports the use of the balance for counts of years and for volumes, and less so for durations counted in single months. It does not test the inflow (Section 5.3).

## 6.4 Reliability of the canal supply

**The Reference run.** Table 17 gives the answer to supporting question 3 for the registered volume, as a pair of bounds. Over the 74 years the canal receives the full registered volume of the month in 59% to 87% of all months, and 80% to 88% of the registered volume is delivered. A hydrological year passes without a shortfall in 45% to 77% of the years. The mean shortfall against the registered volume is 0.48 Mm³/a with the restriction rule and 0.27 Mm³/a without restriction.

*Table 17: Reliability, resilience and vulnerability of the canal supply against the registered volume of 2.34 Mm³/a, Reference run, hydrological years 1936–2009. In brackets: without the doubtful years 1975–1980, in which no failure occurs in either run.*

| Criterion | With the restriction rule (lower bound) | Without restriction (upper bound) |
|---|---|---|
| Reliability by time | 0.590 (0.554) | 0.867 (0.855) |
| Reliability by volume | 0.795 (0.777) | 0.883 (0.873) |
| Yearly reliability | 0.446 (0.397) | 0.770 (0.750) |
| Failure months, of 888 | 364 | 118 |
| Failure years, of 74 | 41 | 17 |
| Longest run of failure years | 17 | 12 |
| Shortfall events | 16 | 11 |
| Mean length of an event (months) | 22.8 | 10.7 |
| Resilience | 0.044 | 0.093 |
| Vulnerability | 0.50 | 0.88 |
| Months with less than half the registered volume | 156 | 111 |

The two runs trade frequency against depth. With the rule the canal fails three times as often, but a failure month still brings half of the registered volume on average (vulnerability 0.50). Without restriction failures are fewer and shorter, but when they come the canal receives almost nothing (vulnerability 0.88), and in 45 months it receives nothing at all. The number of months with less than half the registered volume is therefore not far apart, 156 against 111. The resilience is low in both: once the supply has failed, it stays in failure for 23 months on average with the rule and 11 months without restriction.

**[Figure L here]**
*Figure L: Reference run of the water balance of Klein Maricopoort Dam, hydrological years 1936–2009, with the restriction rule and without restriction. Upper panel: simulated monthly storage. Lower panel: yearly canal delivery against the registered volume of 2.34 Mm³/a. Shaded: the years 1975–1980, in which the inflow is doubtful.*

Figure L shows when the supply falls short. The storage of the two runs is the same while the dam is full and parts in every drawdown. Without restriction the dam is drawn down to its lowest usable storage in each period of shortfall, whereas with the rule it keeps between about 0.5 and 1.5 Mm³ through the long drought, water that is held back from the canal and much of which is lost to evaporation. The lower panel shows three periods of shortfall under both bounds: around 1951, around 1964 and from 1984 to 1995. With the rule there is a fourth, from 2004 to the end of the record, which without restriction shrinks to the single year 2007.

*Table 18: The five longest shortfall events of the Reference run under each bound.*

| Bound | First month | Last month | Months | Total shortfall (Mm³) | Mean shortfall, share of the registered volume |
|---|---|---|---|---|---|
| Rule | Dec 1983 | Jan 1996 | 146 | 21.86 | 0.77 |
| Rule | Mar 2005 | Sep 2010 | 67 | 3.65 | 0.28 |
| Rule | Mar 1950 | Feb 1954 | 48 | 3.37 | 0.36 |
| Rule | Jul 1963 | Feb 1966 | 32 | 3.20 | 0.51 |
| Rule | Feb 1999 | Feb 2000 | 13 | 0.69 | 0.27 |
| None | Jul 1993 | Feb 1995 | 20 | 3.42 | 0.86 |
| None | May 1991 | Oct 1992 | 18 | 3.37 | 0.97 |
| None | May 1988 | Oct 1989 | 18 | 3.10 | 0.89 |
| None | Dec 1989 | Jan 1991 | 14 | 2.39 | 0.88 |
| None | Feb 1987 | Dec 1987 | 11 | 1.96 | 0.92 |

One drought dominates every count (Table 18). With the rule it is a single event of 146 months, whose total shortfall is more than nine times the registered yearly volume and which holds 40% of all failure months. Without restriction the same drought breaks into separate events of 11 to 20 months, because the inflow of each rainy season is passed to the canal at once and the canal is then dry until the next; the five longest events of that run together hold 69% of its failure months. The event that begins in March 2005 runs to the last month of the record, so its length is a minimum.

Two checks leave these results in place. No failure month falls in the doubtful years in any run, so leaving them out changes only the three reliabilities (Table 17, in brackets). The second inflow series, adjusted for the fixed release entry, lowers the reliabilities of the Reference run by at most 0.006 and raises the total shortfall of the longest event under the rule from 21.9 to 22.6 Mm³.

**Sensitivity to the demand.** Figure M shows how the reliability depends on the volume asked of the canal.

**[Figure M here]**
*Figure M: Reliability of the canal supply by time and by volume against the demand on the canal, 0.5 to 3.0 Mm³/a, with the restriction rule and without restriction, hydrological years 1936–2009. Vertical lines: the registered volume (2.34 Mm³/a) and the demand of the WR2012 study (2.73 Mm³/a).*

Without restriction the reliability by time falls steadily as the demand rises, from 0.99 at 0.5 Mm³/a through 0.92 at 1.5 Mm³/a to 0.80 at 3.0 Mm³/a. Between 2.25 and 2.5 Mm³/a the longest event lengthens from 18 to 34 months, because two events of the drought merge. At the upper case of 2.73 Mm³/a the reliability is 0.83 by time and 0.86 by volume without restriction, and 0.55 and 0.77 with the rule.

With the rule the curve lies lower and behaves differently. Even at 0.5 Mm³/a the reliability by time is only 0.82, and the longest event still lasts 128 months. The rule restricts by storage zone whatever the demand, and from 1983 to 1996 the dam stayed in the low zones even at a small demand, because the inflow stayed low. Figure M therefore shows that the answer depends more on the restriction rule than on the demand. The distance between the two bounds at the registered volume, 0.28 in reliability by time, is about as large as the effect of raising the demand from 0.5 to 3.0 Mm³/a with the rule (0.29), and larger than that effect without restriction (0.19).

**Sensitivity to the other inputs.** The same holds for the other inputs (Section 5.4). The rule of the test period alone lowers the reliability by time from 0.59 to 0.39 and lengthens the longest event to 169 months. Evaporation 10% higher or lower, and the release to the river halved or raised by half, each move the reliability by time by about 0.02 under the rule, and every other input by less than 0.01. Without restriction the reliabilities are equally steady, but with 10% more evaporation, or with a lowest usable storage of 0.5 Mm³, two events merge and the longest becomes 34 months instead of 20.

These results carry the limits set out in Section 5.10. In particular, a yearly reliability of 0.45 to 0.77 is a frequency counted in one record, which one drought of unknown cause dominates (Table 18). It is not an assurance of supply.

## 6.5 Groundwater: calibration, comparison with the archive levels and water budget

**Calibration.** For structure S the calibration ended at conductivities of 0.430 m/d for the surface deposits and 0.0029 m/d for the bedrock (Section 5.8). For structure D the two PEST runs lowered phi from 25.6 and from 19.7 to the same value, 11.2, and both ended with both conductivities at the lower limits of their ranges: 0.03 m/d for the surface deposits and 0.0005 m/d for the bedrock. The four water levels therefore do not determine the conductivities of D; the limits do. Each value is an upper limit, since any lower value would fit the four levels at least as well.

**[Figure O here]**
*Figure O: Simulated against observed head at the four boreholes in A31E with a static water level (National Groundwater Archive), for structure S (outflow 1 m below the surface) and structure D (outflow 15.27 m below the surface), with the residual (observed minus simulated) of each.*

Figure O shows the fit at the four boreholes. Structure S matches three of them within 6 m and misses the fourth, 2526AD00180, by 28.9 m: there the measured water table lies 30 m below the valley floor and the model's about 1 m below it. Structure D halves this misfit, to 14.7 m. Over all four boreholes the root mean square falls from 14.9 m in S to 8.5 m in D (Table 19).

This better fit does not show that D has better parameters. In D no water level can rise above the ground drain, 15.27 m below the surface, so the best residual a borehole can reach is 15.27 m less its depth to water. D reaches that value, within 0.9 m, at three of the four boreholes; only 2526CA00864 is free of the drain. The fit of D thus comes from the depth of the outflow and not from the conductivities, and it is no better than that of the benchmark, a water table 15.27 m below the ground everywhere (8.5 against 8.6 m). Without borehole 2526AD00180, structure S fits best, at 3.9 m.

*Table 19: Fit of the two structures and of the benchmark (a water table 15.27 m below the ground everywhere) to the four static water levels used in the calibration and to the 262 archive levels of unrecorded status that were not used. Residual = observed minus simulated head; RMS = root mean square of the residuals.*

| | Four static levels: mean (m) | RMS (m) | RMS without 2526AD00180 (m) | 262 levels: mean (m) | RMS (m) | Within ±10 m | RMS by location group (m) |
|---|---|---|---|---|---|---|---|
| Structure S | −7.7 | 14.9 | 3.9 | −7.0 | 24.3 | 31% | 24.8 |
| Structure D | +0.1 | 8.5 | 5.0 | −5.6 | 16.9 | 62% | 19.5 |
| Benchmark | −2.3 | 8.6 | 5.2 | −6.5 | 14.9 | 71% | 17.9 |
| D with the conductivities of S | – | – | – | +4.3 | 22.7 | 53% | 23.5 |

The calibration also answers whether the regional values are consistent with the measured levels. With the regional recharge, the levels are matched only by a bedrock transmissivity far below the regional 22.81 m²/d (Table 3): 0.60 m²/d in S and 0.10 m²/d in D, over the 207.5 m of the layer. For the surface deposits the two structures lie on either side of it, at 89 and 6.2 m²/d. The regional recharge and transmissivity are therefore not consistent with each other at these four boreholes, unless most of the recharge leaves the ground close to where it entered.

**Comparison with the archive levels.** The 262 levels that were not used in the calibration separate the two structures more clearly than the four that were (Table 19, Figure P).

**[Figure P here]**
*Figure P: Residual (observed minus simulated head) at the single water levels recorded inside A31E (National Groundwater Archive, 1910–1994) against ground level, for structure S (upper panel) and structure D (lower panel). Grey: levels whose status is not recorded, not used in the calibration; open circles: the mean of each location group; blue: the four static levels.*

In structure S only 31% of the 262 levels lie within 10 m of the model (Table 19). Figure P shows where the misfit lies: on the low ground. Where the land surface lies below 1 100 m the measured water table is on average 23.1 m deeper than the model's, and between 1 100 and 1 200 m it is 9.7 m deeper, whereas above 1 300 m the mean residual is only −1.9 m. The misfit at borehole 2526AD00180 is therefore not an isolated error; it follows the pattern of the valleys. The same appears in a count that does not depend on single elevations: only 9 of the 262 recorded levels are shallower than 5 m, but S places the water table shallower than 5 m at 114 of the 262 boreholes, and D at 14.

Structure D removes most of this pattern. Its root mean square is 16.9 m, and 62% of the levels lie within 10 m. On the lowest ground its mean residual is −11.0 m in place of −23.1 m. On the higher ground it is not clearly better: between 1 200 and 1 300 m its mean residual is −8.9 m against −4.4 m in S. Three further results limit what can be claimed for D:
- **It fits no better than the benchmark**, which has a root mean square of 14.9 m. With the conductivities of S it fits worse, at 22.7 m. The levels thus inform the depth of the outflow more than they inform the conductivities.
- **The levels themselves scatter by about 11 m inside the location groups** (Section 5.8). The benchmark and D are both close to that floor, so the remaining misfit cannot be reduced much by any model of this cell size.
- **In the western arm both structures place the water table about 15 m too high on average.** The mean residuals of its 23 levels are −15.4 m in S and −14.3 m in D.

On the surface deposits, the setting of the irrigated land, 26 levels in 11 groups give a root mean square of 17.1 m for S and 13.8 m for D.

The archive levels thus support D over S in the valleys and decide nothing on the high ground. The comparison is not a validation (Section 5.8). If some of these levels were measured during or soon after pumping, they are too deep, and the comparison favours D unfairly.

**[Map 8 here]**
*Map 8: Simulated depth to water in the groundwater model of A31E for (a) structure S (outflow 1 m below the surface) and (b) structure D (outflow 15.27 m below the surface), with the rivers and streams, the two dams, the land mapped as irrigated below Klein Maricopoort Dam and the four boreholes with a static water level, each with its residual (observed minus simulated head).*

Map 8 shows the difference between the structures in space. In S the median depth to water is 9.1 m, and in 17% of the cells the water table lies within 1 m of the surface. In D the median depth is 15.3 m and no cell has water within 1 m. Under the land mapped as irrigated the water table lies 4.5 m deep in S and 15.3 m deep in D. The abstraction cases of Section 6.6 start from these two levels.

**Water budget.** The two structures take in the same recharge and dispose of it in opposite ways (Table 20).

*Table 20: Water budget of the two base cases of the groundwater model, without wells. The budget closes to 0.00% in both.*

| Term | S (Mm³/a) | S (share) | D (Mm³/a) | D (share) |
|---|---|---|---|---|
| In: recharge | 17.53 | 100% | 17.53 | 100% |
| Out: ground drain | 7.67 | 43.8% | 16.90 | 96.4% |
| Out: river drains | 4.02 | 22.9% | 0.13 | 0.7% |
| Out: stream drains | 5.85 | 33.3% | 0.51 | 2.9% |
| Rivers and streams together | 9.86 | 56.2% | 0.63 | 3.6% |

In S more than half of the recharge reaches the rivers and streams. Of the 4.02 Mm³/a that reaches the four rivers, 2.49 Mm³/a discharges to the Klein Marico River itself, 0.78 Mm³/a to the Doringrivier, 0.41 Mm³/a to the Waterkloofspruit and 0.33 Mm³/a to the Wilgeboomspruit. In D almost all the recharge leaves through the ground drain, at depth, and the four rivers together receive 0.13 Mm³/a.

Neither result agrees with the surface flows. These are quantities of different kinds and are compared for scale only. The groundwater discharge to rivers and streams in S, 9.86 Mm³/a, exceeds every available estimate:
- the baseflow of 2.00 Mm³/a in the Reserve determination (DWS, 2021);
- the baseflows of 2.53 and 3.43 Mm³/a in the WR2012 study (Bailey & Pitman, 2016a);
- the net contribution of the whole reach, 5.01 Mm³/a (Table 15);
- the modelled naturalised runoff of 7.21 Mm³/a, which includes storm runoff.

The 0.63 Mm³/a of D lies below every one of them. The valley water levels thus contradict S and the streamflow contradicts D; the real catchment lies between the two, and the records in hand cannot place it.

The large share of the ground drain in both structures follows from the low conductivity of the bedrock. Section 4.3 left about 14 Mm³/a of the estimated recharge unaccounted for and named three possible fates: uptake by vegetation, outflow underground and an overestimated recharge. With a closed edge and a fixed recharge, the model can use only the first. Its split between ground drain and streams is one possible way of closing the balance. It is not a finding of where the recharge goes.

## 6.6 Abstraction intended to offset the shortfall

The drawdowns given in this and the following sections are values of the model, used to compare cases and structures. They are not predictions of how far a water level would fall. The model rests on four water levels that do not determine its conductivities, it is run at steady state, and a cell of 200 m averages what a single borehole would show. This limit applies to every drawdown below and is not repeated.

**The abstraction curve.** Figure Q gives the response of both structures to abstraction under the land mapped as irrigated.

**[Figure Q here]**
*Figure Q: Steady-state response of the groundwater model to abstraction spread over the 45 model cells under the land mapped as irrigated, for structure S and structure D. Upper panel: mean drawdown in the pumped cells; lower panel: share of the abstraction balanced by less discharge to the rivers and streams. Open circles: rates that structure D cannot deliver (label: rate delivered, Mm³/a). Shaded: the mean shortfall against the registered volume in the Reference run and cases M and D, for both bounds (0.27–0.70 Mm³/a), and the rate during the longest shortfall event of the Reference run (1.80–2.05 Mm³/a).*

The upper panel shows how far the water level falls. In structure S the mean drawdown in the pumped cells grows faster than the rate, from 0.96 m at 0.25 Mm³/a and 2.30 m at 0.5 Mm³/a to 40.8 m at the registered volume of 2.34 Mm³/a, where the water level in 19 of the 45 pumped cells lies more than 47.5 m below the surface, the base of the weathered zone. The area in which the drawdown exceeds 1 m grows from 2.6 km² to 46.5 km².

In structure D the drawdown is far larger at every rate: 4.92 m at 0.25 Mm³/a and 20.6 m at 0.5 Mm³/a, five and nine times the values of S. At 0.5 Mm³/a the water level falls below 47.5 m in 7 of the 45 cells. Above that rate D cannot deliver what is asked: the wells deliver 0.93 Mm³/a at 1.0 Mm³/a, and 1.18 and 1.23 Mm³/a at 2.0 and 2.34 Mm³/a, with a mean drawdown of about 160 m. In D the 45 cells under the irrigated land can therefore yield no more than about 1.2 Mm³/a.

The lower panel shows where the water comes from, and here the two structures give opposite answers at every rate. In S, between 0.25 and 1.0 Mm³/a, 87% to 89% of the pumped water is balanced by less discharge to the river drains and under 1% by less discharge to the stream drains; the rest comes from the ground drain. At 2.34 Mm³/a the rivers and streams still supply 78%. Split by river, at 0.5 Mm³/a about 69% of the pumped water is balanced by less outflow to the Klein Marico River itself and about 20% by less outflow to the lower Waterkloofspruit; at 2.34 Mm³/a these shares are 65% and 9%. In D the rivers and streams supply 0.3% to 1.5% at every rate, and the ground drain the rest.

**What the two answers mean.** In structure S, groundwater pumped under the irrigated land is water that would otherwise have flowed down the Klein Marico River and the lower Waterkloofspruit to Kromellenboog Dam, which serves the scheme downstream (Section 2.1). At steady state about nine-tenths of the abstraction would be a transfer between users and not new water. In structure D the abstraction takes water from the deep outflow, which stands for uptake by vegetation and other losses at depth, and the rivers are not affected. Which of the two applies is not decided by the data (Section 6.5).

**What decides the drawdown and what decides the source.** One run separates the two questions (Table 21). When structure D is given the conductivities of S, an abstraction of 0.5 Mm³/a lowers the water level by 2.22 m, almost the 2.30 m of S, and the whole abstraction still comes from the ground drain. The depth of the outflow thus decides where the pumped water comes from, and the conductivity how far the water level falls. The large drawdowns of D, and its limit of about 1.2 Mm³/a, follow from conductivities that the calibration placed at the lower limit of their range and did not determine.

*Table 21: Mean drawdown in the pumped cells, and share of the abstraction balanced by less discharge to the rivers and streams, for an abstraction of 0.5 Mm³/a in the cases that change one thing. P1: under the land mapped as irrigated; P2: spread over the surface deposits within 1 km of it; P3: on the bedrock within 1 km.*

| Case | S: drawdown (m) | S: from rivers and streams | D: drawdown (m) | D: from rivers and streams |
|---|---|---|---|---|
| P1 (as in Figure Q) | 2.30 | 89.2% | 20.6 | 0.5% |
| P2 | 0.55 | 88.8% | 0.73 | 2.7% |
| P3 | 3.93 | 58.0% | Not run | Not run |
| P1, recharge × 0.89 (case D) | 2.42 | 89.8% | 24.3 | 0.6% |
| P1, conductivities of S in structure D | – | – | 2.22 | 0% |
| P1, recharge and conductivities halved | 7.43 | 87.6% | 117.5 (not delivered in full) | 1.0% |
| P1, recharge and conductivities doubled | 0.96 | 89.1% | 4.92 | 0.3% |

**Spreading the abstraction.** When the same 0.5 Mm³/a is spread over the 474 cells of surface deposits within 1 km of the irrigated land, the mean drawdown falls to a quarter of its value under the fields in S and to a twenty-eighth in D, and the source does not change (Table 21). Even the registered volume, spread in this way, gives a mean drawdown of 8.2 m in S, against 40.8 m under the fields. Placed on the bedrock within the same distance, 0.5 Mm³/a gives a larger drawdown in S and draws 58% from the rivers and streams. In the model, how widely the abstraction is spread therefore governs the drawdown far more than the rate does. It does not govern what the abstraction costs the river.

**What four water levels cannot decide.** The last two rows of Table 21 give the clearest measure of the uncertainty. A model with half the recharge and half the conductivities, and one with double, fit the four static levels exactly as well as the calibrated model (Section 5.9). Yet for the same 0.5 Mm³/a the drawdown under the fields ranges from 0.96 to 7.43 m in S and from 4.9 m to more than the cells can deliver in D, while the source of the water is unaffected.

**Registered borehole use.** The check run with the 0.265 Mm³/a registered from boreholes inside A31E, at the registered positions, does not change the head at borehole 2526AD00180 in either structure. Registered use does not explain the misfit there, and the base cases stand without wells.

## 6.7 Climate change

**The canal supply.** Table 22 sets cases M and D against the Reference run, for both bounds.

*Table 22: The climate cases against the Reference run. Canal supply: with the restriction rule / without restriction, hydrological years 1936–2009. Groundwater: discharge to rivers and streams in the base case of each structure, and its change under the recharge factor of the case (Table 12).*

| Case | Reliability by time | Reliability by volume | Yearly reliability | Mean shortfall (Mm³/a) | Longest event (months) | Groundwater to rivers and streams, S | Groundwater to rivers and streams, D |
|---|---|---|---|---|---|---|---|
| Reference | 0.590 / 0.867 | 0.795 / 0.883 | 0.446 / 0.770 | 0.48 / 0.27 | 146 / 20 | 9.86 Mm³/a | 0.63 Mm³/a |
| M (median) | 0.541 / 0.829 | 0.758 / 0.854 | 0.405 / 0.703 | 0.60 / 0.36 | 148 / 35 | −3.8% | −5% |
| D (dry end) | 0.477 / 0.791 | 0.720 / 0.823 | 0.324 / 0.635 | 0.70 / 0.44 | 163 / 35 | −10.5% | −14% |

At the median of the projections, case M, the reliability by time falls by 5 percentage points with the rule and by 4 without restriction, and the reliability by volume by 3 to 4 points. At their dry end, case D, the reliability by time falls by 11 and 8 points, and the reliability by volume by 6 to 8. Without restriction the scheme would receive its full yearly volume in about seven years out of ten in case M, and in fewer than two out of three in case D, where it was three out of four. The mean shortfall against the registered volume rises by a quarter to a third in case M and by a half to two-thirds in case D.

Three features of Table 22 show what drives these changes. First, the dry end of the rainfall weighs as much as the median change in climate. Cases M and D share the warming and its factor on evaporation and demand and differ only in inflow and recharge, yet with the rule the reliability by time of D lies 6 points below that of M, more than the 5 points by which M lies below the Reference run; without restriction the two steps are equal, 4 points each. Second, the shortfalls lengthen. With the rule the long event grows from 146 to 148 months in case M and to 163 months in case D (October 1983 to April 1997), and its total shortfall from 21.9 to 24.5 and 26.6 Mm³. Without restriction the events of the drought merge, so that the longest lasts 35 months instead of 20, and the number of events rises from 11 to 15 and 19. Third, deep shortfalls become more common: the months in which the canal receives less than half of the registered volume rise from 156 to 187 and 214 with the rule, and from 111 to 138 and 164 without restriction.

**[Figure N here]**
*Figure N: Share of months in which the simulated storage of Klein Maricopoort Dam is at or above each level, for the Reference run and cases M and D, hydrological years 1936–2009. Left panel: with the restriction rule; right panel: without restriction.*

Figure N shows that cases M and D lower the storage of the dam at all times and not only in droughts. The dam holds at least half its capacity in about 65% of the months in the Reference run with the rule, 60% in case M and 55% in case D (without restriction about 60%, 55% and 50%). It stands below 1.5 Mm³ in about 18%, 21% and 24% of the months with the rule, and in about 24%, 31% and 35% without restriction.

These are responses of the recorded sequence of years to factors grounded in the projections. They probably understate the loss in the driest years (Section 5.5).

**Groundwater.** In the groundwater model, a lower recharge reduces the discharge of groundwater to the rivers and streams by about as much as the recharge (Table 22). Under recharge factors of 0.96 and 0.89 the discharge falls by 3.8% and 10.5% in structure S, slightly less than the recharge, and by 5% and 14% in structure D, more than the recharge.

Map 9 shows where the water table falls under case D. It compares two runs, each with 0.5 Mm³/a abstracted under the irrigated land, one at the base recharge and one at 89% of it. The drawdown of the abstraction itself is thereby removed, and what remains is the additional lowering caused by the lower recharge.

In structure S the additional lowering has a mean of 1.00 m over the catchment (median 0.55 m), a 95th percentile of 3.39 m and a largest value of 9.31 m, and it exceeds 1 m over 220 km² and 5 m over 7 km² of the 602 km². The largest falls lie on the high ground between the valleys. In the valleys and under the fields the drains hold the water table, so that under the 45 pumped cells the additional lowering averages only 0.23 m (largest 0.75 m).

In structure D the additional lowering has a mean of 0.38 m (median 0.00 m), a 95th percentile of 2.31 m and a largest value of 7.52 m, and it exceeds 1 m over 85 km² and 5 m over 3.5 km². Over most of the catchment it is small, but it is largest under and around the pumped cells, where it averages 3.78 m. There the drier climate adds to the drawdown of the abstraction, which rises from 20.6 m to 24.3 m (Table 21).

Under case M the additional lowering is about a third of that under case D: a mean of 0.35 m in S and 0.13 m in D over the catchment, and 0.08 m in S and 1.26 m in D under the pumped cells.

**[Map 9 here]**
*Map 9: Additional lowering of the simulated water table when recharge falls to 89% of the base value (case D), for (a) structure S and (b) structure D, with 0.5 Mm³/a abstracted from the 45 model cells under the land mapped as irrigated in both runs.*

Two consequences follow for abstraction. First, in structure S the river water that an abstraction would capture is itself 4% to 11% smaller in the two cases. Second, the same abstraction lowers the water level further. For 0.5 Mm³/a under the irrigated land, the mean drawdown in the pumped cells rises from 2.30 m to 2.34 m and 2.42 m in S, and from 20.6 m to 21.8 m and 24.3 m in D, where the number of pumped cells in which the water level falls below the base of the weathered zone rises from 7 to 8 and 9 of 45. The source of the water does not change (Table 21).

## 6.8 The extent to which groundwater could offset the shortfall

The main research question asks to what extent groundwater within A31E could offset the shortfalls of the canal supply. The results allow an answer in four parts, each with its own standing. They do not allow a share of the shortfall that boreholes could supply. Table 23 brings the parts together.

*Table 23: The shortfall against the registered volume, set against the modelled recharge of A31E (17.336 Mm³/a; DWS, 2021) and against the response of the two model structures to abstraction under the land mapped as irrigated. For a volume that lies between two model runs, the values of both runs are given. The model columns are runs at the base recharge; how a lower recharge changes them is given in Section 6.7.*

| Volume | Mm³/a | Share of the recharge | Structure S: mean drawdown; from rivers and streams | Structure D: mean drawdown; from rivers and streams |
|---|---|---|---|---|
| Mean shortfall, Reference run, both bounds | 0.27–0.48 | 1.6–2.8% | 0.96–2.30 m; 89% | 4.9–20.6 m; under 1% |
| Mean shortfall, cases M and D, both bounds | 0.36–0.70 | 2.1–4.0% | 0.96–7.43 m; 88–89% | 4.9 m to more than the cells can deliver; 1% or less |
| Rate during the longest event, both bounds | 1.80–2.05 | 10–12% | 7.4–40.8 m; 78–88% | Not delivered: 1.18 Mm³/a at most |
| Whole registered volume | 2.34 | 13.5% | 40.8 m; 78% | Not delivered: 1.23 Mm³/a |

**Size.** Measured against the modelled recharge of the whole catchment, the shortfall is small: the mean shortfall of the Reference run is 1.6% to 2.8% of it, and even the whole registered volume is 13.5%. In cases M and D the mean shortfall rises to 0.36–0.70 Mm³/a, or 2.1% to 4.0% of the recharge, while the recharge itself falls by 4% to 11% (Table 12). Measured against what boreholes in A31E have yielded, it is not small. The mean shortfall equals 8.7 to 15.2 L/s pumped without pause, which is 29 to 51 boreholes at the median strike yield of 0.3 L/s. The registered volume equals 74 L/s, or about 247 such boreholes, and the strike yields of all 109 boreholes with a recorded yield add up to 93 L/s. These counts indicate scale only (Section 5.6).

**Source.** The share of an abstraction that would be taken from the rivers and streams leading to Kromellenboog Dam lies between less than 1% and about 89%, depending on the structure. The records do not decide between them. At one end of this range groundwater would be a new source for the scheme. At the other it would largely be the river's own water, taken before it reaches the lower dam.

**Effect on water levels.** For the mean shortfall the model gives a drawdown under the irrigated land of about 1 to 2 m in structure S and 5 to 21 m in structure D. Models that fit the four water levels equally well extend this to 7 m in S and beyond what the cells can deliver in D (Table 21). The rate needed during the longest shortfall event, 1.8 to 2.05 Mm³/a, is a different matter. In D it cannot be delivered from under the irrigated land at all, and in S it lies between runs with drawdowns of 7 and 41 m. Spreading the abstraction over the valley deposits reduces the drawdown many times over in both structures, but not the share taken from the rivers.

**Timing.** The model, which has no time, cannot say when groundwater would be available. The records give one indication. The Wilgeboomspruit flowed again from April 1988, eight years before the upper dam recovered (Section 6.2). For most of the long shortfall, groundwater inside A31E may therefore have stood nearer to its normal state than to its state of 1984 to 1988. This is an inference from one stream.

The bounded answer to the groundwater part of the main research question is therefore as follows. In the groundwater model an abstraction equal to the mean shortfall against the registered volume (0.27 to 0.48 Mm³/a for the two bounds) lowers the water level under the irrigated land by about 1 to 2 m in one structure of the model and by about 5 to 21 m in the other. Between less than 1% and about 89% of it is balanced by less discharge to the rivers and streams that lead to Kromellenboog Dam. A shortfall of the size of the long drought, 1.8 to 2.05 Mm³/a for more than a decade, could not be offset from under the irrigated land in one structure, and in the other only by taking most of the water from the river. These are differences between steady-state cases of a model that is weakly constrained by four water levels. They show the direction and the relative size of the effect, and not what boreholes would yield, how many would be needed or where. On the available evidence, groundwater within A31E could offset the average shortfall of the canal supply in volume, but whether it would be new water, and whether it could carry the scheme through a drought like that of 1984 to 1995, cannot be established without the data set out in Section 8.2.

## 6.9 Flood risk in the modelled reach

The three methods give design floods that differ widely in size (Table 23a). At the 1:100-year return period, the SDF peak of 1 252 m³/s exceeds the Midgley and Pitman peak by 41%, and it also exceeds the RMF for Kovács region K3. The RMF is the envelope of the largest floods recorded in that region. The SDF therefore lies at the upper end of what the methods give for this catchment. This agrees with the warning of the manual that in dolomitic catchments the flood may be less than half of the SDF (SANRAL, 2013:3-45); dolomite underlies 46% of this catchment (Table 14a).

*Table 23a: Design flood peaks at F2, in m³/s, for a catchment of 1 357.26 km².*

| Method | 1:2 | 1:5 | 1:10 | 1:20 | 1:50 | 1:100 |
|---|---|---|---|---|---|---|
| SDF | 92 | 289 | 464 | 662 | 974 | 1 252 |
| Midgley and Pitman | – | – | 374 | 507 | 703 | 889 |
| **RMF (no return period): 1 205 (region K3); 2 355 (region K4)** | | | | | | |

The hydrographs entered into the flood model, sampled at 15-minute steps, peak at 972, 1 250 and 887 m³/s.

The reach hardly reduces these floods (Table 23b). Between F2 and the lower boundary of the model, 15.7 km downstream, the peak falls by 1% to 3% and arrives about two hours later. At its fullest, the floodplain holds 13 to 17 Mm³, which is 14% to 16% of the volume of the flood. A flood of this size therefore passes through the reach almost unchanged, and the water level falls steadily along the river, from 1 117.1 m to 1 064.6 m in the 1:100-year SDF flood. After the flood, 3.5 to 3.6 Mm³ remain ponded in hollows of the floodplain.

*Table 23b: The design floods routed through the modelled reach of the Klein Marico River (model area 24.3 km², with 8.04 km² of land mapped as cultivated; DFFE, 2024).*

| Plan | Peak in (m³/s) | Peak out (m³/s) | Peak reduced | Delay (h) | Flooded (km²) | Deeper than 1 m (km²) | Deeper than 2 m (km²) | Largest depth (m) | Cultivated land flooded (km²) |
|---|---|---|---|---|---|---|---|---|---|
| 1:50, SDF | 972 | 951 | 2.1% | 2.25 | 7.72 | 6.26 | 4.40 | 7.4 | 3.17 |
| 1:100, SDF | 1 250 | 1 236 | 1.1% | 1.75 | 7.97 | 6.66 | 4.93 | 7.6 | 3.24 |
| 1:100, Midgley and Pitman | 887 | 858 | 3.3% | 2.00 | 7.60 | 6.10 | 4.20 | 7.3 | 3.13 |
| 1:100, SDF, shallow-water equations | 1 250 | 1 234 | 1.3% | 2.00 | 8.34 | 7.01 | 5.33 | 8.0 | 3.33 |

The flooded area changes little between the floods, although their peaks differ widely. The 1:100-year Midgley and Pitman flood has a peak 29% lower than the SDF flood, but it covers only 5% less land: 7.60 against 7.97 km². The valley confines the flow, so a larger flood is carried mainly by greater depth, and in most of the flooded area the water stands more than 1 m deep. The mean depth over the flooded area is 2.3 to 2.7 m. In the 1:100-year SDF flood, the largest velocity across a cell face is below 0.7 m/s on half of the wetted faces, below 2.2 m/s on nine-tenths and below 4.2 m/s on 99%.

The choice of equations matters less than the choice of method. With the shallow-water equations, the 1:100-year SDF flood covers 5% more land than with the diffusion-wave equations, and its outflow peak differs by 0.2%. That run reported local convergence warnings on the rising limb, the largest being an error in the water level of 1.12 m in one cell.

In every plan, 3.1 to 3.3 km² of land mapped as cultivated is flooded (Table 23b). This is about 40% of the cultivated land in the model area, and most of it lies under more than 1 m of water: 2.71 to 2.99 km². Fallow and built-up land flooded covers less than 0.02 km².

The flooded cultivated land includes land mapped as irrigated (Map 11):
- Under the 1:100-year SDF flood, about 44 ha of the land mapped as irrigated is flooded, 38 ha of it more than 1 m deep, in 9 of the irrigated patches.
- Across the four plans, the irrigated land flooded is 42 to 46 ha.

These areas were calculated in GIS from the model results, cell by cell.

**[Map 11 here]**
*Map 11: Maximum depth of the 1:100-year flood (SDF method) in the modelled reach of the Klein Marico River, from the HEC-RAS 2D model, with the outline of the 1:50-year flood. Hatching shows land mapped as irrigated; the inset shows the irrigated land in more detail. Depth classes 0.01–0.5, 0.5–1, 1–2, 2–4 and >4 m.*

## 6.10 Pathways and the two waters

**Particle tracking.** The two structures send water recharged under the irrigated land to different places (Table 23c, Map 10).

In **structure S**, 387 of the 405 particles, or 96%, end in a cell where a river drain discharges groundwater: the Klein Marico River and its tributaries. The paths are short, with a median of 537 m and none longer than 3.9 km. At an effective porosity of 0.10, the median time to the river is 140 years and the 90th percentile about 700 years. The shortest paths, from cells beside the river, take a few months.

In **structure D**, no particle reaches a river or stream drain that discharges. Every particle ends where only the ground drain removes water, and 288 of the 405 do not leave the cell in which they started.

The difference follows from the depth of the water table under the fields, which is shallow in S and deep in D: 4.5 m and 15.3 m (Section 6.5, Map 8). Where the water table stands above the river bed, as in S, groundwater from the fields flows to the river. Where it stands deeper, as in D, the water leaves the water table close to where it entered.

*Table 23c: Particle tracking from the 45 model cells under the land mapped as irrigated (405 particles, base case without wells). Times of travel at an effective porosity of 0.10; at 0.01 they are ten times shorter. Times are those of the moving water alone.*

| | Structure S | Structure D |
|---|---|---|
| Particles ending at a discharging river or stream drain | 387 (96%) | 0 |
| Particles ending where only the ground drain discharges | 18 | 405 |
| Particles that do not leave their starting cell | 45 | 288 |
| Length of path: median / 90th percentile / longest | 537 m / 3.0 km / 3.9 km | 0 m / 351 m / 1.2 km |
| Time of travel: median | 140 years, to the river | 7 years, to the ground drain |

**[Map 10 here]**
*Map 10: Flow paths of 405 particles released in the 45 model cells under the irrigated land (MODPATH 7; Pollock, 2016), for (a) structure S and (b) structure D. Yellow dots mark the end of each path. In S, 387 of the 405 paths end at a river; in D none do. The paths show advective flow direction only; contaminant transport is not modelled, and travel times depend on an assumed porosity.*

These results take the two structures of Section 6.6 one step further. In S, the groundwater that an abstraction under the fields would capture is the same water that carries whatever drains from the fields to the river, decades to centuries later. In D, an abstraction takes almost nothing from the rivers (Table 21), and the water recharged under the fields does not reach them.

**The two waters.** The records of the Department show that the two paths of the conceptual model carry different water (Table 23d, Figure R). The water of path 1, which comes from outside A31E, had a median electrical conductivity of 51.2 mS/m below Klein Maricopoort Dam in 1989–1993 and 62.3 mS/m in 2012–2023. At the three sites along the reach the median was 76 to 83 mS/m in 2004–2007, although these values rest on one to three samples each. The water of path 2, generated inside A31E, is far fresher: the Wilgeboomspruit had a median of 3.85 mS/m in 1971–1991, and the groundwater of A31E 17.7 mS/m (DWS, 2021:163). Kromellenboog Dam, which receives both, lies between them at 21.7 mS/m.

The sulphate shows the same order. Its median is 30 to 57 mg/L below the upper dam and 102 to 145 mg/L along the reach, against 17.7 mg/L in Kromellenboog Dam and 3.05 mg/L in the Wilgeboomspruit.

Over the common period 2012–2023, the river below the upper dam had a median EC of 62.3 mS/m (81 samples) and Kromellenboog Dam 20.7 mS/m (87 samples). With 19% of the inflow to the lower dam coming from the upper dam (Table 15), this implies an EC of about 11 mS/m for the water of the reach (0.19 × 62.3 + 0.81 × 11 = 20.7). That value lies between the Wilgeboomspruit and the groundwater of A31E. The records are therefore consistent with the water of Kromellenboog Dam being a mixture of a saline inflow from upstream and the far fresher water of A31E itself, but they do not show it.

*Table 23d: Screening of the DWS water-quality records along the two paths (DWS, s.a.f; surface samples). Share = percentage of the samples analysed for that quantity that exceed the guideline value. Guidelines: EC above 40 mS/m, the upper limit of the target range for irrigation (DWAF, 1996a:155); inorganic nitrogen above 0.5 and 2.5 mg/L and phosphate as phosphorus above 0.025 mg/L, the boundaries of the trophic classes, which the guideline defines for the average summer concentration (DWAF, 1996b:84, 97). Chloride, sodium and SAR exceed their irrigation guidelines in no sample at any site.*

| Site | Path | Period | Samples | EC median (mS/m) | EC above guideline | Inorganic N above 0.5 / 2.5 mg/L | Phosphate-P above 0.025 mg/L |
|---|---|---|---|---|---|---|---|
| A3H030 | 1 | 1989–1993 | 56 | 51.2 | 86% | 2% / 0% | 4% |
| A3H042Q01 | 1 | 2012–2023 | 81 | 62.3 | 99% | 12% / 4% | 19% |
| 188257 | 1 | 2005–2007 | 3 | 76.3 | 100% | 0% / 0% | 0% |
| 188038 | 1 | 2004–2005 | 3 | 77.7 | 100% | 0% / 0% | 33% |
| 188030 | 1 | 2004 | 1 | 82.6 | 100% | 100% / 0% | 100% |
| A3R003Q01 | 1 and 2 | 1966–2023 | 248 | 21.7 | 17% | 16% / 0% | 29% |
| A3H016Q01 | 2 | 1971–1991 | 54 | 3.85 | 0% | 5% / 2% | 20% |

**[Figure R here]**
*Figure R: Electrical conductivity (upper panel) and sulphate (lower panel) at the DWS water-quality sites along the Klein Marico River below Klein Maricopoort Dam, in Kromellenboog Dam and in the Wilgeboomspruit (DWS, s.a.f), with the period of each record, the upper limit of the target range for irrigation (40 mS/m; DWAF, 1996a:155) and the median EC of the groundwater of A31E (DWS, 2021). Single samples are shown as circles.*

**What the screening shows.** Against the guidelines, the salt content separates the paths. On path 1, 86% to 100% of the samples exceed the EC guideline for irrigation, against 17% in Kromellenboog Dam and none in the Wilgeboomspruit, whereas no sample at any site exceeds the guidelines for chloride, sodium or SAR. The water released from the dam, and so probably the canal water, is therefore saline in its general salt content, measured by EC, and not in sodium in particular.

The nutrients do not separate the paths in the same way. The median of inorganic nitrogen lies below 0.5 mg/L at every site except one, which has a single sample. Below the upper dam, 12% of the samples exceed 0.5 mg/L and 4% exceed 2.5 mg/L, and the 95th percentiles there are 0.88 mg/L for inorganic nitrogen and 0.135 mg/L for phosphate as phosphorus. Phosphate exceeds 0.025 mg/L in 19% of the samples below the upper dam, in 29% in Kromellenboog Dam and in 20% in the Wilgeboomspruit. Episodes of nutrient-rich water thus occur on both paths, including in the runoff of A31E itself.

The share of single samples above a class boundary is a screening indication, not a trophic classification. A value above a guideline shows that the water could affect its use or its ecosystem. It does not by itself show contamination (Section 5.12).

# 7. Discussion

The discussion takes the supporting research questions in turn and then the main question. Its numbers are those of Section 6.

## 7.1 The canal supply in drought

The two bounds of Table 17 are two ways of running short. With the restriction rule the canal falls short in four months out of ten, but such a month still brings half of the registered volume on average. Without restriction it falls short in about one month in eight and then receives almost nothing. Hashimoto et al. (1982:19) found the same trade in their reservoir example, where "high system reliability was accompanied by high system vulnerability". A partial delivery lets an irrigator plant less or apply less (Section 3.1); a dry canal does not. At this dam, however, restriction costs volume: the rule delivers 80% of the registered volume and the unrestricted canal 88%, because much of the water held back evaporates (Section 6.4).

The reliability depends more on this rule than on the demand (Figure M). Without restriction a lower demand helps: at 1.5 Mm³/a, close to the 1.4 Mm³/a that the Department gave as the yield of the dam (DWAF, 2004:50), the canal is supplied in 92% of all months, against 87% at the registered volume. With the rule, even 0.5 Mm³/a leaves a shortfall event of 128 months. The reason lies in the inflow: in its ten driest years in succession the river brought about a third of the registered volume (Section 6.1), so the canal's share was decided by how that water was divided between canal and store, and hardly by how much was asked for. The rule is also the least certain input, since none could be obtained and the two periods of the record give different rules (Figure I).

One drought dominates the counts under both bounds (Table 18), so its cause decides how they may be read. The inflow stayed below its median for thirteen years, although the zone rainfall averaged 99% of its long-term mean from 1986 to 1995 (Sections 1.1 and 6.1). Seven years after the Millennium Drought of south-eastern Australia, runoff as a fraction of rainfall had likewise not recovered in 37% of the watersheds studied (Peterson et al., 2021). The explanations found plausible there rest on the length of the drought and on groundwater, namely declining groundwater storage and a weaker connection between groundwater and streams, with the harvesting of runoff by small private dams as a further cause (Fowler et al., 2022). These match the two explanations of Section 4.1: a dolomite aquifer whose springs stayed low for almost a decade (Pyburn, 2015:44), and a greater use of water above the dam. The records cannot separate them, as is common where gauged flows are affected by poorly defined developments upstream (Kapangaziwiri et al., 2011:128). Since the rainfall of each year does not explain the drought, its recurrence cannot be estimated from the rainfall record, and the reliabilities of Table 17 remain frequencies counted in one record (Section 5.4). Unlike those watersheds, the inflow here did recover, with the rains of 1995 and 1996 (Section 4.4).

The test of Section 6.3 supports counts of years and volumes more than durations counted in months, and it leaves the inflow untested (Section 5.3). Its one systematic error is instructive: over the test period the balance delivers 22% more than the canal carried, because in the years of recovery it resumes delivery as soon as the storage allows (Figure K). A shortfall in this study thus measures what the dam could not supply; the water taken after a drought may stay low for longer.

## 7.2 Water generated inside A31E

The records answer supporting question 2 directly. Water generated inside A31E reaches Kromellenboog Dam below the canal, and it responded to the drought far less than the water from outside: the reach between the dams delivered two-thirds of its later volume in the drought years, while the inflow from upstream fell to a quarter (Table 15). The modelled naturalised runoff shows no reduction and is about twice the remainder in those years. Part of that gap is water taken from the river or lost along it, which a naturalised flow excludes by definition. The rest agrees with the finding that runoff in a long drought falls below what an earlier rainfall–runoff relationship predicts (Saft et al., 2015), and it supports the use of recorded flows in this study.

For the users downstream the result matters directly. Kromellenboog Dam is operated for an irrigation scheme in catchment A31F (DWAF, 2004:57), and in the drought the reach supplied 98% of its inflow. The runoff of A31E thus carried the scheme below it through the years in which the scheme inside it had almost no water. Any use of water inside A31E that reduces the flow of the reach, whether taken from the river or from groundwater that would have reached it, therefore comes out of the supply of the lower dam.

The Wilgeboomspruit shows the response of one small catchment (Figure F). A stream that had flowed in every dry-season month on record stopped in the third year of below-average rainfall, was dry in most months for four years although the rain continued, and returned in April 1988 at a third of its former flow. The store that feeds it is therefore small and quick to respond. Whether it is groundwater is not shown: low flows in South African rivers derive from near-surface storage in soils and in unsaturated rock above the water table as well as from groundwater, with much uncertainty about which dominates in a given basin (Kapangaziwiri et al., 2011:127). The two readings lead to different conclusions. If the store is the aquifer that boreholes would tap, groundwater is weakest in the first years of a drought and partly restored long before the dam recovers. If it lies above the water table, the stream says little about that aquifer.

## 7.3 Groundwater as a backup

Against the modelled recharge the mean shortfall is small (Table 23), but only if recharge is water free to take. Seward et al. (2006) argue that sustainable groundwater use in South Africa should rest instead on capture, the decrease in discharge and increase in recharge that pumping brings about, and capture supplied about 0.85 of long-term withdrawals in the aquifer systems reviewed by Konikow and Leake (2014). Structure S behaves in this way: about nine-tenths of the abstraction is balanced by less discharge to the rivers. Structure D gives the opposite answer, because the source of the pumped water follows from where the water table stands before pumping. In S the water table in the valley stands above the river beds, so the rivers gain groundwater and pumping intercepts it. In D it stands about 15 m below the surface, under the river beds, so there is almost nothing to intercept and the water comes from the deep outflow, which stands for uptake by vegetation among other losses (Section 5.7). The two readings of the Wilgeboomspruit (Section 7.2) correspond to these structures: a stream fed by the aquifer to S, and one fed from above the water table to D.

The drawdown is decided by something else. Given the conductivities of S, structure D lowers the water level by about the same 2 m as S for an abstraction of 0.5 Mm³/a (Table 21). Its large drawdowns, and its limit of about 1.2 Mm³/a under the irrigated land, therefore follow from conductivities that the calibration placed at the lower limits of their ranges, limits that were chosen beforehand and not derived from the water levels. The 1.2 Mm³/a is no estimate of what the valley could yield; it shows that the answer turns on a conductivity that no record in A31E fixes. One result holds in both structures: spreading the abstraction over the valley deposits lowers the drawdown many times and leaves the source unchanged.

The fit at four water levels is therefore not a validation, and published work would not expect one. Calibration yields a non-unique solution, and a groundwater model can be tested but not validated (Konikow & Bredehoeft, 1992). Four calibrated conceptual models of one aquifer system differed little in their heads but greatly in what they predicted beyond the calibration data (Troldborg et al., 2007), as S and D do. Data that both discriminate between conceptual models and bear on the purpose of the model are hard to find (Enemark et al., 2019); here neither structure fits the 262 archive levels better than a water table drawn 15.27 m below the ground (Table 19). Published South African models rest on far more, such as the water-level series used for calibration and validation in the Hout catchment (Ebrahim *et al*., 2019), and even a model of 140 km² with 40 static water levels could not calibrate storage (Watson *et al*., 2026). With four static levels over 600 km² the model of A31E belongs to the lowest class of confidence (Barnett et al., 2012:20–21), and its two structures state openly an uncertainty that a single calibrated model would hide.

Supporting question 4 is thus answered in two steps. The records indicate water levels well below the valley floors, low borehole yields and a shallow store that emptied early in the drought. The model adds that an abstraction equal to the mean shortfall can be delivered in both structures, at a cost to the rivers of anywhere between nothing and nine-tenths, and with a drawdown that depends on an unknown conductivity. In the terms of Calow et al. (2010), groundwater in A31E is limited as a backup not by availability but by access, and by the question of whose water is taken.

## 7.4 Climate change

Supporting question 5 asks how the warmer and probably drier conditions projected for about 2050, represented by the median and the dry end of published projections for the region, would alter the reliability of the canal supply and the availability of groundwater.

At the median of the projections the change is modest. The reliability by time falls by 4 to 5 points and the yearly reliability by 4 to 7 points (Table 22). At their dry end the reliability by time falls by 8 to 11 points and the yearly reliability by 12 to 14 points, and the mean shortfall against the registered volume rises by a half to two-thirds.

The range between the two cases is set by the rainfall and not by the warming. Both cases carry the same warming of 1.9 °C, which raises evaporative demand by a few per cent (Scheff & Frierson, 2014), whereas the change in rainfall between them, from −3.1% to −8.5%, becomes a change in inflow from −7% to −20% through an elasticity of 2.0 to 2.5 (Table 12).

This amplification agrees with the finding that, where about 500 mm of rain falls per year, a change in rainfall is magnified in the river flow (De Wit & Stankiewicz, 2006). It is why the rainfall, which is uncertain even in sign, decides the outcome more than the warming, which is not.

A wetter outcome offers little counterweight. The wettest tenth of the models gives about +0.5% to +3% of annual rain (Section 3.7), and in wet years most of the additional inflow spills from a dam of this size (Section 6.1). The range to be planned for therefore lies between the Reference run and case D, with the median projection, case M, nearer to the Reference run.

The uniform factors also leave out what the projections emphasise. Longer and more frequent droughts are projected for the region (Trisos *et al*., 2022), and the IPCC projects an increase in agricultural and ecological drought in southern Africa (Ranasinghe *et al*., 2021:1771), whereas the cases keep the recorded sequence of years. The clearest rainfall signal is about a tenth less rain in September to November (Section 3.7). A later start of the rains would lengthen the months in which the canal draws on the dam before the first inflow, which a factor applied to every month cannot show (Section 5.5). The cases also keep the rainfall–runoff behaviour of the record, although runoff falls disproportionately in long droughts and may not recover afterwards (Section 7.1).

Cases M and D are therefore more likely to understate the loss of reliability than to overstate it.

For groundwater, the recharge factors follow from the projected rainfall through a relation between recharge and rainfall across Africa, which uses differences between places to stand for a change over time (MacDonald *et al*., 2021). Recharge begins only once rainfall exceeds a threshold (Cuthbert *et al*., 2019), so in the dry years a drier climate could reduce it by more than the factor used. In the model, a lower recharge reduces the discharge of groundwater to the rivers and streams by about as much as the recharge: by 4% and 10% in structure S, and by 5% and 14% in structure D (Table 22). Where the water table falls depends on the structure (Map 9). In structure S the largest additional lowering under case D lies on the high ground between the valleys, where it exceeds 1 m over more than a third of the catchment, while the drains hold the water table in the valleys and under the fields. In structure D the additional lowering is small over most of the catchment but largest under the pumped cells, by about 3.8 m. There the abstraction has drawn the water table below the ground drain, so the drain no longer holds it, and the drier climate adds directly to the drawdown of the abstraction.

The cases thus raise the shortfall by a quarter to two-thirds while the recharge on which an abstraction would draw falls by 4% to 11%. The same abstraction also lowers the water level further, by a few per cent in S and by up to a fifth in D (Table 21). The backup weakens as the need for it grows.

## 7.5 The answer to the main research question and its limits

The main research question has three parts. First, the canal supply is not reliable against the registered volume. Under the inflows of 1936 to 2009 the present dam delivers that volume in full in 45% to 77% of the years, and one drought of more than a decade dominates the shortfall. Second, groundwater inside A31E could replace the average shortfall in volume, but the study cannot say whether that water would be new or would be taken from the rivers that feed Kromellenboog Dam. In a drought like the long one, the abstraction needed could not be delivered from under the irrigated land in one model structure and would come mostly from the rivers in the other. Third, under the warmer and probably drier conditions projected for about 2050, the reliability by time falls by 4 to 5 points at the median of the projections and by 8 to 11 points at their dry end, and the mean shortfall rises by a quarter to two-thirds; the groundwater answer keeps its form and weakens in degree.

Each bound has a known cause and could be narrowed by specific information. The distance between the two bounds of the canal supply is the unknown operating rule. That the reliabilities are frequencies and not probabilities rests on the unexplained inflow of 1982 to 1994. The distance between the two model structures is the question whether the water table in the valley stands above or below the river bed, and the range of the drawdown is the conductivity and thickness of the valley deposits. Section 8.2 names and ranks the data that would settle each.

The study does less than the Project Brief names in four respects, each by a stated decision:
- **Flood risk** was assessed for one reach at the level of a screening. The design floods could not be checked against recorded peaks, and the flooded extent is not a flood line (Sections 5.11 and 6.9).
- **The pathways of contaminants** were traced by particle tracking and by a screening of the water-quality records. The transport of contaminants was not modelled, and no trend or full solute balance was calculated (Sections 5.12 and 6.10).
- **The runoff of A31E itself** was not modelled under climate change. The climate cases act on the inflow at the upstream boundary, on evaporation, on demand and on recharge.
- **The interaction between groundwater and surface water** rests on one inferred indication, on the difference between two model structures and on a mixing check of electrical conductivity, not on a demonstration.

The groundwater flow model that the Brief asks for was built, and it gives relative results only (Section 5.10).

## 7.6 Flood risk in this reach

The design floods of this reach are uncertain mainly because of the method. At the 1:100-year return period the SDF gives 1 252 m³/s and the Midgley and Pitman formula 889 m³/s, against an RMF of 1 205 m³/s for region K3 and 2 355 m³/s for region K4, on whose boundary the catchment lies (Table 23a). The SDF peak exceeds the RMF of region K3, and the manual warns that in dolomitic catchments the flood may be less than half of the SDF (SANRAL, 2013:3-45). Since nearly half of this catchment is dolomite, the SDF is probably an overestimate here. No method can, however, be preferred on evidence. A statistical analysis would settle the choice, but it needs a record of annual flood peaks of adequate length and quality (Smithers, 2012:635), and none was in hand. The manual requires the SDF to be compared with other methods and any large difference to be explained (SANRAL, 2013:3-4). The spread between the methods, about 40% in peak, is therefore the main uncertainty of the flood result. It is far larger than the difference between the two sets of equations, 5% in flooded area.

The flooded land is better defined than the flood. A peak 29% lower covers only 5% less land, because the valley confines the flow and a larger flood is carried mainly by greater depth (Section 6.9). The land at risk is therefore fairly well defined even with an uncertain flood, while the depths and velocities in it are not. In every plan about 40% of the land mapped as cultivated in the reach is flooded, most of it under more than 1 m of water.

The land mapped as irrigated, which the canal is inferred to supply (Section 1.1), lies on this floodplain. The 1:100-year SDF flood covers about 44 ha of it, 38 ha more than 1 m deep, in 9 of the irrigated patches, and the four plans cover 42 to 46 ha (Section 6.9). Its users therefore face two risks of a different kind:
- a shortage of water that lasts years, in a long drought;
- the flooding of their land, in a rare flood.

A flood over the cultivated land is also a pathway along which soil and what lies on it reach the river (Section 4.5). Whether the canal itself crosses the floodplain is not known, because its route is not recorded.

The reach passes the flood on almost unchanged. The peak falls by 1% to 3% over 15.7 km, because the floodplain holds only 14% to 16% of the flood volume (Section 6.9). The Department rated the spillway of Klein Maricopoort Dam "a major risk" and the spillway capacity of Kromellenboog Dam "a major risk factor" (DWAF, 2004:170–171). These ratings predate the rehabilitation of the spillway of Klein Maricopoort Dam from 2009 (News24, 2011), and its present state is not known. On these results, a flood that leaves the upper dam passes the modelled reach with nearly its full peak on its way to Kromellenboog Dam, together with the floods of the Waterkloofspruit and the Wilgeboomspruit, which the model does not add. The reach does not reduce the risk at the lower spillway. That risk is set by the flood from upstream and by the dam itself.

The flooded extent of this study is a screening, not a flood line. The National Water Act provides that no person may establish a township unless the layout plan shows "lines indicating the maximum level likely to be reached by floodwaters on average once in every 100 years" (section 144, quoted by SANRAL, 2013:11-4). The manual adds that "Any development that affects the 1:100 year flood or even 1:50 year flood must be licensed by DWA" (SANRAL, 2013:11-4). Lines of that standing would need a terrain finer than 30 m, a surveyed channel and a model calibrated against at least one recorded flood (Section 5.10).

## 7.7 What the two waters mean for the canal users, the aquifer under the fields and the lower dam

**The canal users.** The water released from Klein Maricopoort Dam exceeds the upper limit of the target range for irrigation, 40 mS/m, in 86% to 99% of the samples. It does not exceed the guidelines for chloride, sodium or SAR in any sample (Table 23d). The canal itself was not sampled, but it is fed from the same dam, so its water is probably of the same kind. It is saline because it is water from outside A31E. It probably carries the return flows of Zeerust and of the irrigation and mines above the dam, whose nutrient and salt content the Department noted (DWAF, 2004:57), and evaporation, which removes a third of the water that enters the dam, leaves its salts behind (Section 4.5). The canal users therefore face two problems, not one: they depend on water whose supply fails in long droughts and whose salt content lies above the target range for their use. Whether this salinity limits the crops grown depends on the crops and on how the water is applied, which the records do not show, and how the salinity changes as the dam falls in a drought was not examined.

**The aquifer under the fields.** Canal water with a median EC of about 62 mS/m is applied on land above groundwater whose median EC in A31E is 17.7 mS/m (DWS, 2021:163). What drains below the fields carries salt into that aquifer. Where it goes next depends on the structure of the model (Section 6.10). In structure S the water reaches the rivers after a median of 140 years at an effective porosity of 0.10, along paths of a few hundred metres, so that the river receives the drainage of the fields decades to centuries after it entered the ground. An abstraction under the fields would capture this same water before it reaches the river (Section 6.6). In structure D the water stays close to the fields and leaves the water table by evaporation and uptake by plants, which would concentrate its salts further.

In either structure, the aquifer that this study assesses as a backup to the canal receives the drainage of the fields that the canal supplies. Its quality could therefore decline where an abstraction would be placed. No series of groundwater quality exists in A31E to test this. The times of travel are those of the moving water alone and rest on an assumed porosity, so they show only the order of time.

**The lower dam.** Kromellenboog Dam receives both waters. Its median EC of 21.7 mS/m, and the mixing check of Section 6.10, are consistent with a water in which the fresh runoff of A31E dominates. That runoff made up 81% of the dam's inflow from 1987 to 2009 and 98% in the drought (Table 15). The runoff of A31E thus keeps the water of the lower dam fresh relative to the water released from the upper dam. This gives the capture of Section 6.6 a second meaning. In structure S, about nine-tenths of an abstraction under the fields would be taken from the rivers that carry this fresh water. The abstraction would then reduce not only the volume reaching the lower dam but also the share of fresh water in it. The model does not represent this, and it remains an inference.

The nutrients do not separate the paths in the same way. Phosphate exceeds the boundary of 0.025 mg/L in 19% of the samples below the upper dam, in 29% in Kromellenboog Dam and in 20% in the Wilgeboomspruit (Table 23d). Nutrient-rich episodes thus also occur in the runoff of A31E itself and do not come only from upstream. These shares are a screening indication and not a trophic classification (DWAF, 1996b:84).

The water of the lower dam serves the irrigation scheme in A31F (DWAF, 2004:57). The reach between the dams is an ecological flow site whose present category, C, is to be maintained (DWS, 2021:130).

# 8. Recommendations

The recommendations are addressed to the Department of Water and Sanitation (DWS), the North West Premier's Office and AGES. Each rests on a result of this study and goes no further than that result.

## 8.1 For planning and management

1. Treat the registered scheme volume as a volume that the dam cannot assure (DWS; Premier's Office). Under the recorded inflows the present dam delivers 2.34 Mm³/a in full in 45% to 77% of the years, and under the conditions projected for about 2050 in 32% to 70% (cases M and D; Tables 17 and 22). Drought plans for the scheme should assume that a shortfall lasting several years will recur, without giving it a probability (Section 7.1).

2. Decide the restriction rule deliberately and make it known to the irrigators (DWS). The rule affects the reliability more than the demand does, and it trades a smaller, steadier supply against a larger, interrupted one (Section 7.1). The rule derived from the years after 1987 alone lowers the reliability by time from 0.59 to 0.39 (Section 6.4). The water balance of this study can be used to compare candidate rules before one is adopted.

3. Do not take the catchment-scale balance of recharge and use as evidence that groundwater is available to the scheme (DWS). The mean shortfall is 1.6% to 2.8% of the modelled recharge, yet in one structure of the model about nine-tenths of an abstraction of that size is taken from the rivers that lead to Kromellenboog Dam, and in the drought the reach supplied 98% of that dam's inflow (Sections 6.2 and 6.6). Until the source is established, an application to abstract groundwater in the valley below Klein Maricopoort Dam should be assessed for its effect on the flow of this reach.

4. Regard groundwater as a partial backup at most (Premier's Office; AGES). The mean shortfall equals 29 to 51 boreholes at the median strike yield, as a matter of scale, and the present evidence does not support the rate that a drought like that of 1984 to 1995 would require (Section 6.8). If boreholes are investigated, they should be spread over the valley deposits and not concentrated under the fields, because spreading lowers the drawdown many times in both model structures (Table 21). Field tests must confirm this.

5. Plan for the dry end of the projections (DWS; Premier's Office). At the median of the projections for about 2050 the reliability by time falls by 4 to 5 points, and at their dry end by 8 to 11 points. The wettest projections give little more rain than the record, so they offer no counterweight (Section 7.4).

6. Have 1:50-year and 1:100-year flood lines determined for the Klein Marico River between the two dams, and obtain the present state of both spillways, before further development on the floodplain (DWS; Premier's Office). In every design flood about 40% of the land mapped as cultivated in the modelled reach is flooded. The reach passes a flood to Kromellenboog Dam almost unchanged, and the Department rated the spillways of both dams a major risk in 2004 (DWAF, 2004:170–171); the spillway of Klein Maricopoort Dam was being rehabilitated in 2011 (News24, 2011), and its present state is not known (Sections 6.9 and 7.6). Flood lines of legal standing need a finer terrain, a surveyed channel and a model calibrated against a recorded flood, which this screening does not have.

7. Monitor the quality of the water at the head of the canal and in boreholes below the irrigated land (DWS; AGES). The water released from Klein Maricopoort Dam exceeds the target range for irrigation in electrical conductivity in most samples, but the canal itself has never been sampled. No series of groundwater quality exists under the fields whose drainage enters the aquifer assessed as a backup (Sections 6.10 and 7.7). Electrical conductivity and the major ions, sampled at the head of the canal and in the boreholes of Table 24, item 2, would show what the canal users receive and whether the drainage of the fields reaches the aquifer below them.

## 8.2 Priorities for data collection

Table 24 ranks the data that would narrow the answer to the main research question, by the width of the uncertainty that each item removes. The first two items decide between the bounds of the two halves of the answer. Items 3 and 4 would turn the groundwater result from a comparison of cases into an estimate. Items 5 to 7 bear on what the surface-water result means and on how far it can be projected. Item 8 comes last because the sensitivity cases show that the capacity, the evaporation and the release each move the reliability by time by 0.02 or less (Section 6.4). Two items need no field work to begin. An operating rule and delivery records, if they exist, lie with the scheme, and the National Groundwater Archive lists lithological logs for 387 boreholes inside A31E, which were not examined in this study (DWS, s.a.d). Two further items, an annual series of flood peaks for the reach and the monitoring of water quality, do not narrow the answer to the main research question and are therefore not ranked here; they are set out in recommendations 6 and 7 (Section 8.1).

*Table 24: Priorities for data collection, ranked by how much each would narrow the answer to the main research question.*

| Rank | What to collect | What it narrows | Who holds or could collect it |
|---|---|---|---|
| 1 | The operating and restriction rule of the scheme; yearly records of water ordered and delivered, including any supply to Zeerust | The two bounds of the canal supply (Sections 5.4 and 6.4) | DWS North West regional office; the managers of the scheme |
| 2 | Water levels and the electrical conductivity of the water in boreholes beside the Klein Marico River below the dam, with surveyed ground levels; a survey of low flows and their electrical conductivity along the reach | The choice between structures S and D, and with it the source of the pumped water (Sections 6.5 and 6.6) | DWS; AGES |
| 3 | The archive's lithological logs for the valley deposits; pumping tests in those deposits | Their thickness and conductivity; the range of the drawdown and the limit in D (Section 6.6) | National Groundwater Archive (DWS); AGES |
| 4 | Water-level series in the valley and in the western arm | How groundwater responds during a drought and how fast it recovers (Sections 5.10 and 6.8) | DWS groundwater monitoring |
| 5 | The route of the canal, its losses, the fields it serves and the water used on them | What a shortfall at the head of the canal means at the fields; whether the scheme records are the canal's users (Sections 1.1 and 5.10) | DWS; the scheme and its irrigators |
| 6 | A gauge on the inflow to the dam; measured water use above the dam | The untested inflow; the cause and recurrence of the low inflow of 1982 to 1994 (Sections 4.1 and 5.10) | DWS Hydrological Services |
| 7 | Monthly runoff and recharge for about 2050 for the catchments above the dam and for A31E, simulated from downscaled projections | Whether the uniform factors of cases M and D understate the loss: a later start of the rains and longer droughts (Sections 5.5 and 7.4) | Regional climate projections (Engelbrecht, 2019); a catchment model of the upper Klein Marico |
| 8 | The area table of the 1982 basin survey, or a new survey; what the release to the river is; the legend of the record flags; published pan factors | Terms of the water balance that each move the reliability by time by 0.02 or less (Section 6.4) | DWS |

# 9. Conclusions

The records show that the canal supply from Klein Maricopoort Dam has failed for long periods. Since the dam was raised, the canal has carried less than the registered scheme volume in almost two-thirds of the years that can be counted, and for at least ten years in succession from 1984 it carried little or nothing. The inflow to the dam, which comes entirely from outside A31E, stayed low for thirteen years although rainfall had recovered, for a cause that lies upstream and is not known.

Water generated within A31E reaches Kromellenboog Dam below the canal, makes up most of that dam's inflow, and fell far less in the drought than the water from outside. It could not replace the canal supply, but it carried the scheme downstream. The one gauged stream inside A31E lost its dry-season flow early in the drought and regained part of it years before the upper dam recovered; whether the store that feeds it is groundwater is not shown.

A monthly water balance of the dam, tested on a period not used to derive its restriction rule, reproduces the storage and the yearly canal volumes. Under the recorded inflows the present dam delivers the registered volume in full in just under half to three-quarters of the years, depending on whether deliveries are restricted as the dam falls. Restriction makes shortfalls more frequent and shallower and lowers the total volume delivered. The reliability depends more on this rule, which is not known, than on the demand.

The groundwater records show deep water levels in the valleys and low borehole yields, but not the properties of the aquifer. A groundwater flow model in two structures, which differ in the depth at which groundwater leaves the catchment, shows that an abstraction equal to the mean shortfall is small against the modelled recharge and can be delivered in both. The structures disagree on the drawdown and on the source of the water, which is the rivers in one and a deep outflow in the other. Four static water levels cannot decide between them.

Under the warmer and probably drier conditions projected for about 2050, the reliability of the canal supply falls and the shortfalls lengthen: modestly at the median of the published projections and markedly at their dry end. The range between the two is set by the change in rainfall, which is uncertain even in sign and which the inflow amplifies, more than by the warming, on which the projections agree. Lower recharge reduces the discharge of groundwater by about as much, slightly less in one structure and more in the other, so the shortfall grows as the water that an abstraction would draw on shrinks. The cases keep the recorded sequence of years and cannot show a later start of the rains, so they probably understate the loss.

In the reach of the Klein Marico River below the Doringrivier, the 1:100-year design flood ranges from about 890 to 1 250 m³/s with the method, and no recorded peak allows a choice between them. The flooded land varies far less than the flood, because the valley confines the flow: about 40% of the land mapped as cultivated in the reach lies under every design flood, mostly more than 1 m deep. The reach barely reduces a flood, which leaves the modelled reach almost unchanged on its way to Kromellenboog Dam.

The two paths of water through A31E carry different water. The water released from Klein Maricopoort Dam, which feeds the canal, exceeds the target range for irrigation in its salt content in most samples, whereas the runoff generated within A31E is fresh, and Kromellenboog Dam lies between them. Water recharged under the irrigated land reaches the river after decades to centuries in one structure of the model and does not reach it in the other. The aquifer assessed as a backup to the canal is therefore the aquifer that receives the drainage of the fields, whose quality is not monitored. Contaminant transport was not modelled.

The canal supply to A31E is therefore not reliable against the volume registered for it, and its weakness is a drought of many years whose recurrence cannot be given a probability. Groundwater within the catchment could offset the average shortfall in volume, but it cannot yet be said whether that water would be new or the river's own, or whether it could carry the scheme through such a drought. The answer is bounded, and its bounds are set mainly by data that are missing and can be collected.

# References

Adeloye, A.J., Soundharajan, B.-S., Ojha, C.S.P. & Remesan, R. 2016. Effect of hedging-integrated rule curves on the performance of the Pong Reservoir (India) during scenario-neutral climate change perturbations. Water Resources Management, 30(2):445-470. https://doi.org/10.1007/s11269-015-1171-z

Allen, R.G., Pereira, L.S., Raes, D. & Smith, M. 1998. Crop evapotranspiration: guidelines for computing crop water requirements. Rome: FAO. (FAO Irrigation and Drainage Paper, 56). https://www.fao.org/3/X0490E/x0490e00.htm Date of access: 6 Oct. 2026.

Aller, L., Bennett, T., Lehr, J.H., Petty, R.J. & Hackett, G. 1987. DRASTIC: a standardized system for evaluating ground water pollution potential using hydrogeologic settings. Ada, OK: Robert S. Kerr Environmental Research Laboratory, US Environmental Protection Agency. (EPA/600/2-87/035). https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=20007KU4.TXT Date of access: 10 Oct. 2026.

Aminzadeh, M., Friedrich, N., Narayanaswamy, S., Madani, K. & Shokri, N. 2024. Evaporation loss from small agricultural reservoirs in a warming climate: an overlooked component of water accounting. Earth's Future, 12(1), art. e2023EF004050. https://doi.org/10.1029/2023EF004050

Bailey, A.K. & Pitman, W.V. 2016a. Water Resources of South Africa, 2012 study (WR2012): executive summary. Pretoria: Water Research Commission. (WRC report no. TT 683/16). https://www.wrc.org.za/wp-content/uploads/mdocs/TT%20683-16.pdf Date of access: 4 Oct. 2026.

Bailey, A.K. & Pitman, W.V. 2016b. Water Resources of South Africa, 2012 study (WR2012): WRSM/Pitman theory manual. Pretoria: Water Research Commission. (WRC report no. TT 690/16). https://www.wrc.org.za/wp-content/uploads/mdocs/TT%20690-16.pdf Date of access: 10 Oct. 2026.

Bailey, A.K. & Pitman, W.V. 2016c. Water Resources of South Africa, 2012 study (WR2012): WRSM/Pitman user manual. Pretoria: Water Research Commission. (WRC report no. TT 689/16). https://www.wrc.org.za/wp-content/uploads/mdocs/TT%20689-16.pdf Date of access: 10 Oct. 2026.

Barnard, H. 1999. Hydrogeological map series of the Republic of South Africa: Johannesburg 2526, 1:500 000 [Map]. Pretoria: Department of Water Affairs and Forestry. (Listed at: https://www.dws.gov.za/Groundwater/hydromapstatus.aspx) Date of access: 10 Oct. 2026.

Barnett, B., Townley, L.R., Post, V., Evans, R.E., Hunt, R.J., Peeters, L., ... Boronkay, A. 2012. Australian groundwater modelling guidelines. Canberra: National Water Commission. (Waterlines Report Series, no. 82). https://groundwater.com.au/wp-content/uploads/2023/02/australian-groundwater-modelling-guidelines.pdf Date of access: 11 Oct. 2026.

Calow, R.C., MacDonald, A.M., Nicol, A.L. & Robins, N.S. 2010. Ground water security and drought in Africa: linking availability, access, and demand [Abstract]. Ground Water, 48(2):246-256. https://doi.org/10.1111/j.1745-6584.2009.00558.x

Camacho Suarez, V.V., Saraiva Okello, A.M.L., Wenninger, J.W. & Uhlenbrook, S. 2015. Understanding runoff processes in a semi-arid environment through isotope and hydrochemical hydrograph separations. Hydrology and Earth System Sciences, 19(10):4183-4199. https://doi.org/10.5194/hess-19-4183-2015

Canadell, J., Jackson, R.B., Ehleringer, J.R., Mooney, H.A., Sala, O.E. & Schulze, E.-D. 1996. Maximum rooting depth of vegetation types at the global scale. Oecologia, 108(4):583-595. https://link.springer.com/article/10.1007/BF00329030

Cobbing, J. 2018. The North West dolomite aquifers, South Africa: a stalled opportunity for water security and development. Colombo: International Water Management Institute. (GRIPP Case Profile Series, 03). https://doi.org/10.5337/2018.223

Coerver, H.M., Rutten, M.M. & Van de Giesen, N.C. 2018. Deduction of reservoir operating rules for application in global hydrological models. Hydrology and Earth System Sciences, 22(1):831-851. https://doi.org/10.5194/hess-22-831-2018

Cullis, J.D.S. & Phillips, M. 2019. Green Book – Surface water and water supply risks for settlements: a first order assessment of the vulnerability to climate change of surface water supply to municipalities across South Africa. Pretoria: Aurecon & CSIR. (Technical report). https://pta-gis-2-web1.csir.co.za/portal/sharing/rest/content/items/c6ddbbdb4581437ab990ddce8d3edad3/data Date of access: 6 Oct. 2026.

Cuthbert, M.O., Taylor, R.G., Favreau, G., Todd, M.C., Shamsudduha, M., Villholth, K.G., ... Kukuric, N. 2019. Observed controls on resilience of groundwater to climate variability in sub-Saharan Africa. Nature, 572(7768):230-234. https://doi.org/10.1038/s41586-019-1441-7

De Wit, M. & Stankiewicz, J. 2006. Changes in surface water supply across Africa with predicted climate change. Science, 311(5769):1917-1921. https://doi.org/10.1126/science.1119929

DEA (Department of Environmental Affairs). 2013. Long-Term Adaptation Scenarios Flagship Research Programme (LTAS) for South Africa: climate trends and scenarios for South Africa. Pretoria. https://www.sanbi.org/wp-content/uploads/2018/04/ltasclimate-trends-and-scenarios-tech-report2013low-res.pdf Date of access: 6 Oct. 2026.

DFFE (Department of Forestry, Fisheries and the Environment). 2024. South African National Land-Cover (SANLC) 2022 [Dataset]. Pretoria. https://egis.environment.gov.za/sa_national_land_cover_datasets Date of access: 10 Oct. 2026.

Dlamini, N., Senzanje, A. & Mabhaudhi, T. 2023. Assessing climate change impacts on surface water availability using the WEAP model: a case study of the Buffalo river catchment, South Africa. Journal of Hydrology: Regional Studies, 46, art. 101330. https://doi.org/10.1016/j.ejrh.2023.101330

Doherty, J.E. & Hunt, R.J. 2010. Approaches to highly parameterized inversion: a guide to using PEST for groundwater-model calibration. Reston, VA: US Geological Survey. (Scientific Investigations Report 2010-5169). https://pubs.usgs.gov/sir/2010/5169/ Date of access: 11 Oct. 2026.

Douville, H., Raghavan, K., Renwick, J., Allan, R.P., Arias, P.A., Barlow, M., ... Zolina, O. 2021. Water cycle changes. In: IPCC. Climate change 2021: the physical science basis. Contribution of Working Group I to the Sixth Assessment Report. Cambridge: Cambridge University Press. pp. 1055-1210. https://doi.org/10.1017/9781009157896.010

DWA (Department of Water Affairs). 2012. Reservoir records of stations A3R002 (Klein Maricopoort Dam) and A3R003 (Kromellenboog Dam) [Dataset]. Supplied with the Water Resources of South Africa, 2012 study. https://waterresourceswr2012.co.za/resource-centre/ Date of access: 5 Oct. 2026.

DWAF (Department of Water Affairs and Forestry). 1996a. South African water quality guidelines. Vol. 4: Agricultural water use: irrigation. 2nd ed. Pretoria. https://www.dws.gov.za/iwqs/wq_guide/Pol_saWQguideFRESHIrrigationvol4.pdf Date of access: 20 Oct. 2026.

DWAF (Department of Water Affairs and Forestry). 1996b. South African water quality guidelines. Vol. 7: Aquatic ecosystems. Pretoria. https://www.dws.gov.za/iwqs/wq_guide/Pol_saWQguideFRESHAquaticecosystemsvol7.pdf Date of access: 20 Oct. 2026.

DWAF (Department of Water Affairs and Forestry). 2004. Internal strategic perspective for Marico, Upper Molopo and Upper Ngotwane catchments. Pretoria. (Report no. P WMA 03/000/00/0404). https://www.dws.gov.za/Documents/Other/WMA/MaricoISPfeb04.pdf Date of access: 7 Oct. 2026.

DWAF (Department of Water Affairs and Forestry). s.a. The Johannesburg brochure. Pretoria. https://www.dws.gov.za/Groundwater/maps/jhbbrochure.pdf Date of access: 10 Oct. 2026.

DWS (Department of Water and Sanitation). 2021. National Water Act, 1998 (Act no. 36 of 1998): Reserve determination for water resources of the Crocodile (West) and Marico catchments. (Notice 1559). Government Gazette, 45568:126-163, 3 Dec. https://www.gov.za/sites/default/files/gcis_document/202112/45568gon1559.pdf Date of access: 4 Oct. 2026.

DWS (Department of Water and Sanitation). 2023. National Water Act, 1998 (Act no. 36 of 1998): establishment of the Limpopo-Olifants Catchment Management Agency. (Notice 3898). Government Gazette, 49325, 22 Sep. https://www.gov.za/sites/default/files/gcis_document/202309/49325gon3898.pdf Date of access: 4 Oct. 2026.

DWS (Department of Water and Sanitation). 2024. Approved irrigation raw water tariffs 2024/25 FY. https://www.dws.gov.za/Projects/WARMS/Revenue/APPROVED%202024-2025%20FY%20IBOM%20IRRIGATION%20TARIFFS.pdf Date of access: 4 Oct. 2026.

DWS (Department of Water and Sanitation). 2025. Provincial state of dams: North West. https://www.dws.gov.za/hydrology/Weekly/ProvinceWeek.aspx?region=NW Date of access: 4 Oct. 2026.

DWS (Department of Water and Sanitation). s.a.a. Assurance of supply. In: Groundwater dictionary. https://www.dws.gov.za/Groundwater/Groundwater_Dictionary/introduction_assurance_of_supply.htm Date of access: 10 Oct. 2026.

DWS (Department of Water and Sanitation). s.a.b. Groundwater Resource Assessment II. https://www.dws.gov.za/groundwater/GRAII.aspx Date of access: 10 Oct. 2026.

DWS (Department of Water and Sanitation). s.a.c. Hydrological services: verified monthly data for stations A3E003, A3H016, A3H030, A3H031, A3H032, A3H033, A3H042, A3R002 and A3R003 [Dataset]. Pretoria. https://www.dws.gov.za/Hydrology/Verified/hymain.aspx Date of access: 5 Oct. 2026.

DWS (Department of Water and Sanitation). s.a.d. National Groundwater Archive [Dataset]. Pretoria. https://www.dws.gov.za/Groundwater/NGA.aspx Date of access: 10 Oct. 2026.

DWS (Department of Water and Sanitation). s.a.e. Quaternary catchment. In: Groundwater dictionary. https://www.dws.gov.za/Groundwater/Groundwater_Dictionary/introduction_quaternary_catchment.htm Date of access: 10 Oct. 2026.

DWS (Department of Water and Sanitation). s.a.f. Water Management System (WMS): surface water quality data [Dataset]. Pretoria: Resource Quality Information Services. https://www.dws.gov.za/iwqs/wms/default.aspx Date of access: 10 Oct. 2026.

DWS (Department of Water and Sanitation). s.a.g. Water Use Authorisation and Registration Management System (WARMS) [Dataset]. Pretoria. https://www.dws.gov.za/Projects/WARMS/default.aspx Date of access: 10 Oct. 2026.

Ebrahim, G.Y., Villholth, K.G. & Boulos, M. 2019. Integrated hydrogeological modelling of hard-rock semi-arid terrain: supporting sustainable agricultural groundwater use in Hout catchment, Limpopo Province, South Africa. Hydrogeology Journal, 27(3):965-981. https://doi.org/10.1007/s10040-019-01957-6

Enemark, T., Peeters, L.J.M., Mallants, D. & Batelaan, O. 2019. Hydrogeological conceptual model building and testing: a review [Abstract]. Journal of Hydrology, 569:310-329. https://doi.org/10.1016/j.jhydrol.2018.12.007

Engelbrecht, F. 2019. Green Book – Detailed projections of future climate change over South Africa. Pretoria: CSIR. (Technical report). https://pta-gis-2-web1.csir.co.za/portal/sharing/rest/content/items/718369b1f453455e8febdf4f25f68249/data Date of access: 6 Oct. 2026.

Eriksson, P.G., Hattingh, P.J. & Altermann, W. 1995. An overview of the geology of the Transvaal Sequence and Bushveld Complex, South Africa [Abstract]. Mineralium Deposita, 30(2):98-111. https://doi.org/10.1007/BF00189339

Esterhuyse, S. 2017. Developing a groundwater vulnerability map for unconventional oil and gas extraction: a case study from South Africa. Environmental Earth Sciences, 76, art. 626. https://doi.org/10.1007/s12665-017-6961-6

Farr, T.G., Rosen, P.A., Caro, E., Crippen, R., Duren, R., Hensley, S., ... Alsdorf, D. 2007. The Shuttle Radar Topography Mission. Reviews of Geophysics, 45(2), art. RG2004. https://doi.org/10.1029/2005RG000183

Fowler, K., Peel, M., Saft, M., Peterson, T.J., Western, A., Band, L., ... Nathan, R. 2022. Explaining changes in rainfall–runoff relationships during and after Australia's Millennium Drought: a community perspective. Hydrology and Earth System Sciences, 26(23):6073-6120. https://doi.org/10.5194/hess-26-6073-2022

Gutiérrez, J.M., Jones, R.G., Narisma, G.T., Alves, L.M., Amjad, M., Gorodetskaya, I.V., ... Yoon, J.-H. 2021. Atlas. In: IPCC. Climate change 2021: the physical science basis. Contribution of Working Group I to the Sixth Assessment Report. Cambridge: Cambridge University Press. pp. 1927-2058. https://doi.org/10.1017/9781009157896.021

Harbaugh, A.W. 2005. MODFLOW-2005, the U.S. Geological Survey modular ground-water model: the ground-water flow process. Reston, VA: US Geological Survey. (Techniques and Methods 6-A16). https://pubs.usgs.gov/publication/tm6A16 Date of access: 11 Oct. 2026.

Hashimoto, T., Stedinger, J.R. & Loucks, D.P. 1982. Reliability, resiliency, and vulnerability criteria for water resource system performance evaluation. Water Resources Research, 18(1):14-20. https://doi.org/10.1029/WR018i001p00014

Howard, E. & Washington, R. 2020. Tracing future spring and summer drying in southern Africa to tropical lows and the Congo Air Boundary. Journal of Climate, 33(14):6205-6228. https://doi.org/10.1175/JCLI-D-19-0755.1

Iturbide, M., Fernández, J., Gutiérrez, J.M., Pirani, A., Huard, D., Al Khourdajie, A., ... Yelekçi, Ö. 2022. Implementation of FAIR principles in the IPCC: the WGI AR6 Atlas repository. Scientific Data, 9, art. 629. https://doi.org/10.1038/s41597-022-01739-y

Iturbide, M., Gutiérrez, J.M., Alves, L.M., Bedia, J., Cerezo-Mota, R., Cimadevilla, E., ... Vera, C.S. 2020. An update of IPCC climate reference regions for subcontinental analysis of climate model data: definition and aggregated datasets. Earth System Science Data, 12(4):2959-2970. https://doi.org/10.5194/essd-12-2959-2020

Jovanovic, N., Bugan, R.D.H., Tredoux, G., Israel, S., Bishop, R. & Marinus, V. 2017. Hydrogeological modelling of the Atlantis aquifer for management support to the Atlantis Water Supply Scheme. Water SA, 43(1):122-138. https://watersa.net/article/view/10759

Jury, M.R. 2016. Climate influences on upper Limpopo River flow. Water SA, 42(1):63-71. https://doi.org/10.4314/wsa.v42i1.08

Kapangaziwiri, E., Hughes, D.A., Tanner, J. & Slaughter, A. 2011. Resolving uncertainties in the source of low flows in South African rivers using conceptual and modelling studies. In: Abesser, C., Nützmann, G., Hill, M.C., Blöschl, G. & Lakshmanan, E., eds. Conceptual and modelling studies of integrated groundwater, surface water, and ecological systems. Wallingford: International Association of Hydrological Sciences. (IAHS Publication, 345). pp. 127-132. https://iahs.info/uploads/dms/16813.26-127-132-345-04-H01_109_KAPANGAZIWIRI.pdf Date of access: 11 Oct. 2026.

Kjeldsen, T.R. & Rosbjerg, D. 2004. Choice of reliability, resilience and vulnerability estimators for risk assessments of water resources systems. Hydrological Sciences Journal, 49(5):755-767. https://doi.org/10.1623/hysj.49.5.755.55136

Klemeš, V. 1986. Operational testing of hydrological simulation models. Hydrological Sciences Journal, 31(1):13-24. https://doi.org/10.1080/02626668609491024

Kleynhans, C.J. & Louw, M.D. 2007. Module A: EcoClassification and EcoStatus determination. In: River EcoClassification: manual for EcoStatus determination (version 2). Pretoria: Water Research Commission and Department of Water Affairs and Forestry. (WRC report no. TT 329/08). https://www.dws.gov.za/wem/Manuals/EcostatusModuleAMar07.pdf Date of access: 20 Oct. 2026.

Knowling, M.J. & Werner, A.D. 2016. Estimability of recharge through groundwater model calibration: insights from a field-scale steady-state example. Journal of Hydrology, 540:973-987. https://researchnow.flinders.edu.au/en/publications/estimability-of-recharge-through-groundwater-model-calibration-in/

Knüppe, K. 2011. The challenges facing sustainable and adaptive groundwater management in South Africa. Water SA, 37(1):67-79. https://doi.org/10.4314/wsa.v37i1.64110

Konikow, L.F. & Bredehoeft, J.D. 1992. Ground-water models cannot be validated [Abstract]. Advances in Water Resources, 15(1):75-83. [https://doi.org/10.1016/0309-1708(92)90033-X](https://doi.org/10.1016/0309-1708(92)90033-X)

Konikow, L.F. & Leake, S.A. 2014. Depletion and capture: revisiting "The source of water derived from wells". Groundwater, 52(S1):100-111. https://pubs.usgs.gov/publication/70127476

Kovacs, Z. 1988. Regional maximum flood peaks in southern Africa. Pretoria: Department of Water Affairs, Directorate of Hydrology. (Technical Report TR 137). https://www.dws.gov.za/iwqs/reports/tr/TR137_Kovacs_1988_Regional_maximum_flood_peaks_in_southern_Africa.pdf Date of access: 20 Oct. 2026.

Lankford, B., Pringle, C., McCosh, J., Shabalala, M., Hess, T. & Knox, J.W. 2023. Irrigation area, efficiency and water storage mediate the drought resilience of irrigated agriculture in a semi-arid catchment. Science of the Total Environment, 859, art. 160263. https://doi.org/10.1016/j.scitotenv.2022.160263

Le Maitre, D.C. & Colvin, C.A. 2008. Assessment of the contribution of groundwater discharges to rivers using monthly flow statistics and flow seasonality. Water SA, 34(5):549-564. https://doi.org/10.4314/wsa.v34i5.180652

Leake, S.A. & Barlow, P.M. 2013. Understanding and managing the effects of groundwater pumping on streamflow. Reston, VA: US Geological Survey. (Fact Sheet 2013-3001). https://pubs.usgs.gov/publication/fs20133001 Date of access: 11 Oct. 2026.

Lubczynski, M.W. 2006. Groundwater fluxes in arid and semi-arid environments. In: Baba, A., Howard, K.W.F. & Gunduz, O., eds. Groundwater and ecosystems. Dordrecht: Springer. pp. 225-236. https://doi.org/10.1007/1-4020-4738-X_18

MacDonald, A.M., Bonsor, H.C., Ó Dochartaigh, B.É. & Taylor, R.G. 2012. Quantitative maps of groundwater resources in Africa. Environmental Research Letters, 7(2), art. 024009. https://doi.org/10.1088/1748-9326/7/2/024009

MacDonald, A.M., Lark, R.M., Taylor, R.G., Abiye, T., Fallas, H.C., Favreau, G., ... West, C. 2021. Mapping groundwater recharge in Africa from ground observations and implications for water security. Environmental Research Letters, 16(3), art. 034012. https://doi.org/10.1088/1748-9326/abd661

Mbae, M., Hansen, P., Way, C., Mills, F., Willetts, J., Foster, T. & Evans, B. 2024. Onsite sanitation systems and contamination of groundwater: a systematic review of the evidence for risk using the source-pathway-receptor model. PLOS Water, 3(7), art. e0000167. https://doi.org/10.1371/journal.pwat.0000167

Meredith, K.T., Hollins, S.E., Hughes, C.E., Cendón, D.I., Chisari, R., Griffiths, A. & Crawford, J. 2015. Evaporation and concentration gradients created by episodic river recharge in a semi-arid zone aquifer: insights from Cl⁻, δ¹⁸O, δ²H, and ³H. Journal of Hydrology, 529:1070-1078. https://doi.org/10.1016/j.jhydrol.2015.09.025

Michaluk, E. & Keyser, N. 1991. Mafikeng: 1:250 000 geological series, sheet 2524 [Map]. Pretoria: Geological Survey. (Catalogue record: https://gbank.gsj.jp/ld/resource/geolis/90000538.html) Date of access: 10 Oct. 2026.

Moriasi, D.N., Arnold, J.G., Van Liew, M.W., Bingner, R.L., Harmel, R.D. & Veith, T.L. 2007. Model evaluation guidelines for systematic quantification of accuracy in watershed simulations. Transactions of the ASABE, 50(3):885-900. https://swat.tamu.edu/media/1312/moriasimodeleval.pdf Date of access: 10 Oct. 2026.

Nabinejad, S. & Schüttrumpf, H. 2023. Flood risk management in arid and semi-arid areas: a comprehensive review of challenges, needs, and opportunities. Water, 15(17), art. 3113. https://doi.org/10.3390/w15173113

News24. 2011. Flood warning at Klein Maricopoort Dam. 26 January. https://www.news24.com/news24/flood-warning-at-klein-maricopoort-dam-20110126 Date of access: 20 Oct. 2026.

Niswonger, R.G., Panday, S. & Ibaraki, M. 2011. MODFLOW-NWT, a Newton formulation for MODFLOW-2005. Reston, VA: US Geological Survey. (Techniques and Methods 6-A37). https://pubs.usgs.gov/publication/tm6A37 Date of access: 11 Oct. 2026.

Parsons, R.P. & Vermeulen, P.D. 2017. The hidden hydrology of Groenvlei, a lacustrine wetland on the southern Cape coast of South Africa. Water SA, 43(1):42-47. https://doi.org/10.4314/wsa.v43i1.07

Peterson, T.J., Saft, M., Peel, M.C. & John, A. 2021. Watersheds may not recover from drought [Abstract]. Science, 372(6543):745-749. https://doi.org/10.1126/science.abd5085

Pianosi, F., Beven, K., Freer, J., Hall, J.W., Rougier, J., Stephenson, D.B. & Wagener, T. 2016. Sensitivity analysis of environmental models: a systematic review with practical workflow. Environmental Modelling & Software, 79:214-232. https://doi.org/10.1016/j.envsoft.2016.02.008

Pollock, D.W. 2016. User guide for MODPATH Version 7: a particle-tracking model for MODFLOW. Reston, VA: US Geological Survey. (Open-File Report 2016-1086). https://doi.org/10.3133/ofr20161086

Pyburn, M.R. 2015. The hydrogeological relationship between recharge, abstraction and spring flow in the Zeerust dolomitic aquifer. Potchefstroom: North-West University. (Dissertation – MSc). http://hdl.handle.net/10394/20507

Ranasinghe, R., Ruane, A.C., Vautard, R., Arnell, N., Coppola, E., Cruz, F.A., ... Zaaboul, R. 2021. Climate change information for regional impact and for risk assessment. In: IPCC. Climate change 2021: the physical science basis. Contribution of Working Group I to the Sixth Assessment Report. Cambridge: Cambridge University Press. pp. 1767-1926. https://doi.org/10.1017/9781009157896.014

Rouault, M. & Richard, Y. 2005. Intensity and spatial extent of droughts in southern Africa [Abstract]. Geophysical Research Letters, 32(15). https://doi.org/10.1029/2005GL022436

Saft, M., Western, A.W., Zhang, L., Peel, M.C. & Potter, N.J. 2015. The influence of multiyear drought on the annual rainfall-runoff relationship: an Australian perspective. Water Resources Research, 51(4):2444-2463. https://doi.org/10.1002/2014WR015348

Sankarasubramanian, A., Vogel, R.M. & Limbrunner, J.F. 2001. Climate elasticity of streamflow in the United States. Water Resources Research, 37(6):1771-1781. https://doi.org/10.1029/2000WR900330

SANRAL (South African National Roads Agency SOC Ltd). 2013. Drainage manual. 6th ed. Pretoria. https://www.dws.gov.za/projects/nfsp/docs/sanral/Drainage%20Manual%20(Sixth%20Edition%20%5B2013%5D).pdf Date of access: 20 Oct. 2026.

Scheff, J. & Frierson, D.M.W. 2014. Scaling potential evapotranspiration with greenhouse warming. Journal of Climate, 27(4):1539-1558. https://doi.org/10.1175/JCLI-D-13-00233.1

Schulze, R.E. & Schütte, S. 2023. Mapping SCS hydrological soil groups over South Africa at terrain unit spatial resolution. Journal of the South African Institution of Civil Engineering, 65(4):2-9. https://doi.org/10.17159/2309-8775/2023/v65n4a1

Seward, P., Xu, Y. & Brendonck, L. 2006. Sustainable groundwater use, the capture principle, and adaptive management [Abstract]. Water SA, 32(4):473-482. https://ajol.info/index.php/wsa/article/view/5287

SKM (Sinclair Knight Merz). 2013. Australian groundwater modelling guidelines: companion to the guidelines. Canberra: National Water Commission. https://cdn.environment.sa.gov.au/environment/docs/Companion-to-modelling-guidelines.pdf Date of access: 11 Oct. 2026.

Smithers, J.C. 2012. Methods for design flood estimation in South Africa. Water SA, 38(4):633-646. https://scielo.org.za/scielo.php?script=sci_arttext&pid=S1816-79502012000400019 Date of access: 20 Oct. 2026.

Trisos, C.H., Adelekan, I.O., Totin, E., Ayanlade, A., Efitre, J., Gemeda, A., ... Zakieldeen, S. 2022. Africa. In: IPCC. Climate change 2022: impacts, adaptation and vulnerability. Contribution of Working Group II to the Sixth Assessment Report. Cambridge: Cambridge University Press. pp. 1285-1455. https://doi.org/10.1017/9781009325844.011

Troldborg, L., Refsgaard, J.C., Jensen, K.H. & Engesgaard, P. 2007. The importance of alternative conceptual models for simulation of concentrations in a multi-aquifer system [Abstract]. Hydrogeology Journal, 15(5):843-860. https://doi.org/10.1007/s10040-007-0192-y

USACE HEC (US Army Corps of Engineers, Hydrologic Engineering Center). s.a.a. HEC-RAS 2D user's manual, version 7.0. Davis, CA. https://www.hec.usace.army.mil/confluence/rasdocs/r2dum/latest Date of access: 20 Oct. 2026.

USACE HEC (US Army Corps of Engineers, Hydrologic Engineering Center). s.a.b. HEC-RAS hydraulic reference manual, version 7.0. Davis, CA. https://www.hec.usace.army.mil/confluence/rasdocs/ras1dtechref/latest Date of access: 20 Oct. 2026.

USDA-NRCS (United States Department of Agriculture, Natural Resources Conservation Service). 2009. Hydrologic soil groups. In: National engineering handbook, part 630: hydrology. Washington, DC. Chapter 7. https://directives.nrcs.usda.gov/sites/default/files2/1712930634/Part%20630%20-%20Hydrology.pdf Date of access: 10 Oct. 2026.

Walraven, F. 1981. Rustenburg: 1:250 000 geological series, sheet 2526 [Map]. Pretoria: Geological Survey. (Catalogue record: https://gbank.gsj.jp/geolis/geolis_link/90000539/en) Date of access: 10 Oct. 2026.

Watson, A., De Clercq, W., Chow, R., Brookfield, A. & Miller, J. 2026. Combining rainfall-runoff and groundwater modeling to estimate recharge in the data-scarce Verlorenvlei Catchment, South Africa. Hydrogeology Journal (Article in press). https://doi.org/10.1007/s10040-025-03006-x

Woessner, W.W. & Poeter, E.P. 2020. Hydrogeologic properties of earth materials and principles of groundwater flow. Guelph, ON: The Groundwater Project. https://books.gw-project.org/hydrogeologic-properties-of-earth-materials-and-principles-of-groundwater-flow/ Date of access: 20 Oct. 2026.

Woldeamlak, S.T., Batelaan, O. & De Smedt, F. 2007. Effects of climate change on the groundwater system in the Grote-Nete catchment, Belgium. Hydrogeology Journal, 15(5):891-901. https://link.springer.com/article/10.1007/s10040-006-0145-x

Xie, J., Liu, X., Jasechko, S., Berghuijs, W.R., Wang, K., Liu, C., ... Koirala, S. 2024. Majority of global river flow sustained by groundwater. Nature Geoscience, 17(8):770-777. https://doi.org/10.1038/s41561-024-01483-5
