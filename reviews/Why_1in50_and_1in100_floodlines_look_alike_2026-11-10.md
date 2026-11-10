# Why the 1:50 and 1:100 flood lines look almost the same on Map 9

Not for the article. For the meeting with Sascha.

**What the GIS layer is.** The depth layer is the maximum water surface that each mesh cell reached during the run, minus the lowest cell elevation (GIS README). Each cell therefore shows its own peak, whenever it occurred. Your description is correct: the layer is the maximum level reached after the water has passed through the mesh, not a snapshot of one moment.

**Why that gives nearly the same outline.** The two floods differ in size, but the valley confines them:
- The 1:100 peak is 29% above the 1:50 peak.
- The wet area grows by only 3.3%.
- The water surface rises by about 0.28 m.
- The extra wet area is about 0.25 km², which is about 8 m on each side of a flood roughly 490 m wide.
- The valley sides are steep enough (edge slope about 3.5%) that 0.28 m of extra depth moves the edge only a few metres.
- The terrain is 30 m SRTM and the mesh is 30 m, so a shift of 8 m is smaller than one cell. At the scale of Map 9 the two lines overlap.
- The 1:50 extent lies fully inside the 1:100 extent, as it should.

**What to check before the meeting.**
- A shallow-water check gave a difference of +0.37 km² between the two floods, against 0.25 km² from the cell counts. The two numbers come from different methods and are not yet reconciled.
- Table 14 uses mesh cells, while Map 9 uses the RAS Mapper raster. The source of the 1:50 outline on Map 9 (which of the two) still has to be confirmed.
