# -*- coding: utf-8 -*-
import time
import numpy as np
import sys

#Literaturwert setzen
me=0.51099895 #MeV

from scipy.integrate import quad
from scipy.special import kv
import PRyM.PRyM_init as PRyMini
import PRyM.PRyM_main as PRyMmain

PRyMini.aTid_flag = True
PRyMini.compute_bckg_flag = True
PRyMini.compute_nTOp_flag = True
PRyMini.compute_nTOp_thermal_flag = False
PRyMini.save_bckg_flag = False
PRyMini.save_nTOp_flag = False
PRyMini.save_nTOp_thermal_flag = False
PRyMini.verbose_flag = False
PRyMini.smallnet_flag = False
PRyMini.julia_flag = False



def varconst(x,y):
    #Wert variieren
    PRyMini.me=me*x
    PRyMini.Omegabh2=y
    PRyMini.eta0b = PRyMini.Omegabh2_to_eta0b*PRyMini.Omegabh2
    PRyMini.tau_n=PRyMini.tau_n*x**-5

    start_time = time.time()
    res = PRyMmain.PRyMresults()
    res=np.append(res,PRyMini.me/me)
    res=np.append(res,PRyMini.eta0b)
    """
    print(" ")
    print(" Neff --> ",res[0])
    print(" Ωνh2 x 10^6 (rel) --> ",res[1])
    print(" Σmν/Ωνh2 [eV] --> ",res[2])
    print(" YP (BBN) --> ",res[3])
    print(" YP (CMB) --> ",res[4])
    print(" D/H x 10^5 --> ",res[5])
    print(" He3/H x 10^5 --> ",res[6])
    print(" Li7/H x 10^10 --> ",res[7])
    print(" m_e (rel) --> ",res[8])
    print(" eta --> ",res[9])
    print(" Omega_b --> ",PRyMini.Omegabh2)
    print(" ")
    print("--- running time: %s seconds ---" % (time.time() - start_time))
    """
    
    return res


x=float(sys.argv[1])
y=float(sys.argv[3])
z=(sys.argv[4])
bbn_results=varconst(x,y)
np.savetxt(z+sys.argv[2]+".txt",bbn_results)
