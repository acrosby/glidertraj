#GliderTraj

This is a super simple module to write ocean glider trajectories in the IOOS glider format. The writer templates are based on http://github.com/IOOSProfilingGliders/Real-Time-File-Format .

## Convert ROMS drifter simulations

The module has some high-level functionality to read and convert ROMS simulated drifters to the IOOS glider netCDF format.

```python
from ioos_glider import romssim_write

romssim_write(romssimfile, ioosglideroutput, ver="0.0")
```

## geojson Web Service

This Python module contains a small Flask app that will service the IOOS glider netCDF files as geojson. For a test run you can start the service like so:

```bash
python ioos_glider.py
```

And to use it:

[http://localhost:5000/geojson/http://tds.gliders.ioos.us/thredds/dodsC/RU5MonthTime.ncml](http://localhost:5000/geojson/http://tds.gliders.ioos.us/thredds/dodsC/RU5MonthTime.ncml)

For jsonp style callback wrapping:

[http://localhost:5000/geojson/http://tds.gliders.ioos.us/thredds/dodsC/RU5MonthTime.ncml?callback=MyCallbackFunction](http://localhost:5000/geojson/http://tds.gliders.ioos.us/thredds/dodsC/RU5MonthTime.ncml?callback=MyCallbackFunction)

## Requires:

```bash
pip install numpy
pip install netCDF4
pip install geojson
pip install flask
```