brus = 24.90
smørbrød = 45
banan = 8.50

print("Totalsum for alle varene er", brus + smørbrød + banan, "kr")
print("Totalsum med 25% mva for alle varene er", (brus + smørbrød + banan) * 1.25, "kr")
print("Totalsum om 4 personer deler på summen likt er", (brus + smørbrød + banan) * 1.25 / 4, "kr")
print("prisforskjellen mellom den dyreste og billigste varen er", smørbrød - banan, "kr")

# --- Refleksjon ---
#smørbrød er et heltall, brus er et desimaltall. Hva slags datatype ble svaret da du la dem sammen?
#Det ble float siden der et desimaltall

#Hva ble datatypen da du delte på fire? Ble du overrasket?
#Datatypen ble til en float. Er ikke overrasket siden / operatoren vil alltid gi float

#Hvorfor er det en fordel å bruke variabler i stedet for å skrive tallene på nytt hver gang? Tenk på hva som skjer hvis prisen på brus endrer seg.
#For da trenger man kun å endre verdien på en plass i stedet for alle steder i koden