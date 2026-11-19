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