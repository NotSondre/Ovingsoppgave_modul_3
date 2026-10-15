navn = input("Hva er navnet ditt? ")
print ("Hei,", navn)
print (f"Hei, {navn}!")


alder = input("Hvor gammel er du? ")
print (type(alder))
alder = int(alder)
print (alder + 1)
print (type(alder))
print (f"Du blir {alder + 1} til neste år!")

høyde = input("Hvor høy er du? ")
høyde = float(høyde)
print (høyde)


#Hva svarte type() på alderen før du brukte int()? Hvorfor tror du input() gir deg akkurat denne datatypen?
#Den svarte med str. Jeg tror det er siden input tar svar fra tastatur som er tekst

#Hva klaget Python på i steg 5? Beskriv feilmeldingen med egne ord.
#Den klagde på at alder var en string som gjorde at den ikke kunne regne ut svaret

#Sammenlign print("Hei,", navn) og f-strengen. Hvilken synes du er lettest å lese? Hva skjer med mellomrommene i de to variantene?
#f stringen var lettere å lese, spesielt om man skal ha lengere setninger. Siden man trenger ikke å starte og slutte en string hver gang man skal ha inn en variabel.

#Hva tror du skjer hvis brukeren skriver tretti i stedet for 30? Prøv.
#Får feilmeldingen siden vi gjorde svaret til en integer, men tretti er en string