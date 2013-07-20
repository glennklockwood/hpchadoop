#!/usr/bin/env python
#
#   Hadoop mapper/reducer for parsing VCF files using PyVCF library
#
#   Glenn K. Lockwood, San Diego Supercomputer Center               July 2013
#

import vcf
import sys
import getopt

def main():

    opts, args = getopt.getopt(sys.argv[1:], "b:m:re:")

    for o, a in opts:
        if o == "-b":
            preprocess(a)
        elif o == '-m':
            mapper(a)
        elif o == "-r":
            reducer(a)
        elif o == "-e":
            postprocess(a)
        else:
            raise Exception('Must specify an action (-b, -m, -r, or -e)')

################################################################################
### Mapper: Extracts VCF records relevant to analysis performed by reducer
###
def mapper(arg):
    try:
        ( vcfHeader, target_af ) = arg.split(',')
        target_af = float(target_af)
    except ValueError:
        raise ValueError('Must specify -m headerfile.txt,min_allele_freq, e.g., -m header.txt,0.30')

    vcf_reader = vcf.Reader(open(vcfHeader, 'r'))

    vcf_reader._reader = sys.stdin

    vcf_reader.reader = (line.rstrip() for line in vcf_reader._reader if line.rstrip() and line[0] != '#')

    for record in vcf_reader:

        chrom = record.CHROM
        id = record.ID
        pos = record.POS
        ref = record.REF
        alt = record.ALT

        try:
            for idx, af in enumerate(record.INFO['AF']):
                if af > target_af:
                    print( "%d\t%s\t%d\t%s\t%s\t%.2f\t%d\t%d" % (
                        record.POS,
                        record.CHROM,
                        record.POS,
                        record.REF,
                        record.ALT[idx],
                        record.INFO['AF'][idx],
                        record.INFO['AC'][idx],
                        record.INFO['AN'] ) )
        except KeyError:
            pass
         
################################################################################
### Reducer: just passes through all records it receives
###
def reducer(arg):
    for line in sys.stdin:
        sys.stdout.write(line)

################################################################################
### Preprocess: pull the header out of the VCF file and print to stdout
###
def preprocess(arg):
    fvcf = open(arg, 'r')
    for line in fvcf:
        if line[0] == '#':
            sys.stdout.write(line)
        else:
            break
    fvcf.close()

################################################################################
### Postprocess: does nothing
###
def postprocess(arg):
    for line in sys.stdin:
        sys.stdout.write(line)

if __name__ == '__main__':
    main()
