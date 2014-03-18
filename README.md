hpchadoop
=========

The Hadoop Streaming examples presented for the "Hadoop Essentials" USCD 
Extension Course.  These codes will run on any Hadoop 1.0 cluster (we used
Hadoop 1.0.4), and the submit scripts rely on myHadoop 0.30 to interface Hadoop
and Gordon.

Sample projects and code are also included:

* vcfparser.py - code for parsing VCF files in Hadoop using the PyVCF library
* wordcount.py - the canonical word count example implemented in Python, Perl, and R
* coord - coordination analysis for molecular dynamics simulations (we did not 
  cover this in class, and the documentation is incomplete)

I've also provided the starthadoop.sh script, which contains the commands you
will need to type to get into an interactive session and spin up a Hadoop 
cluster.  Each subdirectory also contains a "submit.qsub" command to run the
entire example non-interactively.  You can examine these scripts to see the
commands you would type to run the examples interactively.
