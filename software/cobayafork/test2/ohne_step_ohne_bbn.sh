#!/usr/bin/zsh

# ask for ten tasks
#SBATCH --ntasks=10

#SBATCH --cpus-per-task=1

# maximal time
#SBATCH --time=2-23:10:00 	#d-hh:mm:ss 2-23:10:00

# ask for less tahn 4 GB memory per task=MPI rank
#SBATCH --mem-per-cpu=3900M   
 
# name the job
#SBATCH --job-name=5_cobaya_run                        

# number of nodes
###SBATCH --nodes=1

### MPI ranks per node
###SBATCH --sockets-per-node=1
###SBATCH --cores-per-socket=4

# declare the merged STDOUT/STDERR file
#SBATCH --output=/home/em632080/software/cobayafork/test2/output/ohne_step_ohne_bbn.txt             

# address account
#SBATCH --account=rwth1302              

####SBATCH --ntasks-per-node=1

### beginning of executable commands
module purge
module load iimpi
module load Python/3.10
module load imkl
module load Tk
module load mpi4py/3.1.4

export PATH=/rwthfs/rz/cluster/home/em632080/.local/bin:$PATH

$MPIEXEC -n 10 $FLAGS_MPI_BATCH python ohne_step2.py                
