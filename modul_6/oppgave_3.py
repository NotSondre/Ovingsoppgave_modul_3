teller = 5

while teller >0:
    print(teller)
    teller -= 1  # Samme som: teller = teller - 1

print("Kaffepause!")


#-------------------
riktig_brukernavn = "michael"
riktig_passord = "python123"
forsok = 0
innlogget = False

for forsok in range(3):
    brukernavn = input("Skriv inn riktig brukernavn: ")
    passord = input("Skriv inn riktig passord: ")
    if brukernavn == riktig_brukernavn and passord == riktig_passord:
        print(f"Velkommen, {riktig_brukernavn}!")
        innlogget = True
        break
    elif brukernavn != riktig_brukernavn and passord != riktig_passord:
        print ("Feil brukernavn eller passord. Prøv igjen!!!")
        forsok += 1
        print(f"Du har {3-forsok} forsøk igjen")

if innlogget == False:
    print("For mange feil forsøk. Kontoen er låst.")