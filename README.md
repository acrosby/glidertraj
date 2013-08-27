#GliderTraj

This is a super simple module to write ocean glider trajectories in the IOOS glider format. The writer templates are based on http://github.com/IOOSProfilingGliders/Real-Time-File-Format .

## Convert ROMS drifter simulations

The module has some high-level functionality to read and convert ROMS simulated drifters to the IOOS glider netCDF format.

## geojson Web Service

This Python module contains a small Flask app that will service the IOOS glider netCDF files as geojson.