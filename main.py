#Opties=['Kleine friet 2.20','Middel friet 2.50','Grote friet 3.00']
#Extras=['Speciaal+ 1','Stoofvleessaus + 1.8','Geen extras']
#Saus=['Op de frieten of Klein bakje + 0.5','Groot bakje + 0.8','Geen saus']
#Snacks=['Hamburger(Frikandel) Boulet Mexicano Servola 2.30','Kipnuggets Fingers 2.50','Bicky burger 3,20','Geen snack']

Opties=('Kleine friet','Middel friet','Grote friet')
Extras=['Speciaal','Stoofvleessaus','Geen extras']
Saus=['Op de frieten of Klein bakje','Groot bakje','Geen saus']
Snacks=['Frikandel','Boulet/Mexicano/Servola','Kipnuggets/Fingers','Bicky burger','Geen snack']
Factuur=[0]
Totaal=sum(Factuur)
def BTW_berekenen(Totaal):
        Prijs_ex_btw=Totaal/121*100
        BTW=Totaal-Prijs_ex_btw
        print(round(Prijs_ex_btw),2)
        print(round(BTW,2))


Aantal_personen=int(input("Voor hoeveel personen wil je bestellen?: "))
aantal_bestellingen=0
while aantal_bestellingen<Aantal_personen:
        print("Kies uit volgende opties: K,M,G ",Opties)
        keuze=input()
        if keuze.upper()=='K':
                Factuur.append(2.2)
                aantal_bestellingen=aantal_bestellingen+1
        elif keuze.upper()=='M':
                Factuur.append(2.5)
                aantal_bestellingen=aantal_bestellingen+1
        elif keuze.upper()=='G':
                Factuur.append(3.0)
                aantal_bestellingen=aantal_bestellingen+1
        else:
                print('Foute invoer! Kies uit volgende opties: K,M,G',Opties)










print('€',BTW_berekenen(sum(Factuur),'BTW')
print('€',sum(Factuur),'incl. BTW')















