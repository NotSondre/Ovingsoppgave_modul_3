riktig_svar = "Oslo"

svar = input("Hva er hovedstaden i Norge? ")

if svar == riktig_svar:
    print("Riktig!")
else:
    print("Feil, svaret var", riktig_svar)

alder = input("Hvor gammel er du? ")
alder = int(alder)
if alder == 18:
    print("Du er akkurat myndig!")
else:
    print("Du er ikke 18.")

#Du vil ikke få riktig om man bruker 18 siden alder er ikke gjort til et int. Så du vil få feil.

