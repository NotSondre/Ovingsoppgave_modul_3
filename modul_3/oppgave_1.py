navn = "Sondre"
alder = 23
høyde = 1.89
er_student = True
hobbyer = ["Foto", "Gaming", "Gåing"]

print("Navn:", navn)
print("Alder:", alder)
print("Høyde:", høyde)
print("Er_student:", er_student)
print("Hobbyer:", hobbyer)

print("Hobbyer:", hobbyer)
print("Er_student:", er_student)
print("Høyde:", høyde)
print("Alder:", alder)
print("Navn:", navn)

print(type(navn))
print(type(alder))
print(type(høyde))
print(type(er_student))
print(type(hobbyer))

# --- Refleksjon ---
#Måtte du flytte på variablene for å endre rekkefølgen på utskriften? Hvorfor / hvorfor ikke?
#Trengte ikke det siden det er print rekkefølgen som bestemmer utskriften

#Hva svarte Python på type()? Stemte det med datatypene som er diskutert i pensum?
#Den svarte med hvilke datatype variablen var og det stemte med pensum

#Hvorfor tror du Python må vite hvilken datatype en variabel har?
#For at den skal  gjøre riktig handling. For eksempel om et 3 tall skal bli brukt som en verdi eller tekst (3, "3")