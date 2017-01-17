import random

kwota = 0

def findMeal(x):
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


def fromMenutoList():
    MenuLista = []
    with open('Menu.txt', 'r', encoding='utf-8') as searchfile:
        for line in searchfile:
            MenuLista.append(line.rstrip('\n'))
    return MenuLista

list = ["Zupa","Naleśniki","Gołąbek","Omlet","Jajecznica","Pierogi", "Zupa"]

def zamow(list):
    x = findMeal(list[0])
    if(x!=False):
        y = str(fromMenutoList()[x-1]).split(";",2)[1].lower()
        print("Zamówiono " + y)

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
polec()
