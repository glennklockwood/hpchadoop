# You would type this to get your cluster nodes reserved and log into them
qsub -I -l nodes=2:ppn=16:native:flash,walltime=2:00:00 -q normal

# This generates the Hadoop cluster configuration
myhadoop-configure.sh

# This is the Hadoop control script to start all of the Hadoop daemons
start-all.sh
