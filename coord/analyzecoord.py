#!/usr/bin/env python2
 
import re
import sys
 
display_keys = """Siloxane SiO4 Si3O SiO3 SiO2 SiO1 NBO FreeOH
                  H2O H3O SiOH SiOH2 Si2OH""".split()
 
 
def printargs(counts, isave):
    sys.stdout.write("%-8s" % isave)
    for s in display_keys:
        print "%8d" % counts[s],
        counts[s] = 0
    sys.stdout.write("\n")
 
 
def main():
    sys.stdout.write("%-8s" % "save")
    counts = {};
    for s in display_keys:
        counts[s] = 0
        sys.stdout.write("%8s" % s)
    sys.stdout.write("\n")
 
    isave = 0;
    current = 0;

    regex = re.compile(
        r"""^(\d+)\s+([\d\w]+)\s+\d+\s+[\w\.]+\s+[\w\.]+\s+[\w\.]+\s*$""" )
 
    for line in sys.stdin:
        line = line.lstrip(" \t\r")
        match = regex.match(line)
        if not match:
            continue
 
        specie = match.group(2)
        save = int(match.group(1))
 
        if current == 0:
            current = save
            isave = current
        elif current != save:
            printargs(counts, isave)
            current = save
            isave += 1
 
        if specie in display_keys:
            counts[specie] += 1;
 
    printargs(counts, isave)
 
if __name__ == '__main__':
    main()
