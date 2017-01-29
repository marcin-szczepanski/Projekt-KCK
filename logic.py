import linecache
import clear
import random

##################################

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
    if (a == 0):
        danie_blad = "Chcesz zamówić danie, którego nie ma w menu! Proszę zamów coś innego :)"
        return (danie_blad+"\n", "Niestety dania nie ma w naszej karcie.","")
    for i in range(0,a):
        tab.append(findMeal(list[i][1]))
        if(tab[i]!=False) and (tab != []):
            ilosc = list[i][0]
            global kwota
            kwota = kwota + int(ilosc)*int((fromMenutoList()[tab[i]-1]).split(";",2)[-1])
            dania_komunikat += (odmiana(list,i)) + "\n"
            dania_stolik += (odmiana(list,i)) + "\n"
        else:
            danie_blad = "Chcesz zamówić danie, którego nie ma w menu! Proszę zamów coś innego :)"
            return (danie_blad+"\n", "Niestety dania nie ma w naszej karcie.","")
    return ("Zamówiono: \n" + dania_komunikat, "Przyjąłem zamówienie. \n", dania_stolik)


def odmiana(list, i):  #służy do skomplikowania wyjścia, np. zamówiono 2 serniki ale już dla 5 sztuk mamy zamówiono 5 serników
        ilosc = list[i][0]
        inMenu = findMeal(list[i][1])
        if(ilosc > 4):
            return(str(ilosc) + menuOdmienionetoArray()[inMenu-1][4])
        else:
           return(menuOdmienionetoArray()[inMenu-1][ilosc-1])

def zabierz(list):
    x = list[1][0]
    if (x=="naczynie"):
        x="talerz"
    if (x=="karta"):
        x="menu"
    return("Zabrano: " + x + "\n", "Już zabieram. \n", x)

def przyniesF(list):
    if list[0][0] == "przyniesienie":
        list[0][0] = list[1][0]
    x = list[0][0]
    if (x=="karta"):
        x="menu"
    return("Przyniesiono: " + x + "\n", "Proszę bardzo. \n", x)

def odejdz():
    return("Kelner odchodzi od stołu \n","","")

def podejdz():
    return("","","podejdz")

def polec():
    x = random.randint(1,13)
    polecam = str(fromMenutoList()[x-1]).split(";",2)[0].lower()
    return("Polecono: " + polecam, "Dzisiaj polecamy " + polecam + "! \n")

def zaplac(): # funkcja do placenia, oblicza sume zamowienia
       return("Kwota do zapłaty to " + str(kwota) + " zł.", "Proszę o zapłatę " + str(kwota) + " \n", str(kwota))
	
def error(): ### gdy nie zrozumiemy o co chodzi klientowi :)
    return("Nie zrozumiałem.  \n","","")

###############################	

def clbadwds(list): ### funkcja czyści niepotrzebne słowa dla funkcji prosic()
	args = []
	while (list):
		if list[0][1] != 'NUMCRD':
			args.append(list.pop(0))
		else:
			list.pop(0)
	return (args)

def zamow(list): ### funkcja przekształca listę do postaci argumentów postaci [liczebnik, string z nazwą dania]
	meals = []
	count = len(list)//3
	print(list)
	if (len(list) % 3) != 0:
		return (error())
	meals = [[[None] for col in range(2)] for row in range(count)]
	for i in range(count):
		number = list.pop(0)
		meals[i][0] = int(number[0])
		noun = list.pop(0)
		adj = list.pop(0)
		meals[i][1] = noun[0] + " " + adj[0]
	ret = zamowF(meals)
	return (ret)

def prosic(list, file="words.txt"):
	f = open(file, mode="r+")
	j = 0
	k = 0
	action = ''
	word = ''
	count = len(f.readlines())+1
	c = len(list)
	while (j != c):
		for i in range(count):
			wiersz = linecache.getline(file, i).split(";")
			word = list[j][0]
			if word in wiersz:
				action = wiersz[-1].replace("\n","")
				k = 1
				break
		j = j + 1
		if k != 0:
			break
	f.close();
	if action == '':
		ret = zamow(list)
	else:
		value = whataction(action)
		how_many_args = value[1]
		word = value[0]
		possibles = globals().copy()
		possibles.update(locals())
		method = possibles.get(word)
		listargs = clbadwds(list)
		args = []
		while (listargs):
			args.append(listargs[0])
			listargs.pop(0)
		if how_many_args != '0':
			ret = method(args)
		else:
			ret = method()
	return (ret)

def createobjectslist(wordlist = '', listofpartsofspeech = ''): ## tworzy listę obiektów: [[słowa],[odpowiadające części mowy]]
	w = wordlist.split(" ")
	l = listofpartsofspeech.split(" ")
	count = len(w)
	tab = [[[None] for col in range(2)] for row in range(count)]
	for i in range(count):
		tab[i][0] = w[i]
		tab[i][1] = l[i]
	return(tab)

def whataction(word, file = "synonymous_words.txt" ):
    f = open(file, mode="r+")
    count = len(f.readlines())+1
    k = 0
    for i in range(count):
	    wiersz = linecache.getline(file, i).split(";")
	    if word in wiersz:
		    action=wiersz[-2]
		    how_many_args=wiersz[-1]
		    how_many_args = how_many_args.replace("\n","")
		    k = 1
		    break;
    f.close()
    if k == 0:
	    action = "error"
	    how_many_args = '0'
    return(action, how_many_args)


def understanding(s):
	x=clear.wordtoinfinitive(s)
	wordlist = x[0]
	listofpartsofspeech = x[1]
	list = createobjectslist(wordlist, listofpartsofspeech)
	count = len(list)
	action = "error"
	for i in range(count):
		if list[i][1] == 'V':
			action_list = list.pop(i)
			action = action_list[0]
			break;
	value = whataction(action)
	word = value[0]
	how_many_args = value[1]
	possibles = globals().copy()
	possibles.update(locals())
	method = possibles.get(word)
	args = []
	while (list):
		args.append(list[0])
		list.pop(0)
	if how_many_args != '0':
		ret = method(args)
	else:
		ret = method()
	return (ret)

##x=understanding("poproszę napój")
##print(x)
