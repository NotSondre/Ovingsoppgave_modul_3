handlekurv = ["melk", "brød", "ost", "egg"]
priser = [22, 35, 89, 45]

print("Varer i handlekurven:")
for i in range(0, len(handlekurv)):
    print(f"- {handlekurv[i]}")

total = 0
for pris in priser:
    total += pris

print(f"Totalt: {total} kr")

if len(handlekurv) == 0:
    print("Handlekurven er tom.")

print("Din tur kommer om:")
teller = 3
while teller >= 1:
    print(teller)
    teller -= 1
print("Neste kunde!")