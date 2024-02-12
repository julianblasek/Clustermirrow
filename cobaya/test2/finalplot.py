import numpy as np
import getdist as gd
import getdist.plots as gdplt
import matplotlib.pyplot as plt
import getdist
from getdist import MCSamples, chains
# Enable LaTeX rendering
plt.rcParams['text.usetex'] = True


all_samples1 = []
all_samples2=[]

titles1 = ["without el. fractions in likelihood", "with Li, He, D in likelihood", "with He, D in likelihood"]
contour_colors1 = ['blue', 'red', 'green']

titles2 = ["without el. fractions in likelihood", "with Li, He, D in likelihood", "with He, D in likelihood"]
contour_colors2 = ['blue', 'red', 'green']


file_path=["./step3/chains/","./step1/chains/","./step2/chains/","./raw2/chains/","./raw1/chains/","./raw4/chains/"]
sample_files = ["1.txt", "2.txt", "3.txt", "4.txt", "5.txt", "6.txt", "7.txt", "8.txt", "9.txt", "10.txt"]

names1 = [r'$H_0$', r'$m_{e}^x$',  r'$^7Li/H$', r'$D/H$', r'$Y_p$']
names2 = [r'$H_0$',  r'$^7Li/H$', r'$D/H$', r'$Y_p$']


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
        
        lithium_samples = np.column_stack((data[:,2], lithium_column))  # Lithium-Spalte zu den anderen Spalten hinzufügen
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
        
        lithium_samples = np.column_stack((data[:, [2, 5]], lithium_column))  # Lithium-Spalte zu den anderen Spalten hinzufügen
        deuterium_samples = np.column_stack((lithium_samples, deuterium_column))  # Lithium-Spalte zu den anderen Spalten hinzufügen
        yp_samples = np.column_stack((deuterium_samples, yp_column))  # Lithium-Spalte zu den anderen Spalten hinzufügen
        eta_samples = np.column_stack((yp_samples, eta_column))
        samples=gd.MCSamples(loglikes=data[:,0],weights=data[:,1],samples=yp_samples,names=names1,ignore_rows=0.1)
        
    
    return samples

for i in [0,1,2]:
    all_samples1.append(datagen(1,file_path[i]))

for i in [3,4,5]:
    all_samples2.append(datagen(0,file_path[i]))    



def gesamt_mittel_std(mittelwerte, std_abweichungen):
    # Prüfen, ob die Längen der Arrays übereinstimmen
    if len(mittelwerte) != len(std_abweichungen):
        raise ValueError("Die Arrays müssen die gleiche Länge haben.")

    # Anzahl der Werte im Array
    n = len(mittelwerte)

    # Berechne den gesamten Mittelwert und die gesamte Standardabweichung
    gesamt_mittelwert = np.mean(mittelwerte)
    gesamt_std_abweichung = np.sqrt(np.sum(std_abweichungen**2 + (mittelwerte - gesamt_mittelwert)**2) / n)

    return gesamt_mittelwert, gesamt_std_abweichung

def getmean_std(samples):
    
    means=[]
    for i in samples:
        means.append(chains.Chains.getMeans(i))
        
        
    stds=[]
    for i in samples:
        stds.append(chains.Chains.getVars(i))
        
    return np.vstack(means), np.vstack(np.sqrt(stds))
        






means1,stds1=getmean_std(all_samples1)
means2,stds2=getmean_std(all_samples2)





mittelwerte=[]
fehler=[]

for i in range(3):

    mittelwerte.append([file_path[i],means1[i]])
    fehler.append([file_path[i],stds1[i]])
    
for i in range(3):
    mittelwerte.append([file_path[i+3],means2[i]])
    fehler.append([file_path[i+3],stds2[i]])
    

print(" ")
print(titles2[1])    
print(" ")
print(mittelwerte[4])
print(" ")
print(fehler[4])
print("-------------------------- ")

print(" ")
print(titles2[2])    
print(" ")
print(mittelwerte[5])
print(" ")
print(fehler[5])
print("-------------------------- ")