# fslViridis

Goal of this mini project is to port the great perceptually uniform colormaps from matplotlib (https://bids.github.io/colormap/) to FSL.

This project contains LUTs for:
	-> Viridis
	-> Inferno
	-> Plasma
	-> Magma

There is also a little jpeg image for each map.

Also contains a simple Python script that creates lookup tables for FSL's fslview from matplotlib colormaps

Basic usage:

python makeFslLut.py <CMAP> <OUT>
	-> CMAP is a valid matplotlib colormap name. See http://matplotlib.org/examples/color/colormaps_reference.html
	-> OUT root for output. Will make a lut (OUT.lut) and a snapshot of the colormap (OUT.jpeg)
