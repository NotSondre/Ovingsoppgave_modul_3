riktig_brukernavn = "michael"
riktig_passord = "python123"

brukernavn = input("Brukernavn: ")
passord = input ("Passord: ")
alder = int(input("Alder: "))

if brukernavn == riktig_brukernavn and passord == riktig_passord and alder < 13:
    print("Du er for ung")
elif brukernavn == riktig_brukernavn and passord == riktig_passord:
    print(f"Velkommen, {riktig_brukernavn}!")
elif brukernavn == riktig_brukernavn:
    print("Feil passord")
elif brukernavn != riktig_brukernavn:
    print("Ukjent bruker")
else:
    print("Ukjent bruker")    

#Vi får logget inn
#Vi får opp feil passord
#Ukjent bruker
#Ukjent bruker