favoritter = ["Mario Kart", "Super Smash Bros", "Donkey Kong", "Octopath Traveler"]

# Runde | Verdien til favoritt | Skrives ut
# 1     |                      |
# 2     |                      |
# 3     |                      |
# 4     |                      |

for favoritt in favoritter:
    print(f"Jeg anbefaler {favoritt}")
print("Ferdig med lista!")

#Del 2-------------------

for tall in range(5):
    print(tall)

tall = int(input("Skriv tall: "))
for gange_tabell in range(1, 11):
    print(f"{tall} x {gange_tabell} = {tall * gange_tabell}")


utgifter = [45, 30, 62, 28, 55]  # Hva du brukte i kantina hver dag denne uka

total = 0
for belop in utgifter:
    total += belop  # Samme som: total = total + belop

for gjennomsnitt in range(0,20,5):
    total / len(utgifter)

print (gjennomsnitt)
print(f"Denne uka brukte du {total} kr i kantina.") #220