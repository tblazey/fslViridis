# fslViridis

Goal of this mini project is to port the great perceptually uniform colormaps from matplotlib (https://bids.github.io/colormap/) to FSL's fslview.

This project contains LUTs for
1. Viridis
2. Inferno
3. Plasma
4. Magma

There is also a little jpeg image for each map. Finally, there is a simple Python script that creates lookup tables for fslview from matplotlib colormaps.

Basic usage:

python makeFslLut.py [CMAP] [OUT]
	-> CMAP is a valid matplotlib colormap name. See http://matplotlib.org/examples/color/colormaps_reference.html
	-> OUT root for output. Will make a lut (OUT.lut) and a snapshot of the colormap (OUT.jpeg)
