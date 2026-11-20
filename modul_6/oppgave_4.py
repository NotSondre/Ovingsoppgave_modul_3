ukedager = ("mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag")
#ukedager.append("lillelørdag")
#ukedager[0] = "fridag"
print (ukedager[0])
print (ukedager[4])
print (len(ukedager))

for ukedag in ukedager:
    print (f"Det er {ukedag}!")

#-------------------del 2
pameldinger = ["Ada", "Linus", "Grace", "Ada", "Guido", "Linus", "Ada"]
len(pameldinger)

deltakere = set(pameldinger)
deltakere.add("Margaret")
deltakere.add("Grace")
print(deltakere)
print(len(deltakere))

if "Ada" in deltakere:
    print(f"Ada er her!")
else:
    print("Ada har gått bort")

for deltakere in deltakere:
    print (f"Velkommen {deltakere}!")