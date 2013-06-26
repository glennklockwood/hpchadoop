#!/usr/bin/env python2

import sys

for line in sys.stdin:
        line = line.lstrip(" \t\r")
        match = regex.match(line)
        if not match:
            continue

        specie = match.group(2)
        save = int(match.group(1))
 
        key = "%s-%s\t1" % ( save, specie )
    print key
