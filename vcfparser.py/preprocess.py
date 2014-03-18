#!/usr/bin/env python

import sys

fvcf = open(sys.argv[1], 'r')
for line in fvcf:
    if line[0] == '#':
        sys.stdout.write(line)
    else:
        break
fvcf.close()
