#!/usr/bin/python

#Parse arguments
import argparse
argParse = argparse.ArgumentParser(description='Creates a fslview LUT out of a matplotlib colormap')
argParse.add_argument('cmap',help='Name of matplotlib colormap',nargs=1,type=str)
argParse.add_argument('out',help='Root for output file',nargs=1,type=str)
args = argParse.parse_args()

#Load the other libraries we need
import numpy as np, matplotlib.pyplot as plt, sys

#Open lut file for writing
try:
	lutOut = open('%s.lut'%(args.out[0]), 'w')
except(IOError):
	print 'Error: Cannot write %s'%(args.out[0])
	sys.exit()

#Write fsl lut header
lutOut.write('%!VEST-LUT\n')
lutOut.write('%%BeginInstance\n')
lutOut.write('<<\n')
lutOut.write('/SavedInstanceClassName /ClassLUT\n')
lutOut.write('/PseudoColorMinimum 0.00\n') 
lutOut.write('/PseudoColorMaximum 1.00\n')
lutOut.write('/PseudoColorMinControl /Low\n')
lutOut.write('/PseudoColorMaxControl /High\n')
lutOut.write('/PseudoColormap [\n')

#Get full colormap
try:
	cmap = plt.get_cmap(args.cmap[0])
except(ValueError):
	print 'ERROR: %s doesn\'t seem to be a valid matplotlib colormap name...'%(args.cmap[0])
	sys.exit()

#Write out color
for i in range(255):
	lutOut.write('<-color{%.6f,%.6f,%.6f}->\n'%(cmap(i)[0],cmap(i)[1],cmap(i)[2]))

#Write out footer
lutOut.write(']\n')
lutOut.write('>>\n')

#Close it up
lutOut.close()

#Make a plot of the lut 
mapX = np.linspace(0,1,225); mapCoords = np.vstack((mapX,mapX))
fig = plt.figure(1,figsize=(1,5),frameon=False)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)
ax.imshow(np.flipud(mapCoords.T),cmap=cmap,interpolation="nearest",aspect='auto')
plt.savefig('%s.jpeg'%(args.out[0]))
