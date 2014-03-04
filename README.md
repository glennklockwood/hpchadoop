hpchadoop
=========

Files for using Hadoop on traditional HPC resources.  Note that the job submission scripts included in this repository are designed to work with myHadoop 0.2x releases only.  They will not work with myHadoop 0.30 or later!

Sample job submission scripts:

* hadoopcluster.fg-sierra.qsub - PBS script for launching Hadoop on FutureGrid Sierra (SDSC); optional support for Hadoop over Infiniband
* hadoopcluster.fg-hotel.qsub - PBS script for launching Hadoop on FutureGrid Hotel (UIC)
* hadoopcluster.xsede-gordon.qsub - PBS script for launching Hadoop on Gordon using TCP over Infiniband

Sample projects and code are also included:

* coord - coordination analysis for molecular dynamics simulations (documentation is incomplete)
* vcfparser.py - code for parsing VCF files in Hadoop using the PyVCF library
* wordcount.py - the canonical word count example implemented in Python, Perl, and R
