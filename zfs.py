#!/usr/bin/python

"""
zfs.py

Python wrapper for the libzfs 'zfs' binary.

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

ZFS = "/sbin/zfs"

def zfs(cmd, *args):
    """
    Execute a zfs command.

    Inputs:
        cmd (str): sub-command, i.e. create, get
    Outputs:
        retcode  (int): Return code
        output  (list): STDOUT/STDERR
    """
    retcode, output = execute(" ".join([ZFS, cmd, " ".join[args]]))

    return retcode, output


def list(fs=None, types=None, recurs=False):
    """
    Lists the property information for the given datasets.

    Inputs:
        fs      (str): filesystem|volume|snapshot
        types  (list): Types to display, where type is one of filesystem,
                       snapshot, volume
        recurs (bool): Recursively display children
    Outputs:
        <var> (<type>): <description>
    """
    pass


def get(fs=None, props=None, types=None, recurs=False):
    """
    Displays  properties  for  the  given  datasets.

    Inputs:
        props  (list): Properties, default all
        fs      (str): filesystem|volume|snapshot
        types  (list): Types to display, where type is one of filesystem,
                       snapshot, volume
        recurs (bool): Recursively display children
    Outputs:
        props (dict): Properties
    """
    pass


def snapshots(fs=None, recurs=False):
    """
    List snapshots.

    Inputs:
        fs      (str): Dataset
        recurs (bool): Recursively list snapshots
    Outputs:
        snaps (dict): Dataset snapshots
    """
    pass
