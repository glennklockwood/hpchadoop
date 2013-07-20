Hadoop streaming VCF parsingexample for SDSC Gordon
===================================================
Some example scripts to illustrate how to parse a VCF file using Hadoop streaming, Python, and PyVCF.  The tutorial can be found here:

http://users.sdsc.edu/~glockwood/comp/hadoop-vcfparse.php

These files are designed to run on SDSC Gordon.  Unfortunately I do not have an input file that can be publically disseminated for use with this tutorial, so you will have to provide your own (e.g., the VCF output from GATK should work).

The parsevcf.py script contains the preprocessor, mapper, reducer, and postprocessor.  In this example only the preprocessor and mapper are needed, and the reducer and postprocessor do nothing.  The following command line options control what stage of the map/reduce process parsevcf.py will use:

* parsevcf.py -b <vcf file> invokes the preprocessor (-b for beginning) step.  Prints the header of <vcf file> to stdout.
* parsevcf.py -m <header file>,<min af> invokes the mapper and takes VCF records from stdin and parses them according to the VCF header contained in <header file>.  It then prints out some relevant information for every variant with an allele frequency greater than <min af>.  There is no space between the comma separating <header file> from <min af>; e.g., parsevcf.py -m header.txt,0.30
* parsevcf.py -r invokes the reducer.  In this version the reducer simply passes all data through, but it would be easy to modify to do something useful.
* parsevcf.py -e invokes the postprocessor (-e for ending).  In this version it simply passes all of stdin to stdout.

I have also included streaming-parsevcf.xsede-gordon.qsub, the submit script that will run the Hadoop streaming with parsevcf.py script.  It currently calls both mapper and reducer, even though the reduce does nothing.  To disable the reduce step altogether, pass "-D mapred.reduce.tasks=0" on the hadoop jar command.
