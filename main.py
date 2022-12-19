#Opties=['Kleine friet 2.20','Middel friet 2.50','Grote friet 3.00']
#Extras=['Speciaal+ 1','Stoofvleessaus + 1.8','Geen extras']
#Saus=['Op de frieten of Klein bakje + 0.5','Groot bakje + 0.8','Geen saus']
#Snacks=['Hamburger(Frikandel) Boulet Mexicano Servola 2.30','Kipnuggets Fingers 2.50','Bicky burger 3,20','Geen snack']

Opties=('Kleine friet','Middel friet','Grote friet')
Extras=['Speciaal','Stoofvleessaus','Geen extras']
Saus=['Op de frieten of Klein bakje','Groot bakje','Geen saus']
Snacks=['Frikandel/Boulet/Mexicano/Servola','Kipnuggets/Fingers','Bicky burger','Geen snack']
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
print('Wil je Extras?: SP/SV/G ',Extras)
aantal_bestellingen=0
while aantal_bestellingen<Aantal_personen:
        print("Kies uit volgende opties: SP/SV/G",Extras)
        keuze=input()
        if keuze.upper()=='SP':
                Factuur.append(1)
                aantal_bestellingen=aantal_bestellingen+1
        elif keuze.upper()=='SV':
                Factuur.append(1.8)
                aantal_bestellingen=aantal_bestellingen+1
        elif keuze.upper()=='G':
                Factuur.append(0)
                aantal_bestellingen=aantal_bestellingen+1
        else:
                print('Foute invoer! Kies uit volgende opties: SP/SV/G',Extras)


print('Wil je Snacks erbij?: Ja/Nee: ')
ja_nee=input()
if ja_nee.upper=='nee':
        print('€', sum(Factuur), 'incl. BTW')
elif ja_nee.upper=='ja':
      print('Geef nu g1/g2/g3/Stop',Snacks)
keuze=input()
        while keuze.upper!='stop':
                if keuze.upper() == 'g1':
                        Factuur.append(2.3)
                elif keuze.upper() == 'g2':
                        Factuur.append(2.5)
                elif keuze.upper() == 'g3':
                        Factuur.append(3.0)
        else:
        print('Foute invoer! Kies uit volgende opties: g1/g2/g3/Stop', Snacks)
else:  print('Foute invoer! Wil je Snacks erbij?: Ja/Nee: ')






















