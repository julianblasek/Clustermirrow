# this code cannot be run directly
# do 'source /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/bin/clik_profile.csh' from your csh shell or put it in your profile

 

if !($?PATH) then
setenv PATH /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/bin
else
set newvar=$PATH
set newvar=`echo ${newvar} | sed s@:/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/bin:@:@g`
set newvar=`echo ${newvar} | sed s@:/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/bin\$@@` 
set newvar=`echo ${newvar} | sed s@^/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/bin:@@`  
set newvar=/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/bin:${newvar}                     
setenv PATH /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/bin:${newvar} 
endif
if !($?PYTHONPATH) then
setenv PYTHONPATH /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib/python/site-packages
else
set newvar=$PYTHONPATH
set newvar=`echo ${newvar} | sed s@:/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib/python/site-packages:@:@g`
set newvar=`echo ${newvar} | sed s@:/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib/python/site-packages\$@@` 
set newvar=`echo ${newvar} | sed s@^/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib/python/site-packages:@@`  
set newvar=/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib/python/site-packages:${newvar}                     
setenv PYTHONPATH /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib/python/site-packages:${newvar} 
endif
if !($?LD_LIBRARY_PATH) then
setenv LD_LIBRARY_PATH /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib
else
set newvar=$LD_LIBRARY_PATH
set newvar=`echo ${newvar} | sed s@:/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib:@:@g`
set newvar=`echo ${newvar} | sed s@:/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib\$@@` 
set newvar=`echo ${newvar} | sed s@^/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib:@@`  
set newvar=/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib:${newvar}                     
setenv LD_LIBRARY_PATH /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/lib:${newvar} 
endif
if !($?LD_LIBRARY_PATH) then
setenv LD_LIBRARY_PATH /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main
else
set newvar=$LD_LIBRARY_PATH
set newvar=`echo ${newvar} | sed s@:/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main:@:@g`
set newvar=`echo ${newvar} | sed s@:/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main\$@@` 
set newvar=`echo ${newvar} | sed s@^/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main:@@`  
set newvar=/rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main:${newvar}                     
setenv LD_LIBRARY_PATH /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main:${newvar} 
endif
setenv CLIK_PATH /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main

setenv CLIK_DATA /rwthfs/rz/cluster/home/em632080/software/cobaya/code/planck/clik-main/share/clik

setenv CLIK_PLUGIN dust,ffp8,basic,systematics,cibsz,basic_P

