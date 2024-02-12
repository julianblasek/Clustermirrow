import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

data = np.genfromtxt("/home/em632080/class/plots/class_public/varying_const/daten3.txt")
z = data[:, 0]
m = data[:, 2]

# Erstelle den Plot
plt.figure(figsize=(12, 6.75), dpi=400)
plt.grid()
plt.title("Stepfunction", fontsize=16)
plt.xlabel("$Log(z)$", fontsize=14)
plt.ylabel("${m_{e}}^*$", fontsize=14)

# Verwende eine logarithmische Skala auf der x-Achse
plt.xscale('log')
plt.plot(z, m)

# Erzeuge benutzerdefinierte Ticks für die x-Achse in Potenzschreibweise
def format_func(value, tick_number):
    # Konvertiere die Potenz in eine Potenzschreibweise ohne die '0'
    exponent = int(np.log10(value))
    return fr"$10^{{{exponent}}}$"

plt.gca().xaxis.set_major_formatter(FuncFormatter(format_func))
plt.tick_params(labelsize=12)
plt.savefig("test.pdf")
