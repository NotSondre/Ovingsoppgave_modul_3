poeng = input("Antall Poeng: ")
poeng = int(poeng)

if poeng > 100:
    print("Ugyldig poengsum")
elif poeng >= 90: 
    print("A")
elif poeng >= 80: 
    print("B")
elif poeng >= 60: 
    print ("C")
elif poeng >= 50: 
    print ("D")
elif poeng >= 40: 
    print ("E")
elif poeng < 40:
    print ("F")
else:
    print ("Ugyldig poengsum")

#Test programmet med 95, 72, 40 og 12. Skriv en kommentar med hva du forventer før du kjører.
#95=A, 72=C, 40=E, 12=F

#Lag en kopi av kjeden, men snu rekkefølgen slik at du sjekker E først (if poeng >= 40) og A sist. Hva tror du 95 poeng gir nå? Skriv det ned, og kjør.
#Du vil få E siden poengsummen oppfyller det første kravet som er spurt (om den er over 40)

#Sett den riktige rekkefølgen tilbake, men bytt ut alle elif med if. Kjør med 95 poeng igjen.
#Den vil printe ut alle karakterer utenom F siden den oppfyller alle IF statementsa

#For B skriver vi bare poeng >= 80. Hvorfor trenger vi ikke også sjekke at poengene er under 90?
#Fordi om poengsummen oppfyller kravet for A sjekker den aldri lenger ned i if statementet

#Når kjører else-delen?
#Når alle andre ledd ikke har kjørt
