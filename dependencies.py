# --------------------------------------------------------------------------
# Blendyn -- file dependencies.py
# Copyright (C) 2015 -- 2020 Andrea Zanoni -- andrea.zanoni@polimi.it
# --------------------------------------------------------------------------
# ***** BEGIN GPL LICENSE BLOCK *****
#
#    This file is part of Blendyn, add-on script for Blender.
#
#    Blendyn is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Blendyn  is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Blendyn.  If not, see <http://www.gnu.org/licenses/>.
#
# ***** END GPL LICENCE BLOCK *****
# -------------------------------------------------------------------------- 

from collections import namedtuple

global deps

# Generic dependency.
# :module: name of the module
# :package: name of the python package (if None, package = module)
# :name: name to be given to module during import (if None, name = module)
# :installed: boolean flag indicating if the dependency is found in the system
Dependency = namedtuple("Dependency", ["module", "package", "name", "installed"])

# NetCDF
netcdf_deps = (\
        Dependency(module = "netCDF4", package = None, name = None, installed = False)\
        )

# Plotting with Pygal/Cairosvg
plotting_pygal_deps = (\
        Dependency(module = "pygal", package = None, name = None, installed = False),\
        Dependency(module = "cairosvg", package = None, name = None, installed = False)\
        )

# Control of MBDyn simulation from Blender
psutil_deps = (\
        Dependency(module = "psutil", package = None, name = None, installed = False)\
        )

# Dictionary of dependencies
deps = {
    "NetCDF": netcdf_deps,
    "Plot-Pygal": plotting_pygal_deps,
    "Psutil": psutil_deps
    }
