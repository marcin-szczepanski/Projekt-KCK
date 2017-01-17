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

#list = ["Naleśniki z serem"]
list = ["Naleśniki z mięsem"]

def zamow(list): #na podstawie listy tworzy zamówienie
    x = findMeal(list[0])
    if(x!=False):
        y = str(fromMenutoList()[x-1]).split(";",2)[1].lower()
        global kwota
        kwota = kwota + int((fromMenutoList()[x-1]).split(";",2)[-1])
        print("Zamówiono " + y)
    else:
        print("Nie mamy takiego dania! Proszę zamówić coś innego")

def zabierz(x):
    if(x.lower() == "menu"):
        print("Zabrano menu ze stołu")
    if(x.lower() == "talerze"):
        print("Zabrano talerze")

def podejdz():
    print("Kelner podchodzi do stołu")

def odejdz():
    print("Kelner odchodzi od stołu")

def polec():
    x = random.randint(1,17)
    polecam = str(fromMenutoList()[x-1]).split(";",2)[1].lower()
    print("Polecam " + polecam + "!")

zamow(list)
#list = ["Omlet","Jajecznica","Pierogi", "Zupa"]

#zamow(list)
#print(kwota)
#polec()

def zaplac(x): # funkcja do placenia, oblicza sume zamowienia
    if(x.lower() == "karta"):
        print("Wybrano płatność kartą. Kwota do zapłaty to " + str(kwota) + " zł.")
    if(x.lower() == "gotówka"):
        print("Wybrano płatność gotówką. Kwota do zapłaty to " + str(kwota) + " zł.")

#zaplac("KARTA")
#zaplac("gotówka")
