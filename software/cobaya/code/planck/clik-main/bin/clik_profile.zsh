# this code cannot be run directly
# do 'source /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/bin/clik_profile.zsh' from your zsh shell or put it in your profile

add_path_element() {
    local tmp="${1//:${2}:/:}"
    tmp="${tmp/#${2}:/}"
    tmp="${tmp/%:${2}/}"
    echo -n "${tmp}:${2}"
} 

if [ -z "${PATH}" ]; then 
PATH=/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/bin
export PATH
else
export PATH=$(add_path_element "$PATH" /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/bin)
fi
if [ -z "${PYTHONPATH}" ]; then 
PYTHONPATH=/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib/python/site-packages
export PYTHONPATH
else
export PYTHONPATH=$(add_path_element "$PYTHONPATH" /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib/python/site-packages)
fi
if [ -z "${LD_LIBRARY_PATH}" ]; then 
LD_LIBRARY_PATH=/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib
export LD_LIBRARY_PATH
else
export LD_LIBRARY_PATH=$(add_path_element "$LD_LIBRARY_PATH" /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib)
fi
if [ -z "${LD_LIBRARY_PATH}" ]; then 
LD_LIBRARY_PATH=/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main
export LD_LIBRARY_PATH
else
export LD_LIBRARY_PATH=$(add_path_element "$LD_LIBRARY_PATH" /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main)
fi
CLIK_PATH=/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main
export CLIK_PATH

CLIK_DATA=/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/share/clik
export CLIK_DATA

CLIK_PLUGIN=dust,ffp8,basic,systematics,cibsz,basic_P
export CLIK_PLUGIN

