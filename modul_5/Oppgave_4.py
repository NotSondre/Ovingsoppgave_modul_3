def finn_karakter (poeng: int) -> str:
        if poeng > 100:
             return ("Ugyldig poengsum")
        if poeng < 0:
             return ("Ugyldig pengsum")
        if poeng >= 90: 
            return ("A")
        if poeng >= 80:
            return ("B")
        if poeng >= 60:
            return ("C")
        if poeng >= 50:
            return ("D")
        if poeng >= 40:
            return ("E")
        else:
            return ("F")


def skriv_resultat(navn: str, karakter: str) -> None:
    print(f"Navn: {navn}, Karakter: {karakter}")

navn = input("Hva er navnet ditt? ")
karakter = finn_karakter (int(input("Poeng: ")))

skriv_resultat(navn, karakter)

#------------ Del 2 -------------
def doble(tall: int) -> int:
    return tall * 2

print(doble("5"))

#--------------------------------------------------

brus = 24.90
smørbrød = 45
banan = 8.50

def regn_total(brus: float, smørbrød: float, banan: float) -> float:
     return brus + smørbrød + banan
total = regn_total(brus, smørbrød, banan)
print (total)

def legg_til_mva(total: float) -> float:
     return total * 1.25
mva = legg_til_mva(total)
print (mva)

def del_regning(mva: float) -> float:
     return mva / 4
delt_regning = del_regning(mva)
print (delt_regning)