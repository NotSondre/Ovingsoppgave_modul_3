def doble_print(tall):
    print(tall * 2)

def doble_return(tall):
    return tall * 2
    print("Ferdig!")

a = doble_print(5)
b = doble_return(5)
print(a)
print(b)

print(doble_return(5) + 1)
print(doble_return(doble_return(3)))

def regn_areal(lengde, bredde):
    return lengde * bredde

def skriv_areal(lengde, bredde):
    print (f"Areal: {lengde * bredde}")

c = regn_areal(5, 10)
print(c)
skriv_areal(10, 10)