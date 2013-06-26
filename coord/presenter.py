#!/usr/bin/env python2

import sys


display_keys = """Siloxane SiO4 Si3O SiO3 SiO2 SiO1 NBO FreeOH
    H2O H3O SiOH SiOH2 Si2OH""".split()

data = {}
for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t',1)
    save, specie = key.split('-',1)
    if save not in data:
        data[save] = {}
    data[save][specie] = int(value)

sys.stdout.write("%-8s" % 'Save')
for s in display_keys:
    sys.stdout.write( "%8s" % s )
sys.stdout.write("\n")

keys = data.keys()
for key in sorted(data.keys(), key=lambda a:int(a)):
        sys.stdout.write("%-8s" % key)
        for s in display_keys:
            if s in data[key]:
                sys.stdout.write( "%8d" % data[key][s] )
            else:
                sys.stdout.write("%8d" % 0 )
        sys.stdout.write("\n")

if __name__ == '__main__':
    main()
