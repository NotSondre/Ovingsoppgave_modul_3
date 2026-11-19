#def lag_hilsen():
#    melding = "Hei!"
#    print(melding)

#lag_hilsen()
#print(melding) 

#by = "Oslo"

#def skriv_by():
#    print(f"Jeg bor i {by}.")

#skriv_by()

#def doble(tall):
#    tall = tall * 2
#    print(f"Inne: {tall}")

#tall = 5
#doble(tall)
#print(f"Ute: {tall}")

#Del 2
poeng = 0

def legg_til_poeng(poeng: int) -> int:
    return poeng + 10 + 25


def trekk_fra_poeng(poeng: int, antall: int) -> int:
    return poeng + antall


poeng = 0
antall = 5
poeng = legg_til_poeng(poeng)
antall = trekk_fra_poeng (poeng, antall)
poeng = antall
print(poeng)


