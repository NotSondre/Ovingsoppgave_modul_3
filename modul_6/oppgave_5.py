priser = {"kaffe": 25, "rundstykke": 30, "suppe": 65, "eple": 10}
print(priser["suppe"])  # 65
print(priser["rundstykke"])  # 30

priser["te"] = 20     # Nøkkelen finnes ikke: nytt par legges til
priser["kaffe"] = 28  # Nøkkelen finnes: verdien endres
print (priser)
#print(priser["pizza"])

vare = input("Hva vil du kjøpe? ")
if vare in priser:
    print(f"{vare} koster {priser[vare]} kr.")
else:
    print(f"Beklager, vi har ikke {vare}.")



for rett, pris in priser.items():
    print(f"{rett}: {pris} kr")


kurv = ["kaffe", "rundstykke", "kaffe", "brownie"]
#
# kurv = ["brownie", "brownie", "brownie", "brownie"]

def regn_total(kurv: list[str], priser: dict[str, int]) -> int:
    total = 0
    for vare in kurv:
        if vare in priser:
          total += priser[vare]
    else:
       print(f"{vare} finnes ikke")
    return total

totalpris = regn_total(kurv, priser)
print(f"Totalpris {totalpris}")
