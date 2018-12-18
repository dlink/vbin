#!/usr/bin/env python

# Goal: report on filesystems that are getting full
# high_water_mark is a percent.  Default = 80

# Examples
#  checkfs.py
#  checkfs.py 90
#  checkfs.py 90%

import sys
from subprocess import Popen, PIPE

# get args - get high_water_mark
high_water_mark = '80'
if len(sys.argv) > 1:
    high_water_mark = sys.argv[1].replace('%', '')
    if not high_water_mark.isdigit():
        print 'unrecognized percentage: %s' % high_water_mark
        sys.exit(1)

# get disk usage
cmd = 'df -m'
process = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
(stdout, stderr) = process.communicate()
if stderr or process.returncode != 0:
    print 'Error: %s.  Returncode: %s' % (stderr.strip(), process.returncode)
    sys.exit(1)
# put it all into a single array
parts = stdout.split()[7:]

# look for disk used_perc > high_water_mark
i = 0
while len(parts) > i:
    filesystem, blocks, used, available, used_perc, mounted_on = parts[i:i+6]
    used_perc2 = used_perc.strip('%')
    if used_perc2 >= high_water_mark:
        print filesystem, blocks, used, available, used_perc, mounted_on
    i += 6

