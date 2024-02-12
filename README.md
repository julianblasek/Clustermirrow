Vorweg Kommentare kaum vorhanden, Übersicht ist katastrophal und Bezeichnungen der Ordner und Dateien noch schlimmer, sorry schon mal dafür. Submodules (PRyMordial, Cobaya etc ...) sind nicht drin.

cobaya/test2 -- wird lediglich verwendet um die chains zu speichern

class/ --  enthält die verschiedenen Class Versionen welche für die verschiedenen Funktionen (stepfunction, raw, powerlaw etc.) verwendet wurden 

software/cobaya --  liklihoods

software/cobayafork/test2 -- enthält Submodules Cobaya & PRyMordial und die Dateien (bspw. step.py, step2.py) welche für verschiedenen Konfigurationen (mit/ohne BBN ...) das Sampling starten. Wobei erwähnt werden muss, dass wir (aufgrund von Zeitproblemen) lediglich step-, step2-, step3-, raw.py verwendet haben.

main.py -- Datei welche benutz wurde um Prymordial jedes mal neu zu initialisieren, da wir das Problem mit den globalen variablen hatten. (software/cobayafork/test2/PRyMordial/main.py) 

VG
