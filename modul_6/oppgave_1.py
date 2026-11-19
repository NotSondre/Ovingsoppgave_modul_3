fruktskal = ["eple", "banan", "pære", "kiwi"]
print(type(fruktskal))

print(fruktskal[0])  # eple
print(fruktskal[1])  # banan
print(fruktskal[3])  # kiwi
print (len(fruktskal))
#print (fruktskal[4])

fruktskal.append("mango")
fruktskal.remove("banan")
print (fruktskal)
print (len(fruktskal))


valgt_frukt = input("Hvilken frukt vil du ha? ")

if valgt_frukt in fruktskal:
    fruktskal.remove(valgt_frukt)
    print(f"Værsågod, her er en {valgt_frukt}!")
else:
print(fruktskal[-1])