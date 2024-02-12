import numpy as np
import getdist as gd
import getdist.plots as gdplt
import matplotlib.pyplot as plt
import getdist
from getdist import MCSamples, chains
# Enable LaTeX rendering
plt.rcParams['text.usetex'] = True
h_min, h_max = 0.7304 - 0.0104, 0.7304 + 0.0104
li_min, li_max = 1.6e-10 - 0.03e-10, 1.6e-10 + 0.03e-10
d_min, d_max = 2.54e-5 - 0.04e-5, 2.54e-5 + 0.04e-5
y_min, y_max = 0.2449 - 0.004, 0.2449 + 0.004


all_samples1 = []
all_samples2=[]

titles1 = ["without el. fractions in likelihood", "with Li, He, D in likelihood", "with He, D in likelihood"]
contour_colors1 = ['blue', 'red', 'green']

titles2 = ["without el. fractions in likelihood", "with Li, He, D in likelihood", "with He, D in likelihood"]
contour_colors2 = ['blue', 'red', 'green']


file_path=["./step3/chains/","./step1/chains/","./step2/chains/","./raw2/chains/","./raw1/chains/","./raw4/chains/"]
sample_files = ["1.txt", "2.txt", "3.txt", "4.txt", "5.txt", "6.txt", "7.txt", "8.txt", "9.txt", "10.txt"]
names1 = [r'$H_0$', r'$m_{e}^x$', r'$^7Li/H$', r'$D/H$', r'$Y_p$']
names2 = [r'$H_0$', r'$ $', r'$^7Li/H$', r'$D/H$', r'$Y_p$']


def datagen(i,pfad):
    if(i==0):
        samples = []
        data = []
        for file in sample_files:
            sample = np.genfromtxt(pfad + file)
            samples.append(sample)

        data = np.vstack(samples)
        lithium_column = data[:, 33]  # Lithium-Spalte auswählen (Index 34)
        yp_column = data[:, 34]
        deuterium_column= data[:, 35]
        eta_column=data[:,36]
        empty= np.zeros((eta_column.shape[0], 1))
        
        first=np.column_stack((data[:,2], empty))
        lithium_samples = np.column_stack((first, lithium_column))  # Lithium-Spalte zu den anderen Spalten hinzufügen
        deuterium_samples = np.column_stack((lithium_samples, deuterium_column))  # Lithium-Spalte zu den anderen Spalten hinzufügen
        yp_samples = np.column_stack((deuterium_samples, yp_column))  # Lithium-Spalte zu den anderen Spalten hinzufügen
        eta_samples =np.column_stack((yp_samples,eta_column))


        samples=gd.MCSamples(loglikes=data[:,0],weights=data[:,1],samples=yp_samples,names=names2,ignore_rows=0.1)   
        
    
    
    if(i==1):
        samples = []
        data = []
        for file in sample_files:
            sample = np.genfromtxt(pfad + file)
            samples.append(sample)

        data = np.vstack(samples)
        lithium_column = data[:, 34]  # Lithium-Spalte auswählen (Index 34)
        yp_column = data[:, 35]
        deuterium_column= data[:, 36]
        eta_column=data[:,37]
        
        ##HIER EINSTELLBAR WELCHE DATEN AUSGEWÄHLT WERDEN
        
        lithium_samples = np.column_stack((data[:, [2, 4]], lithium_column))  # Lithium-Spalte zu den anderen Spalten hinzufügen
        deuterium_samples = np.column_stack((lithium_samples, deuterium_column))  # Lithium-Spalte zu den anderen Spalten hinzufügen
        yp_samples = np.column_stack((deuterium_samples, yp_column))  # Lithium-Spalte zu den anderen Spalten hinzufügen
        eta_samples = np.column_stack((yp_samples, eta_column))
        samples=gd.MCSamples(loglikes=data[:,0],weights=data[:,1],samples=yp_samples,names=names1,ignore_rows=0.1)
        
    
    return samples

for i in [0,1,2]:
    all_samples1.append(datagen(1,file_path[i]))

for i in [3,4,5]:
    all_samples2.appenda(datagen(0,file_path[i]))  
 

plotter1 = gdplt.get_subplot_plotter()
plotter1.settings.figure_legend_loc=(0.43,0.835)
plotter1.settings.axes_labelsize=28
plotter1.settings.legend_fontsize=25
plotter1.settings.axes_fontsize=17
plotter1.triangle_plot(all_samples1, filled=True, legend_labels=titles1, contour_colors=contour_colors1)


"""
# H_0
for i in range(5):
    plotter1.subplots[i, 0].axvspan(h_min, h_max, color="orange", alpha=0.25)

#Li7    
for i in range(2):
    plotter1.subplots[2, i].axhspan(li_min, li_max, color="orange", alpha=0.25) 
    
#Deuterium    
for i in range(3):
    plotter1.subplots[3, i].axhspan(d_min, d_max, color="orange", alpha=0.25)  
#Helium   
for i in range(4):    
    plotter1.subplots[4, i].axhspan(y_min, y_max, color="orange", alpha=0.25)

plotter1.subplots[3, 3].axvspan(d_min, d_max, color="orange", alpha=0.25)
plotter1.subplots[4, 3].axvspan(d_min, d_max, color="orange", alpha=0.25)
plotter1.subplots[4, 4].axvspan(y_min, y_max, color="orange", alpha=0.25)
"""
plotter1.export("plots/short_mit.pdf")









plotter2 = gdplt.get_subplot_plotter()
plotter2.settings.figure_legend_loc=(0.43,0.82)
plotter2.settings.axes_labelsize=28
plotter2.settings.legend_fontsize=25
plotter2.settings.axes_fontsize=17
plotter2.triangle_plot(all_samples2, filled=True, legend_labels=titles2, contour_colors=contour_colors2) #mit label


"""
# H_0
for i in range(4):
    plotter2.subplots[i, 0].axvspan(h_min, h_max, color="orange", alpha=0.25)

#Li7    
for i in range(2):
    plotter2.subplots[2, i].axhspan(li_min, li_max, color="orange", alpha=0.25) 
    
#Deuterium    
for i in range(3):
    plotter2.subplots[3, i].axhspan(d_min, d_max, color="orange", alpha=0.25)  
#Helium   
for i in range(4):    
    plotter2.subplots[4, i].axhspan(y_min, y_max, color="orange", alpha=0.25)

plotter2.subplots[3, 3].axvspan(d_min, d_max, color="orange", alpha=0.25)
plotter2.subplots[4, 3].axvspan(d_min, d_max, color="orange", alpha=0.25)



plotter2.subplots[4, 4].axvspan(y_min, y_max, color="orange", alpha=0.25)
"""
plotter2.export("plots/short_ohne.pdf")
