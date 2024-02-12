import numpy as np
var=1.05
path="/home/em632080/class/plots/class_public/varying_const/daten9.txt"
first_border = 70

#Erstellen der Z-Daten
#Erstellen der Z-Daten
z1 = np.linspace(0, first_border*2/3, 100) #Um Step clean zu modellieren
z2 = np.linspace(first_border*2/3+0.01,100,2000)
z3 = np.exp(np.linspace(np.log(101), np.log(1e14), 2000)) #fürt restliche Werte


# Grenzen der linearen Funktion
e = 1.0  # end

# Lineare Funktion
def step1(x):
    if x <= first_border:
        return e
    else:
        return var

# Überschreiben der daten.txt für Class x, 1 (alpha), step1(x) me
temp1 = [(x, 1, step1(x)) for x in z1] #x, 1, step1
temp2= [(x, 1, step1(x)) for x in z2] #x, 1, step1
temp3= [(x, 1, var) for x in z3] #x,1,var

temp=temp1+temp2+temp3
np.savetxt(path, temp)