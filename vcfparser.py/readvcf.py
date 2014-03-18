#!/usr/bin/env python
################################################################################
# Hadoop mapper/reducer for parsing VCF files using PyVCF library
#
# Glenn K. Lockwood, San Diego Supercomputer Center                 July 2013
################################################################################

import vcf
import sys

try:
    ( vcfHeader, target_af ) = sys.argv[1].split(',')
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
