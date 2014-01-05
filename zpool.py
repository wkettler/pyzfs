#!/usr/bin/python

"""
zpool.py

Python wrapper for libzfs 'zpool' binary.

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
    Lists all pools along with a health status and
        space usage.   
    
    Inputs:
        pool (str): Storage pool
    Outputs:
        list (dict): Pool list
"""
def list(pool=None):
    pass

"""
    Displays the detailed health status for all pools.
    
    Inputs:
        pool (str): Storage pool
    Outputs:
        status (dict): Pool status
"""
def status(pool=None):
    pass

"""
    Displays the command history of the specified  pool  or
        all pools if no pool is specified.
    
    Inputs:
        pool (str): Storage pool
    Outputs:
        history (list): Pool history
"""
def history(pool=None):
    pass

"""
    Retrieves the given list of properties for the specified pool or
        all pools if no pool is specified.
    
    Inputs:
        pool       (str): Storage pool
        properties (str): Comma separated list of properties, default all
    Outputs:
        props (dict): Pool properties
"""
def get(pool=None, properties=None):
    pass

"""
    Displays I/O statistics for the given pools.
    
    Inputs:
        pool     (str): Storage pool
        interval (int): Interval in seconds
        ct       (int): Number of reports
    Outputs:
        stats (dict): Iostat output
"""
def iostat(pool, interval, ct):
    pass

"""
    Displays the detailed health status for all pools
        exhibiting errors.
    
    Inputs:
        None
    Outputs:
        errors (dict): Pool status
"""
def errors():
    pass
