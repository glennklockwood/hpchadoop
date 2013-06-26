#!/usr/bin/env python2

import sys
import re
import getopt

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "mrp")
    except getopt.GetoptError:
        print("Invalid option")
        sys.exit(1)
    if "-m" in [o[0] for o in opts]:
        mapper()
    elif "-r" in [o[0] for o in opts]:
        reducer()
    elif "-p" in [o[0] for o in opts]:
        presenter()
    else:
        print("Invalid option")
        sys.exit(1)

def mapper():
    regex = re.compile(
        r"""^(\d+)\s+([\d\w]+)\s+\d+\s+[\w\.]+\s+[\w\.]+\s+[\w\.]+\s*$""" )
 
    for line in sys.stdin:
        line = line.lstrip(" \t\r")
        match = regex.match(line)
        if not match:
            continue

        specie = match.group(2)
        save = int(match.group(1))
 
        key = "%s-%s\t1" % ( save, specie )
        print key

def reducer():
    current_word = None
    current_count = 0
    word = None

    for line in sys.stdin:
        line = line.strip()
        word, count = line.split('\t', 1)

        try:
            count = int(count)
        except ValueError:
            continue

        if current_word == word:
            current_count += count
        else:
            if current_word:
                print '%s\t%s' % ( current_word, current_count )
            current_count = count
            current_word = word

    if current_word == word:
        print '%s\t%s' % ( current_word, current_count )

def presenter():
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
