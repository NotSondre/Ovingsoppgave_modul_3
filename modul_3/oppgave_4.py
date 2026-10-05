poeng = 0

# Jeg tror poeng blir: 10
poeng = poeng + 10
print(poeng)

# Jeg tror poeng blir: 20
poeng += 10
print(poeng)

# Jeg tror poeng blir: 45
poeng += 25
print(poeng)

# Jeg tror poeng blir: 40
poeng -= 5
print(poeng)

# Jeg tror poeng blir: 80
poeng *= 2
print(poeng)

# Jeg tror poeng blir: 20
poeng /= 4
print(poeng)

# --- Refleksjon ---
#Hvilke av forutsigelsene dine stemte? Der du bommet — hva hadde du tenkt feil?
#Stemte egentlig utenom den siste. Glemte litt at / gir alltid float så jeg skrev 20 i stedet for 20.0

#Hva skjedde med datatypen til poeng i det siste steget? Hvorfor?
#Den ble til en float siden de ble brukt /

#Ga utvidelsen samme resultat som +=? Hva er da poenget med +=?
#Gir renere kode (Du slipper å skrive variabel navnet flere ganger), som gjør den mer leselig