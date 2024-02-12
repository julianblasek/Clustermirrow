import numpy as np
import getdist as gd
import getdist.plots as gdplt
import matplotlib.pyplot as plt

file_path=["./step3/chains/","./step1/chains/","./step2/chains/","./raw1/chains/","./raw2/chains/"]
file_names=["Mit Step ohne BBN-El","Mit Step mit BBN-El","Mit Step mit BBN-El ohne Li7","Ohne Step mit BBN-El","Ohne Step ohne BBN-El"]
sample_files = ["1.txt", "2.txt", "3.txt", "4.txt", "5.txt", "6.txt", "7.txt", "8.txt", "9.txt", "10.txt"]

names1 = [r'$H_0$', r'$\log{A}$', r'$m_{e}^x$', r'$n_s$', r'$\Omega_b$', r'$\Omega_{cdm}$', r'$\tau$', r'$A_{planck}$', r'$^7Li/H$', r'$D/H$', r'$Y_p$', r'$\eta$']
names2 = [r'$H_0$', r'$\log{A}$', r'$n_s$', r'$\Omega_b$', r'$\Omega_{cdm}$', r'$\tau$', r'$A_{planck}$', r'$^7Li/H$', r'$D/H$', r'$Y_p$', r'$\eta$']

def vis2(pfad,title):
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
    
    lithium_samples = np.column_stack((data[:, 2:9], lithium_column))  # Lithium-Spalte zu den anderen Spalten hinzufügen
    deuterium_samples = np.column_stack((lithium_samples, deuterium_column))  # Lithium-Spalte zu den anderen Spalten hinzufügen
    yp_samples = np.column_stack((deuterium_samples, yp_column))  # Lithium-Spalte zu den anderen Spalten hinzufügen
    eta_samples = np.column_stack((yp_samples, eta_column))


    samples=gd.MCSamples(loglikes=data[:,0],weights=data[:,1],samples=eta_samples,names=names2,ignore_rows=0.1)
    return samples


all_samples = []
titles = ["with Li, He, D in likelihood", "without el. fractions in likelihood"]
contour_colors = ['blue', 'red']


for i in range(3,5):
    all_samples.append(vis2(file_path[i], file_names[i]))

# Create a single triangle plot for all the samples
plotter = gdplt.get_subplot_plotter()
plotter.settings.figure_legend_loc=(0.6,0.8)
plotter.settings.axes_labelsize=32
plotter.settings.legend_fontsize=30
plotter.settings.axes_fontsize=18
plotter.triangle_plot(all_samples, filled=True, legend_labels=titles, contour_colors=contour_colors)
#SH0ES Werte
h_min, h_max = 0.7304 - 0.0104, 0.7304 + 0.0104
li_min, li_max = 1.6e-10 - 0.03e-10, 1.6e-10 + 0.03e-10
d_min, d_max = 2.54e-5 - 0.04e-5, 2.54e-5 + 0.04e-5
y_min, y_max = 0.2449 - 0.004, 0.2449 + 0.004
# H_0
for i in range(11):
    plotter.subplots[i, 0].axvspan(h_min, h_max, color="orange", alpha=0.25)

#Li7    
for i in range(8):
    plotter.subplots[7, i].axhspan(li_min, li_max, color="orange", alpha=0.25) 
    
#Deuterium    
for i in range(8):
    plotter.subplots[8, i].axhspan(d_min, d_max, color="orange", alpha=0.25)  
#Helium   
for i in range(9):    
    plotter.subplots[9, i].axhspan(y_min, y_max, color="orange", alpha=0.25)

plotter.subplots[8, 8].axvspan(d_min, d_max, color="orange", alpha=0.25)
plotter.subplots[9, 8].axvspan(d_min, d_max, color="orange", alpha=0.25)
plotter.subplots[10, 8].axvspan(d_min, d_max, color="orange", alpha=0.25)
plotter.subplots[9, 9].axvspan(y_min, y_max, color="orange", alpha=0.25)
plotter.subplots[10, 9].axvspan(y_min, y_max, color="orange", alpha=0.25)
plotter.export("plots/combined_ohne_step.pdf")
