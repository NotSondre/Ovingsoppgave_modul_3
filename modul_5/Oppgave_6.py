def regn_pris(antall, pris_per_stk):
    return antall * pris_per_stk
    

def skriv_kvittering(navn, total):
    print(f"Kvittering for {navn}")
    print(f"Totalt: {total} kr")
 
def avslutt():
    print("Takk for handelen!")

pris = regn_pris(3, 49.90)
total = pris
skriv_kvittering("Michael", pris)
print(f"Du betalte {total} kr.")
avslutt()