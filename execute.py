#!/usr/bin/python

"""
execute.py

Execute a command in the default shell.

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

import subprocess

"""
    execute
    
    Description:
        Execute a command in the default shell.

    Inputs:
        cmd (str): Command to execute.

    Outputs:
        retcode (int): Exit status.
        stdout  (str): STDOUT
        stderr  (str): STDERR
"""
def execute(cmd):
    try:
        phandle = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT) 
        phandle.poll()
        (stdout, stderr) = phandle.communicate()
        retcode = phandle.returncode
    except Exception as e:
        raise e
        
    return (retcode, stdout, stderr)