poeng = 0

# Jeg tror poeng blir: 10
poeng = poeng + 10
print(poeng)

# Jeg tror poeng blir: 35
poeng += 25
print(poeng)

# Jeg tror poeng blir: 30
poeng -= 5
print(poeng)

# Jeg tror poeng blir: 60
poeng *= 2
print(poeng)

# Jeg tror poeng blir: 15
poeng /= 4
print(poeng)

# --- Refleksjon ---
#Hvilke av forutsigelsene dine stemte? Der du bommet — hva hadde du tenkt feil?
#Stemte egentlig utenom den siste. Glemte litt at / gir alltid float så jeg skrev 15 i stedet for 15.0

#Hva skjedde med datatypen til poeng i det siste steget? Hvorfor?
#Den ble til en float siden de ble brukt /

#Ga utvidelsen samme resultat som +=? Hva er da poenget med +=?
#Gir renere kode (Du slipper å skrive variabel navnet flere ganger), som gjør den mer leselig