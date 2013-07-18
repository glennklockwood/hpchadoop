Hadoop streaming wordcount example for SDSC Gordon
==================================================
Some example scripts to illustrate wordcount using Hadoop streaming and Python.  The tutorial can be found here:

http://users.sdsc.edu/~glockwood/comp/hadoopstreaming.php

These files are designed to run on SDSC Gordon, and the tutorial uses the text of Moby Dick.  This input text can be downloaded from Project Gutenberg (http://www.gutenberg.org/cache/epub/2701/pg2701.txt).

* mapper.py - The mapper script
* reducer.py - The reducer script
* streaming-wordcount-py.xsede-gordon.qsub - The submit script that will run the Hadoop streaming with mapper.py and reducer.py non-interactively

For people more comfortable with Perl, I also wrote the same mappers/reducers in that language.  A submit script (virtually identical) is also included:
* mapper.pl
* reducer.pl
* streaming-wordcount-pl.xsede-gordon.qsub


