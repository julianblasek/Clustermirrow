# this code cannot be run directly
# do 'source /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/bin/clik_profile.sh' from your sh shell or put it in your profile

function addvar () {
local tmp="${!1}" ;
tmp="${tmp//:${2}:/:}" ; tmp="${tmp/#${2}:/}" ; tmp="${tmp/%:${2}/}" ;
export $1="${2}:${tmp}" ;
} 

if [ -z "${PATH}" ]; then 
PATH=/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/bin
export PATH
else
addvar PATH /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/bin
fi
if [ -z "${PYTHONPATH}" ]; then 
PYTHONPATH=/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib/python/site-packages
export PYTHONPATH
else
addvar PYTHONPATH /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib/python/site-packages
fi
if [ -z "${LD_LIBRARY_PATH}" ]; then 
LD_LIBRARY_PATH=/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib
export LD_LIBRARY_PATH
else
addvar LD_LIBRARY_PATH /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib
fi
if [ -z "${LD_LIBRARY_PATH}" ]; then 
LD_LIBRARY_PATH=/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main
export LD_LIBRARY_PATH
else
addvar LD_LIBRARY_PATH /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main
fi
CLIK_PATH=/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main
export CLIK_PATH

CLIK_DATA=/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/share/clik
export CLIK_DATA

CLIK_PLUGIN=dust,ffp8,basic,systematics,cibsz,basic_P
export CLIK_PLUGIN

