Hadoop streaming VCF parsingexample for SDSC Gordon
===================================================
Some example scripts to illustrate how to parse a VCF file using Hadoop streaming, Python, and PyVCF.  The tutorial can be found here:

http://users.sdsc.edu/~glockwood/comp/hadoop-vcfparse.php

These files are designed to run on SDSC Gordon.  Unfortunately I do not have an input file that can be publically disseminated for use with this tutorial, so you will have to provide your own (e.g., the VCF output from GATK should work).

The following files are included:
* preprocess.py - the preprocessor script to extract the VCF header
* readvcf.py - the mapper script
* submit.qsub - the submit script to run this all on Gordon.  The actual hadoop commands are contained within this script as well.
