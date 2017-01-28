import random

kwota = 0

def findMeal(x): #funkcja do znajdywania w pliku menu.txt odpowiedniego posiłku, o który prosi klient
    lista = []
    isItFound = False
    lines = 0
    with open('Menu.txt', 'r', encoding='utf-8') as searchfile:
        for line in searchfile:
            lines = lines + 1
            if x in line:
                line = line[0:line.find(';')]
                lista.append(line.rstrip('\n'))
                break
        a = len(lista)
        if a>0:
            return lines
        else:
            return False


def fromMenutoList(): #wczytuje menu.txt i tworzy z niego listę
    MenuLista = []
    with open('Menu.txt', 'r', encoding='utf-8') as searchfile:
        for line in searchfile:
            MenuLista.append(line.rstrip('\n'))
    return MenuLista


def menuOdmienionetoArray(): #wczytuje plik menuOdmienione i tworzy z niego listę
    with open('menuOdmienione.txt', 'r', encoding='utf-8') as f:
        results = []
        for line in f:
            results.append(line.strip().split(';'))
        return results

def zamowF(list): #na podstawie listy tworzy zamówienie
    a = len(list)
    tab = []
    dania_komunikat = ""
    dania_stolik = ""
    for i in range(0,a):
        tab.append(findMeal(list[i][1]))
        if(tab[i]!=False):
            ilosc = list[i][0]
            global kwota
            kwota = kwota + int(ilosc)*int((fromMenutoList()[tab[i]-1]).split(";",2)[-1])
            dania_komunikat += (odmiana(list,i)) + "\n"
            dania_stolik += (odmiana(list,i)) + "\n"
        else:
            danie_blad = "Chcesz zamówić danie, którego nie ma w menu! Proszę zamów coś innego :)"
            return (danie_blad, "Niestety dania nie ma w naszej karcie.","")
    return (dania_komunikat, "Przyjąłem zamówienie", dania_stolik)


def odmiana(list, i):  #służy do skomplikowania wyjścia, np. zamówiono 2 serniki ale już dla 5 sztuk mamy zamówiono 5 serników
        ilosc = list[i][0]
        inMenu = findMeal(list[i][1])
        if(ilosc > 4):
            return(str(ilosc) + menuOdmienionetoArray()[inMenu-1][4])
        else:
           return(menuOdmienionetoArray()[inMenu-1][ilosc-1])


def zabierz(list):
    if list[0][0] == "zabranie":
        list[0][0] = list[1][0]
    x = list[0][0]
    return("Zabrano: " + x + "\n", "Już zabieram.", x)

def przyniesF(list):
    if list[0][0] == "przyniesienie":
        list[0][0] = list[1][0]
    x = list[0][0]
    return("Przyniesiono " + x + "\n", "Proszę bardzo.", x)

def odejdz():
    return("Kelner odchodzi od stołu")

def polec():
    x = random.randint(1,19)
    polecam = str(fromMenutoList()[x-1]).split(";",2)[0].lower()
    return("Polecono: " + polecam, "Dzisiaj polecamy " + polecam + "!")

def zaplac(): # funkcja do placenia, oblicza sume zamowienia
    return("Kwota do zapłaty to " + str(kwota) + " zł.", "Proszę o zapłatę " + str(kwota), "Rachunek: " + str(kwota))



##list = [[20, "pierogi ruskie"],[1, "sałatka jarzynowa"],[3, "naleśniki serowe"],[4,"jabłecznik"]]
##print(zamowF(list))
##print(zaplac())
##print (polec())
