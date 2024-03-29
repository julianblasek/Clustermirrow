import os
from cobaya import Likelihood
class lithium(Likelihood):

    def initialize(self):
        self.set_timing_on(True)

        pass

    def get_requirements(self):

        return {'Li7':None, 'D': None, 'Yp':None}

    def logp(self, **params_values):
        chi2 = 0
        chi2 += (params_values['Li7'] - 1.6e-10) ** 2 / 0.3e-10 ** 2 #Lithium
        chi2 += (params_values['D'] - 2.54e-5) ** 2 / 0.04e-5 ** 2 #Deuterium
        #chi2 += (params_values['He3'] - 2.94e-5) ** 2 / 0.049e-5 ** 2 #He3
        chi2 += (params_values['Yp'] - 0.2449) ** 2 / 0.004 ** 2 #Heliumanteil gesamt
        
        return -chi2 / 2

info = {
    #Chain Pfad
    "output":os.path.expanduser("/home/em632080/cobaya/test2/step1/chains/"), #mit BBN
    #"output":os.path.expanduser("/home/em632080/cobaya/test2/step2/chains/"), #mit BBN ohne Li
    #"output":os.path.expanduser("/home/em632080/cobaya/test2/step3/chains/"), #ohne BBN
    "debug":False,
    "test":False,
    "stop_at_error":False,
    "timing":True,
    "resume":False,
    "force":True,
    "theory": {
        "classy": {
            "extra_args": {
                # default CLASS settings:
                "output": "tCl,pCl,lCl,mPk",
                "non linear": "halofit",
                "lensing":"yes",
                "compute damping scale":"yes",
                #'N_ncdm' : 1,
                #'m_ncdm' : 0.06,
                #'T_ncdm' : 0.71611,
                #"N_ur": 2.038,
                "varying_fundamental_constants":"readfile", #mit oder ohne VPC
            },
        #Welche Class Version    
        "path":"/home/em632080/class/step1/class_public" #mit BBN
        #"path":"/home/em632080/class/step2/class_public" #mit BBN ohne Li
        #"path":"/home/em632080/class/step3/class_public" #ohne BBN
        },
    },
    "likelihood": {
        "planck_2018_highl_plik.TTTEEE":{},
        "planck_2018_lensing.clik":{},
        "planck_2018_lowl.TT_clik":{},
        "planck_2018_lowl.EE_clik":{},
        
        "bbn_elements": lithium(), #mit oder ohne Elements
        "bao.sixdf_2011_bao": {},
        "bao.sdss_dr7_mgs": {},
        "bao.sdss_dr12_consensus_bao": {},
        # "sn.pantheon": {},
        },
    'params': {'A': {'derived': 'lambda A_s: 1e9*A_s',
                    'latex': '10^9 A_\\mathrm{s}'},
                'A_s': {'latex': 'A_\\mathrm{s}',
                        'value': 'lambda logA: 1e-10*np.exp(logA)'},
                
                'h': {'latex': 'h',
                    'prior': {'max': 1.0, 'min': 0.4},
                    'proposal': 0.01,     
                    'ref': {'dist': 'norm', 'loc': 0.699, 'scale': 0.001}
                    },
                
                'clamp': {'derived': 'lambda A_s, tau_reio: '
                                    '1e9*A_s*np.exp(-2*tau_reio)',
                        'latex': '10^9 A_\\mathrm{s} e^{-2\\tau}'},
                
                'logA': {'drop': True,
                        'latex': '\\log(10^{10} A_\\mathrm{s})',
                        'prior': {'max': 3.257, 'min': 2.837},
                        'proposal': 0.02,   
                        'ref': {'dist': 'norm', 'loc': 3.046, 'scale': 0.002}
                        },
                
                
                'step': {'latex': 'step',
                        'prior': {'max': 1.2, 'min': 0.8},
                        'proposal': 0.005,
                        'ref': {'dist': 'norm', 'loc': 1.0, 'scale': 0.003}
                        },
                
                
                
                'n_s': {'latex': 'n_\\mathrm{s}',
                        'prior': {'max': 1.0235, 'min': 0.9095},
                        'proposal': 0.004,    
                        'ref': {'dist': 'norm', 'loc': 0.967, 'scale': 0.0004}
                        },
                'omega_b': {'latex': '\\Omega_\\mathrm{b} h^2',
                            'prior': {'max': 0.02452, 'min': 0.02032},
                            'proposal': 0.0002,
                            'ref': {'dist': 'norm','loc': 0.0225,'scale': 0.00002}
                            },
                'omega_cdm': {'latex': '\\omega_\\mathrm{cdm} ',
                            'prior': {'max': 0.1329, 'min': 0.1057},
                            'proposal': 0.003,
                            'ref': {'dist': 'norm', 'loc': 0.123, 'scale': 0.003}
                            },
                'sigma8': {'latex': '\\sigma_8'},
                
                'Li7': {'latex': 'Li7'},
                'Yp': {'latex': 'Yp'},
                'D': {'latex': 'D'},
                'eta': {'latex': 'eta'},
                
                'tau_reio': {'latex': '\\tau_\\mathrm{reio}',
                            'prior': {'max': 0.08449, 'min': 0.0276},
                            'proposal': 0.01,   #053075671
                            'ref': {'dist': 'norm', 'loc': 0.058, 'scale': 0.001}
                            },
    },  
    "sampler": { 
        "mcmc": {
            "drag":True,
            "learn_proposal": True,
            "oversample_power": 0.4,
            "proposal_scale":2.1,
            "Rminus1_stop": 0.01,
            "max_tries": 24000,
            "covmat": os.path.expanduser("/home/em632080/software/cobayafork/test2/covmats/step.covmat"), #mit Step
            },
        },

    }


from cobaya.run import run

import cobaya 

updated_info, sampler = run(info)