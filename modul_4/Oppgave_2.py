aldersgrense = 18

#Vil få at man ikke er gammel nok
alder = 17

#Vil få man er gammel nok
alder = 18

#Vil få man er gammel nok
alder = 19

if alder > aldersgrense:
    print(f"Du er {alder} år, og er gammel nok")
else:
    print(f"Du er {alder} år, og ikke gammel nok")
print("Takk for at du sjekket")

#Hva skjedde i steg 5 og 6? Hva forteller innrykket og kolonet Python?
#Fikk syntax error.

#Linjen fra steg 7 ble skrevet ut uansett hvilken alder du skrev inn. Hvorfor?
#For den er uavhengig av if statementet, så den kjøres uansett hva som kom over den.

#Uttrykket alder >= aldersgrense kjenner du fra forrige modul. Hva slags verdi gir det? Hvordan bruker if den verdien?
#Den gir om noe er sant eller ikke sant. If bruker for å sjekke om noe stemmer eller om den skal gjøre noe annet.

#I utvidelsen: hvilken av > og >= er riktig for en aldersgrense på 18? Hvorfor er dette en lett feil å gjøre?
#>= er riktig for aldersgrense. Fordi > sjekker kun om noe er større, så for at den skal si riktig hvis verdien er lik som 18, må du ha = sammen