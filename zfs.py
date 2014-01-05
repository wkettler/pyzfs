#!/usr/bin/python

"""
zfs.py

Python wrapper for libzfs 'zfs' binary.

Copyright (C) 2013  William Kettler <william.p.kettler@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from execute import execute

"""
    Lists the property information for the given datasets.
    
    Inputs:
        fs         (str): filesystem|volume|snapshot
        types      (str): A comma-separated list of types to display
        recursive (bool): Recursively display children
    Outputs:
        <var> (<type>): <description>
"""
def list(fs=None, types=None, recursive=False):
    pass

"""
    Displays  properties  for  the  given  datasets.
    
    Inputs:
        properties (str): Comma separated list of properties, default all
        fs         (str): filesystem|volume|snapshot
        types      (str): A comma-separated list of types to display
        recursive (bool): Recursively display children
    Outputs:
        props (dict): Properties
"""
def get(properties=None, fs=None, types=None, recursive=False):
    pass

"""
    List snapshots.
    
    Inputs:
        fs         (str): Dataset
        recursive (bool): Recursively list snapshots
    Outputs:
        snapshots (dict): Dataset snapshots
"""
def snapshots(fs=None, recursive=False):
    pass
