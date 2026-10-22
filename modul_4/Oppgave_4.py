#alder = 25
#er_student = True
#har_medlemskort = False

#Den blir false
#print (alder < 12 or alder > 67)

#Den blir true
#print (er_student and alder < 30)

#Den blir true
#print (not har_medlemskort)

#Den blir false
#print (er_student and har_medlemskort)

#True
#print (er_student or har_medlemskort)

#Den blir true
#print (not er_student or alder < 30)


#-----------------------------DEL 2-----------------------------------
alder = int(input("Alder: "))
er_student = input("Er du student? (ja/nei) ").lower() == "ja"

if alder < 12 or alder > 67:
    print (f"Du kommer inn gratis")
elif er_student and alder < 30:
    print (f"50kr")
else:
    print(f"120kr")

if not er_student:
    print ("studenter under 30 år får rabatt")

#8 år, ikke student
#Kommer inn gratis, tips om student

#70 år, ikke student
#Kommer inn gratis, tips om student

#22 år, student
#Student prisen

#35 år, student
#ordinær pris og ikke tips om student

#25 år, ikke student
#Ordniærpris tips om student