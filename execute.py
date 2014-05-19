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
import signal

class Execute(Exception):
    pass

class Timeout(Exception):
    pass

class Retcode(Exception):
    pass

def alarm_handler(signum, frame):
    raise Timeout

def execute(cmd, timeout=None):
    """
    Execute a command in the default shell. If a timeout is defined the command
    will be killed if the timeout is exceeded.

    Inputs:
        cmd     (str): Command to execute
        timeout (int): Command timeout in seconds
    Outputs:
        retcode  (int): Return code
        output  (list): STDOUT/STDERR
    """
    # Define the timeout signal
    if timeout:
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.alarm(timeout)

    try:
        # Execute the command and wait for the subprocess to terminate
        # STDERR is redirected to STDOUT
        phandle = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)

        # Read the stdout/sterr buffers and retcode
        stdout, stderr = phandle.communicate()
        retcode = phandle.returncode
    except Timeout as t:
        # Kill the running process
        phandle.kill()
        raise Timeout("command timeout of %ds exceeded" % timeout)
    except Exception as e:
        raise Execute(e)
    else:
        # Possible race condition where alarm doesn't disabled in time
        signal.alarm(0)

    # Split lines into list
    if stdout and stdout is not None:
        output = stdout.strip()
    else:
        output = None

    return retcode, output
